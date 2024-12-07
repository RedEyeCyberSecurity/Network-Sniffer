# Network-Sniffer
Create a packet sniffer that monitors and captures network packets in real-time to analyze traffic.


🛠️ How It Works
Using libraries like scapy, this tool listens to network traffic, captures packets, and displays useful information about them.


```python
from scapy.all import sniff


# Callback function for processing packets
def packet_callback(packet):
    print(packet.summary())


# Main Sniffer Logic
print("[+] Starting packet sniffer...")
sniff(prn=packet_callback, store=0)
