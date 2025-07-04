import sys, struct, datetime

countProt = {}
protoNames = {
    0x0800: "IPv4", 
    0x0806: "ARP", 
    0x0809: "RARP",
    0x86dd: "IPv6",
    0x88CC: "LLDP",
    0x9001: "3COM - Brigde",
}
 
if len(sys.argv) < 2:
    print (f"uso: {sys.argv[0]} arquivo.pcap")
    sys.exit(1)

fd = open (sys.argv[1], "rb")
fd.seek (24, 0)

hPacket = fd.read(16)
while len(hPacket) == 16:
    ts, ms, lenCap, lenPacket = struct.unpack ("<IIII", hPacket)
    fd.seek(12, 1)
    proto = int.from_bytes(fd.read(2), 'big')
    countProt[proto] = countProt.get(proto, 0) + 1
    fd.seek(lenCap-14, 1)
    hPacket = fd.read(16)
fd.close()

for key in countProt:
    print (protoNames.get(key, f"Não identificado ({hex(key)})"), ":", countProt[key])
