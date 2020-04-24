import netmiko

"""connect single device option 1"""
net_connect1 = netmiko.ConnectHandler(device_type='cisco_ios', host='192.168.1.1', username='cisco', password='cisco')
print(net_connect1.find_prompt())

"""connect single device option 2"""
device = {
    'device_type':'cisco_ios',
    'host':'192.168.1.1',
    'username':'cisco',
    'password':'cisco',
}

net_connect2 = netmiko.ConnectHandler(**device)
print(net_connect2.find_prompt())
