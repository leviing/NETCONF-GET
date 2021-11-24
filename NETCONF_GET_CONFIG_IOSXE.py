# import CSV, NETCONF, and XML modules
import getpass
import csv
from ncclient import manager
import xml.dom.minidom
import xmltodict


def main():

    # get the username and password from terminal
    username = input('Username: ')
    password = getpass.getpass('Password: ')

    # open the CSV with the network device addresses
    with open('Network_Devices.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        
        # loop through IP address in the CSV
        for network_device in reader:
            device = ', '.join(network_device)
            
            # print start message
            print('Connecting to ' + device + '...')
            
            # open an SSH session to the device using NETCONF
            with manager.connect(host=device, username=username, password=password, hostkey_verify=False, device_params={'name': 'iosxe'}, timeout=120) as netconf_connection:

                # get YANG running config and convert XML to dict
                config = netconf_connection.get_config('running')
                config_dict = xmltodict.parse(config.xml)['rpc-reply']['data']
                
                # format config into readable XML form using minidom
                pretty_config = xml.dom.minidom.parseString(config.xml).toprettyxml()
                
                # write XML to file with hostname from config_dict
                with open('XML_RUNNING_CONFIGS\\%s.xml' % config_dict['native']['hostname'], 'w') as f:
                    f.write(pretty_config)
                
                # print completeion message
                print(config_dict['native']['hostname'] + ".XML NETCONF running config saved in \XML_RUNNING_CONFIGS!")

if __name__ == '__main__':
    main()