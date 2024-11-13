import streamlit as st
import app_functions as af
import pickle
import networkx as nx
import matplotlib.pyplot as plt

## PAGE CONFIG

# Set sidebar and layout
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Hide title anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

## DEFINE COLUMNS

lcolumn, rcolumn = st.columns([0.6, 0.4], gap = 'large', vertical_alignment = 'center')

## CONTENT

# Left column content
with lcolumn:
    # Spaces for formatting
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    
    # Load mitosis graph
    with open("assets/graphs/mitosis.pickle", "rb") as f:
        graph = pickle.load(f)
    # Calculate positional data
    pos = nx.spring_layout(graph, k = 0.8, weight = 'weight')
    #pos = nx.kamada_kawai_layout(graph, weight = None, scale = 1)
    #pos = nx.circular_layout(graph)
    # Get node_pos
    node_x, node_y = af.get_node_pos(graph, pos)
    # Get degree values
    degrees = [graph.degree[node] for node in graph.nodes]
    cmin = 30
    cmax = max(degrees)
    # Scale alpha values from degrees
    alphas = [((value - 1)/((cmax) - 1)) for value in degrees]
    # Get edge weight values
    weights = [graph[u][v]['weight'] for u, v in graph.edges()]
    # Scale sizes
    sizes = [degree/4.5 for degree in degrees]

    # Custom function to wrap text at a certain length
    def wrap_text(text, max_length=60):
        words = text.split(' ')
        wrapped_text = ""
        line_length = 0
        for word in words:
            if line_length + len(word) + 1 > max_length:
                wrapped_text += "<br>"  # Add a line break
                line_length = 0
            wrapped_text += word + " "
            line_length += len(word) + 1  # Update line length
        return wrapped_text.strip()

    # Generate hover annotation from 'node_name' and 'node_desc' node annotations
    node_hover_info_complete = [wrap_text(f'{graph.nodes[node]['node_name']}<br><br>{graph.nodes[node]['node_desc']}') for node in graph.nodes]


    # Get node trace
    node_trace = af.generate_node_trace(node_x, node_y, 
                                        size = sizes, color = degrees, 
                                        cmap = 'haline',
                                        cmin = cmin,
                                        cmax = cmax,
                                        alpha = 0.75,
                                        linecolor = 'gainsboro',
                                        cbar_show = False,
                                        text = node_hover_info_complete,
                                        hoverlabel_text_size = 18)

    # Get edge_pos
    edge_x, edge_y = af.get_edge_pos(graph, pos)
    # Get edge trace
    edge_trace = af.generate_edge_trace(edge_x, edge_y, weight = 0.25, alpha = 0.1)

    figure = af.plot_network(node_trace, edge_trace,
                             size = 800,
                             title_show = False,
                             tblr_margin = [5, 5, 5, 5],
                             annot_show = True,
                             annot_text = f'Human mitosis protein interaction network<br>Number of proteins: {len(graph.nodes)}',
                             annot_pos = (0.05, 0.06),
                             annot_text_size = 22,
                             minlim = -0.8,
                             maxlim = 0.8)
    
    # Define hoverlabel format dictionary
    hoverlabel_dict = {'font_size' : 16,
                       'align' : 'left'}
    
    figure.update_traces()
    
    st.plotly_chart(figure, use_container_width = True)

# Right column content
with rcolumn:

    # Set icon width
    icon_width = 50

    # Title
    #st.write('<h1 style="font-size: 75px;">Protein Networks</h1>', unsafe_allow_html = True)
    st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 70px; font-weight: normal;">Protein Networks</h1>', unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.image('assets/icons/404788FF.png', width = icon_width)
    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 26px; font-weight: normal;">How can we find important proteins?</h1>', unsafe_allow_html=True)
    # st.write('##### How can we find **important proteins**?')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    
    st.image('assets/icons/287D8EFF.png', width = icon_width)
    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 26px; font-weight: normal;">Which proteins are targeted by diseases?</h1>', unsafe_allow_html=True)
    # st.write('##### Which proteins are **targeted by diseases**?')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    
    st.image('assets/icons/55C667FF.png', width = icon_width)
    st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 26px; font-weight: normal;">How can artificial intelligence help us design treatments?</h1>', unsafe_allow_html=True)
    # st.write('##### How can **artificial intelligence** help us design treatments?')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    if st.button('Next', use_container_width = False):
        st.switch_page('pages/2_what_are_networks.py')