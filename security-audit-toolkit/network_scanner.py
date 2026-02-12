# src/network_scanner.py
from scapy.all import ARP, Ether, srp

def scan(ip_range):
    print(f"[*] Iniciando escaneo en: {ip_range}")
    # Creando paquete ARP para descubrir hosts
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=False)[0]

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in clients:
        print(f"{client['ip']}\t\t{client['mac']}")

if __name__ == "__main__":
    scan("192.168.1.1/24")