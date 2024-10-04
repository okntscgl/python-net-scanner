import scapy.all as scapy

# 1) arp request (like netdiscover)
# 2) broadcast
# 3) response
# scapy.ls(.....) ->To run the help command, type the following, and then you can see the parameters you want to learn: 

arp_request_packet = scapy.ARP(pdst="10.0.2.0/24")
#scapy.ls(scapy.ARP())
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#scapy.ls(scapy.Ether())
combined_packet = broadcast_packet/arp_request_packet
result = scapy.srp(combined_packet, timeout=1)
print(result)
