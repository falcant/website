import streamlit as st
import datetime

def event_display():
    st.title("My Website Events")

    # Initialize events in session state (replace with your actual data source)
    if 'website_events' not in st.session_state:
        st.session_state.website_events = [
            {
                "name": "Community Meetup",
                "date": datetime.date(2024, 12, 10),
                "time": datetime.time(19, 0),
                "location": "Local Community Center",
                "description": "Join us for a casual meetup to discuss local topics.",
            },
            {
                "name": "Webinar: Streamlit Basics",
                "date": datetime.date(2024, 11, 25),
                "time": datetime.time(14, 30),
                "location": "Online",
                "description": "Learn the fundamentals of building web apps with Streamlit.",
            },
            {
                "name": "Holiday Charity Drive",
                "date": datetime.date(2024, 12, 20),
                "time": datetime.time(10, 0),
                "location": "Downtown Square",
                "description": "Help us collect donations for local families in need.",
            },

        ]

    # Display events
    if st.session_state.website_events:
        st.header("Upcoming Events")
        for event in sorted(st.session_state.website_events, key=lambda x: datetime.datetime.combine(x['date'], x['time'])): #sort events by time.
            with st.expander(f"{event['name']} - {event['date'].strftime('%Y-%m-%d')}"):
                st.write(f"**Time:** {event['time'].strftime('%I:%M %p')}")
                st.write(f"**Location:** {event['location']}")
                st.write(f"**Description:** {event['description']}")
    else:
        st.info("No events scheduled.")

if __name__ == "__main__":
    event_display()