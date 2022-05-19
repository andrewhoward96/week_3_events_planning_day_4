from models.event import *

event1 = Event("20th may", "andys birthday",3,"bloc","splashing",True)
event2 = Event("22nd september", "johnny birthday", 20, "butterfly","smashing",False)
events = [event1, event2]

def add_new_event(event):
    events.append(event)