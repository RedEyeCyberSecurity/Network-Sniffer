from scapy.all import sniff


# Callback function for processing packets
def packet_callback(packet):
    print(packet.summary())


# Main Sniffer Logic
print("[+] Starting packet sniffer...")
sniff(prn=packet_callback, store=0)
