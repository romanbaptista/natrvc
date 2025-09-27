import streamlit as st

## PAGE CONFIG
# Set sidebar and layout
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Hide title anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

# Title
st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Thanks for Your Time!</h1>', unsafe_allow_html=True)
st.write('\n')
# st.write('\n')
# st.write('\n')


lcol, rcol = st.columns(2, gap = 'medium', vertical_alignment = 'top')

with lcol:

    st.write('\n')
    st.write('\n')
    st.image('assets/images/smile_eimeria.png')
        
with rcol:

    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Thanks to Callum De Hoest-Thompson and Marta Raffaelli for <i>Eimeria</i> photomicrographs</h1>', unsafe_allow_html=True)

    
st.write('\n')
st.write('\n')

## BACK/NEXT BUTTONS
lrcol_width = 0.4
mcol_width = 0.4

# Columns
llcol, lcol, mcol, rcol, rrcol = st.columns([lrcol_width, lrcol_width, lrcol_width, lrcol_width, lrcol_width,], gap = 'large', vertical_alignment = 'top')
with llcol:
    if st.button('Back', use_container_width = True):
        st.switch_page('pages/12_project_objectives.py')
with rrcol:
    if st.button('Home', use_container_width = True):
        st.switch_page('pages/1_home.py')