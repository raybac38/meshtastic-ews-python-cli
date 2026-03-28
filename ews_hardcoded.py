import ews_pb2

ews_msg : ews_pb2.Ews = ews_pb2.Ews();


## message type
ews_msg.messageIdentifier.messageType = ews_pb2.TEST;

## contry / region
ews_msg.messageIdentifier.region = ews_pb2.ANTARTICA;

## provider
ews_msg.messageIdentifier.providerIdentifier = ews_pb2.DUMMY_1;

## hazard category
ews_msg.hazard.hazardCategoryAndType = ews_pb2.MARINE_POLLUTION;

## hazard severity
ews_msg.hazard.severity = ews_pb2.SEVERITY_MODERATE;

## hazard week number
ews_msg.hazardChronology.weekNumber = ews_pb2.CURRENT_WEEK;

## hazard time of the week
ews_msg.hazardChronology.timeOfTheWeek = ews_pb2.MONDAY_00_02_AM;

## hazard duration
ews_msg.hazardChronology.duration = ews_pb2.MORE_THAN_12H_LESS_THAN_24H;

## guidance lib selection
ews_msg.guidanceToReact.librarySelection = ews_pb2.REGION_LIBRARY;

## guidance lib version
ews_msg.guidanceToReact.libraryVersion = ews_pb2.VERSION_2;

## guidance instruction
ews_msg.guidanceToReact.instructionsListA = ews_pb2.DANGER_EVAC;
ews_msg.guidanceToReact.instructionsListB = ews_pb2.CHECK_AUTHORITIES;

## eclipse center latitude
ews_msg.targetArea.ellipse = 64;

## eclipse center longitude

## eclipse semi major axis

## eclipse semi minor axis

## eclipse azimuth


## additional parametre not yet supported

## ask for confirmation before sending




### Sending payload

import meshtastic
import meshtastic.serial_interface
import portnums_pb2
import time

interface = meshtastic.serial_interface.SerialInterface("/dev/ttyUSB0")

payload = ews_msg.SerializeToString()

interface.sendData(
    payload,
    portNum=portnums_pb2.EWS
)

print(payload.hex())

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