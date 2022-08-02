# perfectly working script for pre and post checks by feeding list of commands to list of devices and write output to file
# HOW TO ADD DEVICE NAME TO THE OUTPUTFILE ?

import sys
import getpass
import os
import datetime
from netmiko import ConnectHandler

runday = datetime.datetime.now()

#outputfile = "pre-checks-" + runday.strftime("%A")+ "-" + runday.strftime("%d") + "-" + runday.strftime("%B") + "-" + runday.strftime("%Y") + ".txt"
outputfile = "pre-checks-" + runday.strftime("%Y_%m_%d-%I_%M_%S_%p")

device_list = [
"192.168.1.223",
"192.168.1.134",
]

command_list = [
"sh version",
"sh ip route",
"sh ip int brief",
]

user = input("Username: ")
password = getpass.getpass()

fW = open('outputs/' + outputfile, "w")

for devices in device_list:
    device = {
        'device_type': "cisco_ios",
        'ip': devices,
        'username': user,
        #'username': 'cisco',
        'password': password,
        'port': 22,
        'verbose': False,
    }
    deviceID = "Device: -----------------> " + devices
    fW.write("\n\n\n\n******************************************\n")
    fW.write(deviceID)
    fW.write("\n****************************************\n")
    print(devices)
#    command_list.clear()
    #Create the connection to the device
    connect_router = ConnectHandler(**device)


    for cmds in command_list:
        try:
            fW.write("\n\n=========================\n")
            fW.write(cmds)
            fW.write("\n=========================\n")
            output0 = connect_router.send_command(cmds)
            fW.write(output0)
            print(output0)
        except Exception as e:
            print(e)
    connect_router.disconnect()

fW.close
