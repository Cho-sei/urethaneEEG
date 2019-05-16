import serial
import threading
import time

class CognionicsTrigger:
    def __init__(self, port_name, baudrate=57600, **serial_keyargs):
        self.serial_port = serial.Serial(port_name, baudrate, **serial_keyargs)

    def send_trigger(self, char):
        """send a binary to port as a trigger.
        Another thread is used avoiding blocking main experiment.
        """
        assert len(char) == 1, "cognionics usb can send only 1 byte."
        serialport_lock = threading.Lock()
        trigger_onset = threading.Thread(
            target=self._threadsafe_trigger, args=(self.serial_port, char.encode(), serialport_lock)
        )
        trigger_reset = threading.Timer(
            .01, self._threadsafe_trigger, args=(self.serial_port, b'\0', serialport_lock)
        )
        trigger_onset.start()
        trigger_reset.start()

    @staticmethod
    def _threadsafe_trigger(serialport, binary, lock, **serial_keyargs):
        with lock:
            written_byte = serialport.write(binary, **serial_keyargs)
            time.sleep(.01)
        return written_byte#no meaning

if __name__ == "__main__":
    import sys
    port_name = sys.argv[1]
    string = sys.argv[2]

    trigger = CognionicsTrigger(port_name)
    for char in string:
        print("order of '{}' is {}".format(char, ord(char)))
        trigger.send_trigger(char)