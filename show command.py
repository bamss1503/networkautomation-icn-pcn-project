import netmiko

R1 = {
    'device_type':'cisco_ios',
    'host':'192.168.1.1',
    'username':'cisco',
    'password':'cisco',
    'secret':'class'
}
R2 = {
    'device_type':'cisco_ios',
    'host':'192.168.0.5',
    'username':'cisco',
    'password':'cisco',
    'secret':'class'
}
R3 = {
    'device_type':'cisco_ios',
    'host':'192.168.0.9',
    'username':'cisco',
    'password':'cisco',
    'secret':'class'
}
R4 = {
    'device_type':'cisco_ios',
    'host':'192.168.0.13',
    'username':'cisco',
    'password':'cisco',
    'secret':'class'
}
R5 = {
    'device_type':'cisco_ios',
    'host':'192.168.0.17',
    'username':'cisco',
    'password':'cisco',
    'secret':'class'
}
R6 = {
    'device_type':'cisco_ios',
    'host':'192.168.0.21',
    'username':'cisco',
    'password':'cisco',
    'secret':'class'
}

all_device = [R1, R2, R3, R4, R5, R6]

for device in all_device:
    net_connect = netmiko.ConnectHandler(**device)
    #enter into privillage mode
    net_connect.enable()
    #display interface ip address and status for all route
    print(net_connect.send_command("show ip int br"))
