import streamlit as st

## PAGE CONFIG
# Set sidebar and layout
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Hide title anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

lrcol_width = 0.1
mcol_width = 0.9

## FORMAT COLUMNS
lcol, mcol, rcol = st.columns([lrcol_width, mcol_width ,lrcol_width], gap = 'medium', vertical_alignment = 'center')

with mcol:

        st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Networks can change over time</h1>', unsafe_allow_html=True)

        lmcol, rmcol = st.columns([0.5, 0.5], gap = 'small', vertical_alignment = 'center')

        with lmcol:
            st.video('./assets/videos/temporal_network.mp4', autoplay = True, loop = True)

        with rmcol:
            st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 30px; font-weight: bold;">This is called a temporal network.</h1>', unsafe_allow_html=True)
            st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Temporal networks help us understand which biologicl pathways are important at different lifecycle stages.</h1>', unsafe_allow_html=True)
            st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Transcriptomics data provides a snapshot of proteins being made at each lifecycle stage.</h1>', unsafe_allow_html=True)
            st.write('\n')

        lcol2,mcol2,rcol2 = st.columns(3, gap = 'large', vertical_alignment = 'top')
    
        with lcol2:
            if st.button('Back', use_container_width = True):
                st.switch_page('pages/8_using_ai.py')
        with rcol2:
            if st.button('Next', use_container_width = True):
                st.switch_page('pages/10_drug_effects.py')
