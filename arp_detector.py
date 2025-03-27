from scapy.all import sniff


IP_MAC_MAP = {}  # Словарь, содержащий сопоставления IP и MAC-адресов. 


def process_packet(packet):
    source_ip = packet['ARP'].psrc
    source_mac = packet['ether'].src
    if source_mac in IP_MAC_MAP.keys():
        if IP_MAC_MAP[source_mac] != source_ip:
            try:
                old_ip = IP_MAC_MAP[source_mac]
            except:
                old_ip = 'Unknown'
            return "Возможная атака посредника отравлением ARP-таблицы"
        else:
            IP_MAC_MAP[source_mac] = source_ip

# Возможная атака посредника отравлением ARP-таблицы.
sniff(count = 0, filter = 'ARP', store = 0, prn = process_packet)