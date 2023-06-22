from scapy.all import *
from scapy.layers.inet import IP, ICMP
# Ağ kartı arayüzü adı
iface = "eth0"

# Promiscuous modu test etmek için ping gönderimi yapılıyor
ping_pkt = IP(dst="8.8.8.8")/ICMP()
ans, unans = sr(ping_pkt, iface=iface, timeout=1, verbose=0, count=1)

# Promiscuous moddaysanız yanıt alırsınız, aksi takdirde yanıt alamazsınız
if len(ans) > 0:
    print(f"Ağ kartı arayüzü {iface} promiscuous modda çalışıyor.")
else:
    print(f"Ağ kartı arayüzü {iface} promiscuous modda çalışmıyor.")
