#!usr/bin/python
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its mac address")
    parser.add_option("-m","--mac-addr",dest="mac_addr",help="New Mac address for Interface")
    (options , arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify the Interface, use '-h' or '--help' for more info")
    elif not options.mac_addr:
        parser.error("[-] Please specify the Mac Address, use '-h' or '--help' for more info")
    return options

def change_mac(interface , mac_addr):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_addr])
    subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig",options.interface]))
    mac_address_search_results = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if mac_address_search_results:
        return mac_address_search_results.group(0)
    else:
        print("[-] Could not find Mac Address")

options = get_arguments()

try:
    current_mac = get_current_mac(options.interface)
    print("Old Mac Address = ",current_mac)
except:
    pass

change_mac(options.interface,options.mac_addr)

try:
    current_mac = get_current_mac(options.interface)
    if current_mac == options.mac_addr:
        print("New Mac Address = ",current_mac)
    else:
        print("[-] Mac Address Not Changed")
except:
    print("Invalid Interface")