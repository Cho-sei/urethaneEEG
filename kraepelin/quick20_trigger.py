from cognionics_trigger import CognionicsTrigger

with open("triggerbox_serialnumbers.txt", 'r') as f:
    serialnumber_list = f.readlines()

import serial.tools.list_ports
for portinfo in serial.tools.list_ports.comports():
    if portinfo.serial_number in serialnumber_list:#TODO:register serials for other quick-20
        trigger = CognionicsTrigger(portinfo.device, baudrate=57600)
        print(portinfo.serial_number, portinfo.device)
        break
else:
    raise RuntimeError("not found any receiver or trigger box")
send_trigger = trigger.send_trigger


if __name__ == "__main__":
    print(trigger.serial_port.name, trigger.serial_port.baudrate)
    import sys
    import time
    char = chr(int(sys.argv[1]))
    send_trigger(char)
    print(char)
    time.sleep(1.)