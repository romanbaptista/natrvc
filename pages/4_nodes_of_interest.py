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
    st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Nodes of interest</h1>', unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    # st.write('\n')
    # st.write('\n')

    st.video('./assets/videos/anim3.mp4', autoplay = True, loop = False)

    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 30px; font-weight: bold;">More connections = more neighbours = more important</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Highly connected nodes are called \'hubs\'.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Hubs are able to easily affect large parts of the network, and can be targets for disruption and treatment.</h1>', unsafe_allow_html=True)
    st.write('\n')

    lcol2,mcol2,rcol2 = st.columns(3, gap = 'large', vertical_alignment = 'top')
    
    with lcol2:
        if st.button('Back', use_container_width = True):
            st.switch_page('pages/3_everyday_networks.py')
    with rcol2:
        if st.button('Next', use_container_width = True):
            st.switch_page('pages/5_targeting_proteins.py')
