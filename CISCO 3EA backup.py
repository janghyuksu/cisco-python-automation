## 장비 백업  3대 기준 텍스트->host명

from netmiko import ConnectHandler

device1 = { 
    'device_type': 'cisco_ios', 
    'ip': '192.168.1.100', 
    'username': 'cisco', 
    'password': 'cisco',
    'secret': 'cisco'
}
device2 = { 
    'device_type': 'cisco_ios', 
    'ip': '192.168.1.101', 
    'username': 'admin', 
    'password': 'cisco',
    'secret': 'cisco'
}
device3 = { 
    'device_type': 'cisco_ios', 
    'ip': '192.168.1.102', 
    'username': 'cisco', 
    'password': 'cisco',
    'secret': 'cisco'
}
net_connect1 = ConnectHandler(**device1)
net_connect1.enable()
net_connect2 = ConnectHandler(**device2)
net_connect2.enable()
net_connect3 = ConnectHandler(**device3)
net_connect3.enable()

output1 = net_connect1.send_command('show run')
output1 = output1.splitlines()

hostname1 = ''
for line in output1:
    if 'hostname' in line:
        line = line.split()
        hostname1 = line[1]

output1 = hostname1 + '#show ip int b\n' + net_connect1.send_command('show ip int b') + '\n'
output1 += hostname1 + '#show run\n' + net_connect1.send_command('show run') + '\n'
print(output1)

output2 = net_connect2.send_command('show run')
output2 = output2.splitlines()

hostname2 = ''
for line in output2:
    if 'hostname' in line:
        line = line.split()
        hostname2 = line[1]

output2 = hostname2 + '#show ip int b\n' + net_connect2.send_command('show ip int b') + '\n'
output2 += hostname2 + '#show run\n' + net_connect2.send_command('show run') + '\n'
print(output2)

output3 = net_connect3.send_command('show run')
output3 = output3.splitlines()

hostname3 = ''
for line in output3:
    if 'hostname' in line:
        line = line.split()
        hostname3 = line[1]

output3 = hostname3 + '#show ip int b\n' + net_connect3.send_command('show ip int b') + '\n'
output3 += hostname3 + '#show run\n' + net_connect3.send_command('show run') + '\n'
print(output3)

file = open('C:/Users/장혁수/Desktop/' + hostname1 +'.txt', 'a', encoding = 'utf-8')
file.write(output1)
file.close

file = open('C:/Users/장혁수/Desktop/' + hostname2 +'.txt', 'a', encoding = 'utf-8')
file.write(output2)
file.close

file = open('C:/Users/장혁수/Desktop/' + hostname3 +'.txt', 'a', encoding = 'utf-8')
file.write(output3)
file.close

#interface_output = interface_output.splitlines()
#print(net_connect.find_prompt())
#net_connect.disconnect()
