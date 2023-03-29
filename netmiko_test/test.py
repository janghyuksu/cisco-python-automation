from netmiko import ConnectHandler 
#라이브러리 Connect에 클래스 가져오기

device1 = {
    "device_type": "cisco_ios",
    "host":"192.168.120.1",
    "username" : "cisco",
    "password" : "cisco",
    "secret" : "!@3456Qwerty",
    "port" : "22"
}
#connection = ConnectHandler(host='192.168.120.1', port='22', username='cisco', password='cisco', secret="!@3456Qwerty" device_type='cisco_ios')
# 호출할 개체를 만듬, ip 및 자격증명에 관한  장치 매개변수를 개체에 직접 정의

connection = ConnectHandler(**device1)
connection.enable()
#connection.config_mode() # Global config mode

show_commands = ['show int bri', 'show int desc', 'show run', 'show version']


#여러 명령어 전달하기 for loop 이용
for command in show_commands:  
    print(f'\n *** sending {command} ***\n')
    output = connection.send_command(command)
    print(output)
    with open('show_commands.txt','a+') as f:
        f.write(output)

###명령어 한개 전달---------------------##
#output = connection.send_command('show run')
# send_command를 이용한 스위치 명령어 보내기
#print(output)
##-------------------------------------##

print('Closing Connection')
connection.disconnect()
# disconnect를 이용한 ssh 세션 연결 끊기