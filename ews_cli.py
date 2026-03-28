import ews_pb2

import questionary

ews_msg : ews_pb2.Ews = ews_pb2.Ews();


## message type

## contry / region

## provider

## hazard category

## hazard severity

## hazard week number

## hazard time of the week

## hazard duration

## guidance lib selection

## guidance lib version

## guidance instruction

## eclipse center latitude

## eclipse center longitude

## eclipse semi major axis

## eclipse semi minor axis

## eclipse azimuth

## additional parametre not yet supported

## ask for confirmation before sending




### Sending payload

import meshtastic
import meshtastic.serial_interface
import time

interface = meshtastic.serial_interface.SerialInterface("/dev/ttyACM0")

payload = ews_msg.SerializeToString()

interface.sendText(payload, portNum=384)

print(f"Ews message send")

## delay
time.sleep(1)

interface.close()




## exemple d'utilisation de questionary
'''
questionary.text("What's your first name").ask()
questionary.password("What's your secret?").ask()
questionary.confirm("Are you amazed?").ask()


questionary.select(
    "What do you want to do?",
    choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
).ask()

questionary.rawselect(
    "What do you want to do?",
    choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
).ask()

questionary.checkbox(
    "Select toppings", choices=["foo", "bar", "bazz"]
).ask()

questionary.path("Path to the projects version file").ask()
'''