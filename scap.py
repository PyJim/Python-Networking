from scapy.all import IP, ICMP, sr1
import os

target_ip = os.getenv('TARGET_IP')


# craft the ICMP packet
packet = IP(dst=target_ip) / ICMP()

# send the packet and receive the response
response = sr1(packet, timeout=2, verbose=False)

# check if a response was received

if response:
    print(f"Response received from {response.src}")
else:
    print(f"No response received")