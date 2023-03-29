import netmiko import ConnectHandler

test = netmiko.ConnectHandler{
    device type = "cisco_ios",
    ip = "192.168.1.100",
    username = "cisco",
    password = "cisco",
    secret = "cisco"
}
test.enable()
output = test.send_command("show run")
print(output)
test.disconnect()

file = open('backup.txt','w')
file.write(output)
file.close