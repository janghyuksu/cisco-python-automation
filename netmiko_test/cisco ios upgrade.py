from netmiko import ConnectHandler

# 장비에 대한 정보
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.120.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : '!@3456Qwerty',
    'port': 22,
}

# Netmiko를 사용하여 장비에 연결
ssh_connection = ConnectHandler(**device)

# 1. 업그레이드 파일을 장비에 복사합니다.
#scp_conn = ssh_connection.connect_ssh_scp()
#scp_conn.scp_transfer_file("upgrade_image.bin", remote_file="flash:/upgrade_image.bin")

# 2. 장비의 현재 IOS 버전을 확인합니다.
output = ssh_connection.send_command("show version | include System image file is")
current_image = output.split()[5]
print(f"Current IOS version: {current_image}")

# 3. 업그레이드 파일을 사용하여 IOS를 업그레이드합니다.
command = f"boot system flash:/c2960x-universalk9-mz.152-4.E8.bin"
ssh_connection.send_config_set(command)
ssh_connection.save_config()

# 4. 업그레이드 후, 장비를 재부팅합니다.
output = ssh_connection.send_command_expect("reload")
if "confirm" in output:
    ssh_connection.send_command_timing("y")
    print("Reloading device...")
else:
    print("Failed to reload device.")
   
# 연결 종료
ssh_connection.disconnect()

