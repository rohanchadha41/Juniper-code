from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree
from pprint import pprint

from getpass import getpass
import sys

#Device login with credentials

hostname = input("Hostname: ")
junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS password: ")

#Opening connection to the device via NETCONF over SSH

dev = Device(host=hostname ,user = junos_username,password = junos_password)
dev.open()

print("Login to device successful")

#Filtering only interfaces IRB configuration
with dev as f:
	filter = '<interfaces><interface><name>irb</name></interface></interfaces>'
	data = f.rpc.get_config(filter_xml=filter,options={'format':'set'})

#Printing the output of "show interfaces irb" to the file
	with open('leaf-juniper.txt','w') as g:
		g.write(etree.tostring(data,encoding='unicode', pretty_print=True))
		g.close()

#closing connection
dev.close()

#Opening the file saved above and making changes to filter for only statements with virtual-gateway configured

config_file = open('leaf-juniper.txt', "r")
list_irb = config_file.readlines()
final_irb_list=[]


for x in list_irb:
    if 'virtual-gateway-address' in x:
        final_irb_list.append(int(x.split(" ")[4]))
    else:
        pass

#Opening connection to device again
dev.open()

#Loading the config to the device and then committing it.
with Config(dev) as cu:
	for i in final_irb_list:
		i=str(i)
		#print(i)
		cu.load(f"set interfaces irb unit {i} no-auto-virtual-gateway-esi", format='set', merge= 'True')

	#cu.commit()

print("Changes have been made")

#Closing the connection to the device
dev.close()



print("Logged out")
                 #todo hide
