# Network Scanner

This is a simple network scanner written in Python using the Scapy library. It allows users to scan their local network to discover devices connected to it.

## Requirements

To run this script, you need Python 3 and the Scapy library. You can install Scapy using pip:

Usage
Run the script from the command line, providing the IP address of the local network you want to scan. For example:

bash
pip3 install scapy
python3 network_scanner.py -i 192.168.1.1
If you do not provide an IP address, the script will prompt you to enter one.

How It Works
The script uses the ARP (Address Resolution Protocol) to find all devices on the network.
It creates an ARP request and a broadcast packet to request the MAC addresses of devices within the specified IP range.
The results are displayed, showing which devices responded to the ARP request.
Note
Make sure to run this script with proper permissions, as network scanning may require elevated privileges.
