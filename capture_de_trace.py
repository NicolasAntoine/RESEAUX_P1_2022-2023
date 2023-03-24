import pyshark
try:
    capture = pyshark.LiveCapture(interface="Wi-Fi", output_file="pyshark.pcap")
    capture.sniff()
except KeyboardInterrupt:
    print(capture)
