import meshtastic
import meshtastic.serial_interface
import time

import questionary



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