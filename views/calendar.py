import streamlit as st
import pandas as pd
import pydeck as pdk

# Sample event data with coordinates and descriptions
event_data = pd.DataFrame(
    {
        "event_name": ["Group Run", "Social Event", "Track Workout"],
        "latitude": [34.0522, 40.7128, 37.7749],
        "longitude": [-118.2437, -74.0060, -122.4194],
        "description": [
            "Easy 5k group run in the park.",
            "Post-race celebration at the pub.",
            "Speed workout at the local track.",
        ],
    }
)

st.title("Interactive Event Map")

# Pydeck layer for event markers
layer = pdk.Layer(
    "ScatterplotLayer",
    data=event_data,
    get_position=["longitude", "latitude"],
    get_radius=1000,  # Radius in meters
    get_color=[255, 140, 0],  # Orange color
    pickable=True,  # Make markers interactive
)

# Pydeck view
view_state = pdk.ViewState(
    latitude=event_data["latitude"].mean(),
    longitude=event_data["longitude"].mean(),
    zoom=4,
    pitch=0,
)

# Pydeck tooltip
tooltip = {
    "html": "<b>{event_name}</b><br>{description}",
    "style": {
        "backgroundColor": "white",
        "color": "black",
    },
}

# Render the map
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip))

# Display event details based on selection (optional)
st.subheader("Event Details")
if st.session_state.get("deck_click_event"):
    clicked_event = st.session_state["deck_click_event"]["object"]
    if clicked_event:
        st.write(f"**{clicked_event['event_name']}**")
        st.write(f"Description: {clicked_event['description']}")
        st.write(f"Latitude: {clicked_event['latitude']}")
        st.write(f"Longitude: {clicked_event['longitude']}")
else:
    st.write("Click on a marker to see event details.")

# Add a callback to store clicked event data in session state
def update_click_event(event):
    st.session_state["deck_click_event"] = event

# Register the callback with st.pydeck_chart
if "deck_click_event" not in st.session_state:
    st.session_state["deck_click_event"] = None

st.pydeck_chart(
    pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip),
    on_click=update_click_event,
)