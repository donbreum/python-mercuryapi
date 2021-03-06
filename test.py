#!/usr/bin/env python3
from __future__ import print_function
import time
import mercury
reader = mercury.Reader("tmr:///dev/ttyACM0", baudrate=115200)

print(reader.get_model())
print(reader.get_supported_regions())

reader.set_region("EU3")
reader.set_read_plan([1], "GEN2", read_power=1900)
print(reader.read())

reader.start_reading(lambda tag: print(tag.epc, tag.antenna, tag.read_count, tag.rssi, tag.phase))
time.sleep(5)
reader.stop_reading()