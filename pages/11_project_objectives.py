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
        st.image('assets/icons/ai_gif.gif')
    
    llcol, mmcol, rrcol = st.columns([0.1, 0.8, 0.1], gap = 'small', vertical_alignment = 'center')
    
    with mmcol:
        st.image('assets/icons/plate_gif.gif')
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 34px; font-weight: normal; text-align: center;"><b>Drug Targets</b></h1>', unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;"><span style="color: rgb(41, 175, 128);"><b>3</b></span> anti-<i>Cryptosporidium</i> compounds</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;"><span style="color: rgb(41, 175, 128);"><b>COLO-680N</b></span> human intestine cell line</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;"><span style="color: rgb(41, 175, 128);"><b>2</b></span> doses (High, Low)</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;"><span style="color: rgb(41, 175, 128);"><b>2</b></span> timepoints (6h, 24h)</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;"></h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;"></h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">This provides data on <span style="color: rgb(41, 175, 128);"><b>how</b></span> the drugs produce their beneficial effects.</h1>', unsafe_allow_html=True)

with rcol:

    llcol, mmcol, rrcol = st.columns([0.33, 0.33, 0.33], gap = 'small', vertical_alignment = 'center')
    
    with mmcol:
        st.image('assets/icons/ai_gif.gif')
    
    llcol, mmcol, rrcol = st.columns([0.1, 0.8, 0.1], gap = 'small', vertical_alignment = 'center')
    
    with mmcol:
        #st.write('## Testing known drugs')
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 34px; font-weight: normal; text-align: center;"><b>Predicting unknown drugs</b></h1>', unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Wider data about drugs is available', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Chemical structure, side effects</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">This data can be passed to machine learning models</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">Can we predict the network effects of <span style="color: rgb(41, 175, 128);"><b>unknown</b></span> drugs?</h1>', unsafe_allow_html=True)
        st.write('\n')
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 24px; font-weight: normal;">This allows us to efficiently simulate effects of new drugs and generate better candidate lists.</h1>', unsafe_allow_html=True)

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
