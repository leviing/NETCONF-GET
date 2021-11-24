# NETCONF-GET RUNNING-CONFIG
This Python script will pull the YANG running config from a device(s) listed in a .csv using NETCONF and output a running config in XML. 

The scripts starts by prompting the user to provide a username and password. The username and password variables are in the main function but above the loop so they are used for every network device in the Network_Devices.csv. 

Devices in the .csv file can be listed as IP addresses or hostnames if the network supports. 

NCCLIENT is used to setup the NETCONF session to the device with the Cisco specific IOSXE device parameters. 

The NCCLIENT get_config pulls the YANG running config in XML. 

MINIDOM is used to format the XML into a more readable form when writing the config to a file in the .\XML_RUNNING_CONFIGS\ folder.

\XML_RUNNING_CONFIGS\ needs to be created in the same directory the script is located.

XMLTODICT is used to convert the XML running config into a dictionary object to easily parse the hostname from the config and apply the hostname as the file name written to the output directory.
