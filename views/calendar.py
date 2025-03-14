import streamlit as st
import calendar
from datetime import date
import datetime

#March Events


# Sample event data (replace with your data source)
#event_data = {
#    date(2025, 3, 22): ["🎉🎉WTC 2 Year Anniversary Hike!!🎉🎉","🎉🎉WTC 2 Year Anniversary Party!!🎉🎉"],
#    date(2024, 3, 22): ["Client presentation"],
#    date(2024, 11, 5): ["Team lunch"],
#    date(2024, 11, 15): ["Holiday"]
#}

event_data = {
    date(2025, 3, 22): [("🎉🎉WTC - 2 year anniversary run/hike 🎉🎉","Come join us for a short  2 mile run/hike to celebrate the 2 year anniversary 🥳!!","https://maps.app.goo.gl/omPVnJBPcqKRCc937?g_st=com.google.maps.preview.copy"),
                        ("🎉🎉WTC 2 Year Anniversary Party!!🎉🎉","Come Dance💃🕺, Sing 🎤🎶, Hang Out🎉, this party is FOR YOU!!","https://maps.app.goo.gl/owzqrdq7NgzcbG2Q8")]
}

def calendar_app(event_data):
    """
    An interactive Streamlit app with a clickable calendar and event display,
    showing the number of events on each day, with aligned days of the week.
    """

    #st.title("EVENTS")

    selected_date = st.date_input("Please Choose a Date", 'today')
    #st.write("Your birthday is:", d)
    #selected_date = None


    if selected_date:
        st.write(f"### Events for {selected_date.strftime('%Y-%m-%d')}:")
        if selected_date in event_data:
            #for event in event_data[selected_date]:
                #st.write(f""" {event} """)
                #st.write(" - click here for details")
            #for (event_title, event_details) in event_data.items():
            for date_key in event_data[selected_date]:
                event_title,event_detail,event_location = date_key

                st.write(f""" {event_title} """)
                st.write(f""" 
                         - {event_detail}
                         - Location: [here]({event_location}) 
                         """)
                #st.write(f""" Location: {event_location}""")

        else:
            st.write("No events for this day.")

#if __name__ == "__main__":

st.image("./assets/combined_logo.png", width=300)
st.header("EVENTS")
st.write("""
     🎉 Our calendar of events is packed with exciting runs 🏃‍♀️🏃‍♂️, social gatherings 🥳, 
         and training opportunities 💪 designed to keep you motivated and connected. 
         From scenic trail runs 🏞️ to invigorating group workouts 🏋️‍♀️, there's something for everyone. 
         Take a moment to browse the calendar 🗓️ and discover your next running adventure 🗺️
         . It's the best way to stay informed 📣, plan your week 📝, 
         and join us in building a stronger, healthier community 💗!!
""")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:

    calendar_app(event_data)
with col2:
    st.image("./assets/wtc_twinpeaks.jpg", width=300)