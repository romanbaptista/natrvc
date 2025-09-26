import streamlit as st

## PAGE CONFIG
# Set sidebar and layout
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Hide title anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

# Title
st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">My Project</h1>', unsafe_allow_html=True)
st.write('\n')
# st.write('\n')
# st.write('\n')


lcol, rcol = st.columns(2, gap = 'medium', vertical_alignment = 'top')

with lcol:

    st.image('assets/images/hen.png')
    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">The drugs against this disease have become less effective</i></h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">The only commercial vaccines use live parasites to give immunity</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">New drugs and vaccines are required to help chickens and farmers</h1>', unsafe_allow_html=True)
        
with rcol:

    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 34px; font-weight: normal; ">Chickens can catch a parasitic in fection called coccidiosis</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">It is caused by the parasite <i>Eimeria</i>, symptoms include weight loss, diahoerrea and bleeding.', unsafe_allow_html=True)
    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">The disease can be <span style="color: rgb(41, 175, 128);"><b>fatal</b></span></h1>', unsafe_allow_html=True)
    st.image('assets/images/many_eimeria.jpg')
    
st.write('\n')
st.write('\n')

## BACK/NEXT BUTTONS
lrcol_width = 0.4
mcol_width = 0.4

# Columns
llcol, lcol, mcol, rcol, rrcol = st.columns([lrcol_width, lrcol_width, lrcol_width, lrcol_width, lrcol_width,], gap = 'large', vertical_alignment = 'top')
with llcol:
    if st.button('Back', use_container_width = True):
        st.switch_page('pages/11.py')
with rrcol:
    if st.button('Home', use_container_width = True):
        st.switch_page('pages/1_home.py')
