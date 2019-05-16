from cognionics_trigger import CognionicsTrigger

port_name = 'COM7'#get automatically

import serial.tools.list_ports
for portinfo in serial.tools.list_ports.comp:orts():
    if portinfo.serial_number == 'A1368SV7A':#TODO:register serials for other quick-20
        trigger = CognionicsTrigger(port_name, baudrate=57600)
else:
    raise RuntimeError("not find quick-20 (serial_number:A1368SV7A)")
send_trigger = trigger.send_trigger


if __name__ == "__main__":
    import sys
    import time
    for c in sys.argv[1]:
        send_trigger(c)
        time.sleep(1.)