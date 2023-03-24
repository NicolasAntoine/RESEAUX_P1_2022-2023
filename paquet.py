import pyshark
import time
capture = pyshark.FileCapture("Paquet WireShark screen share paquet 148.pcapng")
j = 0
for i in capture:
    print("packet n° " + str(j))
    j += 1
    i.pretty_print()
    time.sleep(1)
    print("---------")
    print(i[2].field_names)
    time.sleep(5)
    print("---------")