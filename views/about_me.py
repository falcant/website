import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/wtc_circle.png", width=300)

with col2:
    st.title("Wasatch Trails Collective", anchor=False)
    st.write(
        "A group for runners of color in the Salt Lake Area. ⛰️Eastern Shoshone, Goshute, and Núu-agha-tʉvʉ-pʉ̱ (Ute) Lands" )
    st.write("Se habla Español.") 
    #st.write(" ⛰️Eastern Shoshone, Goshute, and Núu-agha-tʉvʉ-pʉ̱ (Ute) Lands")

# --- ABOUT US ---
st.write("\n")
st.subheader("About the WTC", anchor=False)
st.write(
    """
    'About us' content
    """
)

# --- Mission Statement ---
st.write("\n")
st.subheader("WTC Mission Statement", anchor=False)
st.write(
    """
    'Mission Statement' Content
    """
)