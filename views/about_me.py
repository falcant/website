import streamlit as st
# library to rotate the image
from PIL import Image, ImageOps
# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/wtc_circle.PNG", width=300)

with col2:
    st.title("Wasatch Trails Collective", anchor=False)
    st.write(
        """... creating an inclusive & supportive community for runners of color along the Wasatch Front.""")
          
    st.write("⛰️Eastern Shoshone, Goshute, and Núu-agha-tʉvʉ-pʉ̱ (Ute) Lands. Se habla Español.") 
    #st.write(" ⛰️Eastern Shoshone, Goshute, and Núu-agha-tʉvʉ-pʉ̱ (Ute) Lands")

#-- History of the Wastach Trails Collective
st.write("\n")

st.subheader("How it Started:", anchor=False)
st.write("""
        With the mountains and trails so close, 
trail Running in the Salt Lake valley should be easy.
But for People of color, concerns about encountering
racism, affording the gear and lack of resources
complicate this experience and limit our access.

        """)
# -- next centered paragraph
col1, col2,col3 = st.columns(3, gap="small", vertical_alignment="center")
with col1:
    st.write(' ')
with col2:
    st.write("""Maybe Joining a local running group will help,
    but even that can be intimidating. "*Will I be the only
    person of color? Will there be runners who regularly
    make racist jokes? Who leads the group? Is everyone
    dedicated to fostering a welcoming environment?*"
             """)
with col3:
    st.write(' ')

st.write(" \n ")
col1,col2 = st.columns((1,1))
with col1:

    st.write("""
    Recognizing the need for change, Siani reached out to Chanh about starting a group for runners of color. Al great Things need a name, so we
    turned to CHATGPT to generate some options for us. Then Siani reached out to the handful of runners of color she knew, asking the what name they liked and if would like
    to help lead this group. Cristina, Sandra and Cindy were immediately on board.
    
             
    Over Warm bowls of pho, we discussed our dreams for this group.
    We wanted to create a welcoming enviroment for runners
    of all backgrounds, provide gear assistance, offer bilingual
    English and Spanish support, and implement a no-drop
    policy to ensure that on one feels like a burden or
    unwelcomed. """)

with col2:
    st.write("""\n """)
    st.write("\n")
    st.image("./assets/reference_image.jpg",caption="Reference Image for logo (Wasatch Front)")


col1,col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.write("""\n """)
    st.write("\n")
    st.image("./assets/wtc_firstmeeting.jpg",caption = "First WTC Meeting - March 2023")

with col2:
    st.write("""
    In addition to our core running activities, the Wasatch Trails Collective has broadened its scope
    , now encompassing a variety of interests
    . We've expanded into skiing, hiking, and even a book club, among other activities.
    
             
    The WTC experience is uniquely personal. For some, it's a dedicated running group for runners of color
    , providing a supportive and inclusive space. For others, it's a vibrant social community where shared
     meals like tacos, boba
    , and hotpot are enjoyed alongside optional runs.
""")
# --- ABOUT US ---

st.write("\n")
st.subheader("Who Are We?:", anchor=False)
st.write(
    """
    The WTC is a vibrant hub for people of color seeking both athletic and social connection. 
    We're more than just a multi-sport collective
    , offering activities from hiking and skiing to running and cycling; we're also a vital support system.
      Recognizing the unique challenges faced by underrepresented individuals,
        we provide a safe and inclusive space for members to build camaraderie,
     share experiences, and access resources. Whether it's conquering a challenging trail or navigating everyday life, 
     we're committed to empowering our members to thrive
    , fostering a sense of belonging and collective strength

    """
)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")


with col1:
    image = Image.open("./assets/wtc_firstgearswap.jpg")
    image = ImageOps.exif_transpose(image)
    st.image(image,caption="WTC Gear Swap")
with col2:
    st.image("./assets/wtc_firsthalfmarathon.jpeg",caption="SLC Half Marathon 2024")

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