import pyshark
import time
capture = pyshark.FileCapture("Paquet WireShark screen share paquet 148.pcapng",display_filter="")
j = 1
for i in capture:
    i.pretty_print()
    if j == 34:
         print(i.tcp.field_names)
         time.sleep(20)
    print("packet n° " + str(j))
    j += 1