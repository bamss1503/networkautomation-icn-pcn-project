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
ip = ["192.168.10.1", "192.168.20.1", "192.168.30.1", "192.168.40.1", "192.168.50.1", "192.168.60.1"]

for device in all_device:
    net_connect = netmiko.ConnectHandler(**device)

    net_connect.enable()#enter into privillage mode

# add ip address to interface
    ip_add = "ip address "+ip[0]+" 255.255.255.0"
    config_ip = ["int g0/3", ip_add]
    net_connect.send_config_set(config_ip)
    print(net_connect.send_command("show run | include hostname")+" add ip complete")
    ip.pop(0)

# change hostname all device
    hostname = net_connect.show_command("show run | include hostname")+"s"
    net_connect.send_config_set(hostname)
