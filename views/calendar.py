import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime

# Sample event data (replace with your data source)
events = [
    {
        "id": 1,
        "title": "Group Run - Morning",
        "start": "2024-10-27T08:00:00",
        "end": "2024-10-27T09:00:00",
        "allDay": False,
        "description": "Easy 5k run in the park.",
    },
    {
        "id": 2,
        "title": "Group Run - Evening",
        "start": "2024-10-27T18:00:00",
        "end": "2024-10-27T19:00:00",
        "allDay": False,
        "description": "Speed workout at the track.",
    },
    {
        "id": 3,
        "title": "Social Event",
        "start": "2024-11-03",
        "end": "2024-11-04",
        "allDay": True,
        "description": "Post-race celebration at the local pub.",
    },
    {
        "id": 4,
        "title": "Long Run",
        "start": "2024-11-10T07:00:00",
        "end": "2024-11-10T10:00:00",
        "allDay": False,
        "description": "15 mile long run.",
    }
]

calendar_options = {
    "initialView": "dayGridMonth",
    "locale": "en",
    "editable": False,
    "selectable": True,
}

calendar_output = calendar(events, calendar_options)

if calendar_output and calendar_output.get("date"):
    selected_date_str = calendar_output["date"]
    selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d").date()

    st.write(f"### Events on {selected_date}:")
    events_on_date = [
        event
        for event in events
        if datetime.strptime(event["start"].split("T")[0], "%Y-%m-%d").date() == selected_date
        or (event.get("allDay") and datetime.strptime(event["start"], "%Y-%m-%d").date() <= selected_date and datetime.strptime(event["end"], "%Y-%m-%d").date() >= selected_date)
    ]

    if events_on_date:
        for event in events_on_date:
            st.write(f"- **{event['title']}**")
            if not event["allDay"]:
                st.write(f"  - Time: {event['start'].split('T')[1]} - {event['end'].split('T')[1]}")
            if "description" in event:
                st.write(f"  - Description: {event['description']}")
    else:
        st.write("No events on this day.")
elif calendar_output and calendar_output.get("start"): #if a date range is selected
    start_date = datetime.strptime(calendar_output["start"].split("T")[0], "%Y-%m-%d").date()
    end_date = datetime.strptime(calendar_output["end"].split("T")[0], "%Y-%m-%d").date()

    st.write(f"### Events between {start_date} and {end_date}:")
    events_in_range = [
        event
        for event in events
        if (datetime.strptime(event["start"].split("T")[0], "%Y-%m-%d").date() >= start_date and datetime.strptime(event["start"].split("T")[0], "%Y-%m-%d").date() <= end_date)
        or (event.get("allDay") and datetime.strptime(event["start"], "%Y-%m-%d").date() <= end_date and datetime.strptime(event["end"], "%Y-%m-%d").date() >= start_date)
    ]
    if events_in_range:
        for event in events_in_range:
            st.write(f"- **{event['title']}**")
            if not event["allDay"]:
                st.write(f"  - Time: {event['start'].split('T')[1]} - {event['end'].split('T')[1]}")
            if "description" in event:
                st.write(f"  - Description: {event['description']}")
    else:
        st.write("No events in this range.")