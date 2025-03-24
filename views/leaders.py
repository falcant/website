import streamlit as st
from PIL import Image, ImageOps

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:

    st.image("./assets/combined_logo.png",output_format = "PNG")
with col2:
    st.write('')
st.title("Leadership Crew 🌟", anchor=False)
st.write("""To us leaders, it's the supportive and welcoming group
         that we wished existed when we started (trail) running, skiing, or any other outdoor activity.
         We are greatly humbled by the support and love we have received so far and can't wait to what's to come!!""")

st.header("Get to know us! ☺💖", anchor=False)


#-----Leader---------------
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.header("Mimi (Pronouns)", anchor=False)
    st.write(""" 
             - Why I run?:
             - Go-to running trail:
             - When I'm not running, you can find me:
             
             - Go to food/snack order:
        """)

with col2:
    #st.header("(Insert Photo Here)", anchor=False)
    st.image("./assets/mimi_wtc.png",output_format = "PNG")


#-------Leader ----------------------

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.subheader("Hector (He/Him)", anchor=False)
    st.write(""" 
             - **Why I run?**: I love to run because it helps me get out there and explore. 
               Running outdoors in the mountains is my favorite thing to do
             , there’s nothing like that sense of wonder I get every time I explore new places/trails.
             - **Go-to running trail**: I like to connect White Pine lake and Red Pine Lake in Little Cottonwood Canyon
             , I never get tired of the amazing views you get along the way. 
             - **When I'm not running, you can find me**: Sketching or journaling at local coffee shops. 
             - **Go to food/snack order**: I’m a big Coffee fan, nothing like an Oatmilk latte with two expresso shots to get the day started.
        """)

with col2:
    
   
    #st.header("(Insert Photo Here)", anchor=False)
    st.image("./assets/hector_wtc.png", output_format = "PNG")


#-------Leader ----------------------

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.header("Louise (She/Her/Ella)", anchor=False)
    st.write(""" 
             - **Why I run?**: At first, I started running solely for my mental health. I needed something that I didn't have to think too much about but would allow me to move freely. It soon became something that was freeing and a personal meditation. It has been a roller coaster with developing asthma as an adult and severe knee pain. However, slowly but surely, I have been able to improve both my physical and mental health with running. 
               It has become an important part of my life that motivates me to take care of myself and be a part of a welcoming community. 
             - **Go-to running trail**: You can find me at Liberty Park or City Creek trail!
             - **When I'm not running, you can find me**: When I'm not running, I'm either traveling, hanging out with friends, playing Minecraft, or trying new restaurants. :)
             - **Go to food/snack order**: In n out, number 3 with a coke. 
        """)

with col2:
    image = Image.open("./assets/louise_wtc.png")
    image = ImageOps.exif_transpose(image)
    st.image(image, output_format = "PNG")

#-------Leader ----------------------

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.header("Lia (She/Her)", anchor=False)
    st.write(""" 
             - **Why I run?**: I run for the endorphins, the friends who push me to go further than I thought possible, and the food that's waiting at the finish. 
             - **Go-to running trail**: Pipeline Trail.
             - **When I'm not running, you can find me**: Pretending to stretch, indoor cycling, hiking with my camera in hand, and performing craniotomies on fruit flies—for science, of course!     
             - **Go to food/snack order**: Scandinavian Swimmers.
        """)

with col2:
    #st.header("(Insert Photo Here)", anchor=False)
    
    st.image("./assets/lia_wtc.png", output_format = "PNG")

#-------Leader ----------------------

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.header("Kaya (Pronouns)", anchor=False)
    st.write(""" 
             - Why I run?:
             - Go-to running trail:
             - When I'm not running, you can find me:
             
             - Go to Boba Order:
        """)

with col2:
    st.header("(Insert Photo Here)", anchor=False)

#-------Leader ----------------------

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.header("Rogelio (Pronouns)", anchor=False)
    st.write(""" 
             - Why I run?:
             - Go-to running trail:
             - When I'm not running, you can find me:
             
             - Go to Boba Order:
        """)

with col2:
    st.header("(Insert Photo Here)")

#-------Leader ----------------------

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.header("DeShawna", anchor=False)
    st.write(""" 
             - **Why I run?**: I run to feel alive! To feel the cold air to my finger tips and the sweat
             running down my face; feeling my heart beating so fast; feeling the burn in my legs to running up the mountains!
             The pain and disconfort feels so good just within that moment.
             - **Go-to running trail**: Malans Mountain-eye challenging with good vert, good technicality of stepping,
              and beautiful scenery!
             - **When I'm not running, you can find me**: Mom duties; homework, cleaning and doing laundry! it's never
             ending tasks!
             
             - ** Go to food/snack order** : Pickles 🥒, potato chips and coke! I try to keep simple and easy! and affordable 😊.
        """)

with col2:
    
    st.image("./assets/deshawna_wtc.png", output_format = "PNG")