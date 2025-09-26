import streamlit as st

## PAGE CONFIG
# Set sidebar and layout
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Hide title anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

# Title
st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Project objectives</h1>', unsafe_allow_html=True)
st.write('\n')
# st.write('\n')
# st.write('\n')


lcol, rcol = st.columns(2, gap = 'medium', vertical_alignment = 'top')

with lcol:

    llcol, mmcol, rrcol = st.columns([0.33, 0.33, 0.33], gap = 'small', vertical_alignment = 'center')
    
    with mmcol:
        st.image('assets/icons/lines.gif')
    
    llcol, mmcol, rrcol = st.columns([0.1, 0.8, 0.1], gap = 'small', vertical_alignment = 'center')
    
    with mmcol:
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 34px; font-weight: normal; text-align: center;"><b>Drug Targets</b></h1>', unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Use transcriptomics data to build temporal networks for <i>Eimeria tenella</i></h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Incorporate host-pathogen interactions</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Discard orthologous proteins</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Rank potential drug targets based on connections, lifecycle stages and annotations</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;"></h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;"></h1>', unsafe_allow_html=True)
        
with rcol:

    llcol, mmcol, rrcol = st.columns([0.33, 0.33, 0.33], gap = 'small', vertical_alignment = 'center')
    
    with mmcol:
        st.image('assets/icons/plate_gif.gif')
    
    llcol, mmcol, rrcol = st.columns([0.1, 0.8, 0.1], gap = 'small', vertical_alignment = 'center')
    
    with mmcol:
        #st.write('## Testing known drugs')
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 34px; font-weight: normal; text-align: center;"><b>Vaccine Candidates</b></h1>', unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Predict properties of <i>E. tenella</i> proteins using many bioinformatics packages', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Use machine learning to predict whether proteins produce an <span style="color: rgb(41, 175, 128);"><b>immunoprotective effect</b></span></h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Express top candidates in vector orgaism (e.g. yeast)</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Trial vaccine candidates for <span style="color: rgb(41, 175, 128);"><b>efficacy</b></span> and <span style="color: rgb(41, 175, 128);"><b>safety</b></span></h1>', unsafe_allow_html=True)
        st.write('\n')
        
st.write('\n')
st.write('\n')

## BACK/NEXT BUTTONS
lrcol_width = 0.4
mcol_width = 0.4

# Columns
llcol, lcol, mcol, rcol, rrcol = st.columns([lrcol_width, lrcol_width, lrcol_width, lrcol_width, lrcol_width,], gap = 'large', vertical_alignment = 'top')
with llcol:
    if st.button('Back', use_container_width = True):
        st.switch_page('pages/10_temporal_networks.py')
with rrcol:
    if st.button('Home', use_container_width = True):
        st.switch_page('pages/1_home.py')
