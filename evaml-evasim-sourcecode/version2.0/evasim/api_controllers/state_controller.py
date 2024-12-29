from enum import Enum
from asyncio import Event

class Commands(str, Enum):
    MOTION = "Motion"
    TALK = "Talk"

current_command = {}

result_event = Event()

async def get_result():
    current_command.clear()
    await result_event.wait()
    result_event.clear()
    return current_command

def trigger_event():
    result_event.set()

def command_motion(attrib : str, detail : str):
    attrib = attrib.lower()
    command = {"command" : Commands.MOTION.value}
    if attrib == "left-arm":
        command["left-arm"] = detail

    if attrib == "right-arm":
        command["right-arm"] = detail

    if attrib == "head":
        command["head"] = detail
    else:
        if attrib == "type":
            command["type"] = detail

    current_command.update(command)

def command_talk(text : str):
    command = {"command" : Commands.TALK.value}
    command["text"] = text
    current_command.update(command)