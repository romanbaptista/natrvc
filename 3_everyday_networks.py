import streamlit as st

## PAGE CONFIG
# Set sidebar and layout
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Hide title anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

lrcol_width = 0.22
mcol_width = 0.5

## FORMAT COLUMNS
lcol, mcol, rcol = st.columns([lrcol_width, mcol_width ,lrcol_width], gap = 'medium', vertical_alignment = 'center')

with mcol:
    # Title
    # Title
    st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Everyday networks</h1>', unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.video('./assets/videos/anim2.mp4', autoplay = True, loop = True)

    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 30px; font-weight: bold;">Social networks represent complex relationships</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">We understand these easier as we can relate them to our everyday lives.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Knowing who or what you\'re interacting with can allow companies to make recommendations.</h1>', unsafe_allow_html=True)
    st.write('\n')

    lcol2,mcol2,rcol2 = st.columns(3, gap = 'large', vertical_alignment = 'top')
    
    with lcol2:
        if st.button('Back', use_container_width = True):
            st.switch_page('pages/2_what_are_networks.py')
    with rcol2:
        if st.button('Next', use_container_width = True):
            st.switch_page('pages/4_nodes_of_interest.py')
