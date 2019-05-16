from cognionics_trigger import CognionicsTrigger

port_name = 'COM7'#get automatically

trigger = CognionicsTrigger(port_name, baudrate=57600)
send_trigger = trigger.send_trigger


if __name__ == "__main__":
    import sys
    import time
    for c in sys.argv[1]:
        send_trigger(c)
        time.sleep(1.)