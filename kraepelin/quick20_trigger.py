from cognionics_trigger import CognionicsTrigger

import serial.tools.list_ports
for portinfo in serial.tools.list_ports.comports():
    if portinfo.serial_number == 'A1368SV7A':#TODO:register serials for other quick-20
        trigger = CognionicsTrigger(portinfo.device, baudrate=57600)
        print(portinfo.serial_number, portinfo.device)
        break
else:
    raise RuntimeError("not find quick-20 (serial_number:A1368SV7A)")
send_trigger = trigger.send_trigger


if __name__ == "__main__":
    print(trigger.serial_port.name, trigger.serial_port.baudrate)
    import sys
    import time
    char = chr(int(sys.argv[1]))
    send_trigger(char)
    print(char)
    time.sleep(1.)