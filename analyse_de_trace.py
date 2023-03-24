import pyshark
import time
capture = pyshark.FileCapture("visiocall_discord_wifi_eduroam.pcapng",display_filter="tcp")
j = 1
for i in capture:
    i.pretty_print()
    time.sleep(20)
    print("packet n° " + str(j))
    j += 1