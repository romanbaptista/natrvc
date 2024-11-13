## PACKAGES
import streamlit as st

## PAGE CONFIG
# Set sidebar and layout
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Hide title anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

## PAGE LAYOUT

# Set column widths
lrcol_width = 0.22
mcol_width = 0.5

# Set columns
lcol, mcol, rcol = st.columns([lrcol_width, mcol_width ,lrcol_width], gap = 'medium', vertical_alignment = 'center')

## CONTENTS

with mcol:
    # Title
    st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Protein pathways</h1>', unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.video('assets/videos/anim4.mp4', autoplay = True, loop = True, start_time = 18)

    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 30px; font-weight: bold;">Protein are members of pathways</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Pathways are groups of proteins that work together to produce an effect.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Pathogens trying to disrupt cellular networks will affect pathways through their proteins targets.</h1>', unsafe_allow_html=True)
    st.write('\n')

    lcol2,mcol2,rcol2 = st.columns(3, gap = 'large', vertical_alignment = 'top')
    
    with lcol2:
        if st.button('Back', use_container_width = True):
            st.switch_page('pages/5_targeting_proteins.py')
    with rcol2:
        if st.button('Next', use_container_width = True):
            st.switch_page('pages/7_host_pathogen_interactions.py')