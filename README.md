# Network Scanner

This project is a simple **network scanner** written in Python using the **Scapy** library.  
It scans a local network to discover active devices by sending ARP requests and collecting responses.

The purpose of this project is to demonstrate how basic network discovery works at the protocol level.

> ⚠️ **Legal & Ethical Notice**  
> This tool is intended **only for educational purposes, lab environments, or networks you own or are authorized to test**.  
> Scanning networks without permission may be illegal.

---

## Features

- Discover devices on a local network
- Uses ARP requests for fast and reliable detection
- Displays IP and MAC addresses of active hosts
- Simple command-line interface

---

## Requirements

- Python 3.x
- Scapy

---

## Installation

Install the required dependency using pip:

```bash
pip3 install scapy
Usage
Run the script from the command line and specify the target network IP or IP range:

bash
python3 network_scanner.py -i 192.168.1.1
If no IP address is provided, the script will prompt you to enter one interactively.

Note: You may need to run the script with administrator/root privileges to send and receive ARP packets.

How It Works
The script creates an ARP request targeting the specified IP address or range.

The ARP request is sent as a broadcast packet on the local network.

Devices that receive the request respond with their MAC addresses.

The script collects and displays the responses, showing active devices on the network.

This approach is commonly used in network discovery and penetration testing tools.

Example Output
The scan results typically include:

IP Address

MAC Address

This helps identify which devices are currently active on the local network.

Project Structure
graphql
Kodu kopyala
.
├── network_scanner.py   # ARP-based network scanning script
├── README.md            # Project documentation
Security Notes
ARP-based scanning works only within the local network segment and does not cross routers.
In real environments, network administrators mitigate such scans using:

Network segmentation

ARP inspection

Monitoring unusual ARP traffic

Understanding these techniques is essential for both offensive and defensive security.

License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it for educational and ethical purposes.
