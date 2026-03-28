import meshtastic
import meshtastic.serial_interface
import time

message = "message send to port 384"

interface = meshtastic.serial_interface.SerialInterface("/dev/ttyACM0")

interface.sendText(message, portNum=384)

print(f"Message envoyé sur le port 384 : {message}")

## delay
time.sleep(1)

interface.close()
