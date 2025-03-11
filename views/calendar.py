import streamlit as st
import calendar
from datetime import date

# Sample event data (replace with your data source)
event_data = {
    date(2025, 3, 26): ["Meeting with team", "Project deadline"],
    date(2024, 10, 28): ["Client presentation"],
    date(2024, 11, 5): ["Team lunch"],
    date(2024, 11, 15): ["Holiday"]
}

def calendar_app(event_data):
    """
    An interactive Streamlit app with a clickable calendar and event display,
    showing the number of events on each day, with aligned days of the week.
    """

    st.title("Interactive Calendar")

    today = date.today()
    current_year = today.year
    current_month = today.month

    year = st.number_input("Year", min_value=1900, max_value=2100, value=current_year)
    month = st.number_input("Month", min_value=1, max_value=12, value=current_month)

    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    st.write(f"### {month_name} {year}")

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    cols = st.columns(7)  # Create 7 columns for days of the week

    # Display days of the week headers
    for i, day_name in enumerate(days):
        with cols[i]:
            st.write(day_name)

    selected_date = None

    for week in cal:
        cols = st.columns(7)  # Create 7 columns for each week
        for i, day in enumerate(week):
            with cols[i]:
                if day == 0:
                    st.write(" ")
                else:
                    day_date = date(year, month, day)
                    num_events = len(event_data.get(day_date, []))
                    if num_events > 0:
                        button_text = f"{day}"
        
                    else:
                        button_text = str(day)

                    if st.button(button_text, key=f"{year}-{month}-{day}"):
                        selected_date = day_date

    if selected_date:
        st.write(f"### Events for {selected_date.strftime('%Y-%m-%d')}:")
        if selected_date in event_data:
            for event in event_data[selected_date]:
                st.write(f"- {event}")
        else:
            st.write("No events for this day.")

#if __name__ == "__main__":
calendar_app(event_data)