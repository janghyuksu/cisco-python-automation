from netmiko import ConnectHandler

test = netmiko.ConnectHandler{
    device type = "cisco_ios",
    ip = "192.168.120.1",
    username = "cisco",
    password = "cisco",
    secret = "!@3456Qwerty"
}
test.enable()
output = test.send_command("show run")
print(output)
test.disconnect()

file = open('backup.txt','w')
file.write(output)
file.close