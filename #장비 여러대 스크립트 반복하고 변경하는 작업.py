#장비 여러대 스크립트 반복하고 변경하는 작업

from netmiko import ConnectHandler

with open('commands_file') as f:   #파일의 명령을 읽은 다음 그명령을 수행 with을 사용시 파일을 닫을 필요가 없음 , open 된 명령파일을 사용하면 commands 파일을 만듬
    commands_to_send = f.read().splitlines() #스크립트는 command파일을 읽고 command파일의 한줄씩 분할 함

cisco_interface = { 
    'device_type': 'cisco_ios', 
    'ip': '192.168.1.100', 
    'username': 'cisco', 
    'password': 'cisco',
    'secret': 'cisco'
}

all_interface = [cisco_interface]  #장치 여러대 연결 script

for interface in all_interface:   #장치 여러대 연결 script      해석->all_interface의 각 항목에 interface에 대하여
net_connect = ConnectHandler(**cisco_interface) #connecthandler를 사용하여 스위치에 연결하는 변수를 연결함 
output = net_connect.send.command('show run') #show run 의 명령의 결과는 출력 변수에 저장 됨
print(output) #출력 인쇄


''''''
# cisco_interface 대신 여러대를 사용

from getpass import getpass
from netmiko import ConnectHandler

username = raw_input('Enter your SSH username: ' )
password = getpass

with open('commands_file') as f:
    commands_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

for interface in all_interface:
    print 'Connecting to device" ' + devices_list
    ip_address_of_device = devices
    ios_device = {
    'device_type': 'cisco_ios', 
    'ip': '192.168.1.100', 
    'username': 'cisco', 
    'password': 'cisco',
    'secret': 'cisco'
    }

net_connect = ConnectHandler(**cisco_interface) 
output = net_connect.send.command('show run') 
print(output) 




#예외처리
try:
    net_connect = ConnectHandler(**장비명)
    except



