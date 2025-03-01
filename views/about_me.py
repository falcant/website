import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/wtc_circle.png", width=300)

with col2:
    st.title("Wasatch Trails Collective", anchor=False)
    st.write(
        """... creating an inclusive & supportive community for runners of color along the Wasatch Front.""")
          
    st.write("⛰️Eastern Shoshone, Goshute, and Núu-agha-tʉvʉ-pʉ̱ (Ute) Lands. Se habla Español.") 
    #st.write(" ⛰️Eastern Shoshone, Goshute, and Núu-agha-tʉvʉ-pʉ̱ (Ute) Lands")

# --- ABOUT US ---

st.write("\n")
st.subheader("Who Are We?:", anchor=False)
st.write(
    """
    We are a trail-focused running group created by and for runners of color in the Salt Lake Area.

    """
)

# --- Mission Statement ---
st.write("\n")
st.subheader("WTC Mission Statement", anchor=False)
st.write(
    """
    Our mission is to create an inclusive & supportive community for runners of color along the Wasatch Front.
      We strive to provide a space that empowers runners of all levels to achieve their personal goals, 
      improve diversity & equity in the broader running community, 
      and reduce the barriers that limit the participation & representation of people of color in endurance sports. 

    """
)

#st.image("./assets/wtc_firstmeeting.jpg",width=400,caption="(WTC First Event - March 18th 2023)")
#st.image("./assets/wtc_firstmeeting.jpg",width=400,caption="(WTC First Event - March 18th 2023)")
#--- Photo Section------
col1, col2,col3 = st.columns(3, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/wtc_firstmeeting.jpg")
with col2:
    st.image("./assets/wtc_firstgearswap.JPG")
with col3:
    st.image("./assets/wtc_firsthalfmarathon.jpeg")