from flask import render_template, request
from app import app
from models.events_list import add_new_event, events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name_event']
    event_guests = request.form['num_of_guests']
    event_room = request.form['room']
    event_description = request.form['description']
    event_recurring = request.form['recurring']
    new_event = Event(event_date,event_name,event_guests,event_room,event_description, event_recurring)
    print(new_event)
    add_new_event(new_event)

    return render_template('index.html', events=events)