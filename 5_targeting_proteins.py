## PACKAGES
import streamlit as st

import app_functions as af
import networkx as nx
import pickle
import plotly.graph_objects as go


## PAGE CONFIG
# Set sidebar and layout
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Hide title anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

## SESSION STATE

if 'selected_node' not in st.session_state:
    st.session_state.selected_node = None
    

## FUNCTIONS

def highlight_node_and_neighbours(graph, node_index):
    '''
    Takes a graph and generates node colouring based on a given node index.
    '''
    
    # Define colours
    node_col = 'rgb(220, 227, 25)'
    #node_col = 'rgb(190, 196, 2)'
    neighbour_col = 'rgb(41, 175, 128)'
    other_col = 'grey'
    
    # Get node neighbours
    neighbours = list(graph.neighbors(node_index))

    # Set colours
    colours = [node_col if i == node_index else
               (neighbour_col if i in neighbours else
                other_col)
               for i in range(len(graph.nodes))]
    
    return colours

def generate_highlighted_graph(graph: nx.Graph, 
                               node_x: list, 
                               node_y: list,
                               edge_trace, 
                               highlighted_node = None,
                               plot_size: int = 600,
                               node_size: int = 50,
                               text_font_size: int = 24,
                               text_font_color: str = 'gainsboro',
                               text_font_weight: str = 'bold',
                               title_show: bool = False,
                               title_text: str = 'Network Graph',
                               title_text_size: int = 18):
    '''
    Generates an updated version of an existing graph
    '''

    # Apply node colours to plot
    colours = (highlight_node_and_neighbours(graph, highlighted_node)
               if highlighted_node is not None else ['grey'] * len(graph.nodes))
    
    # Define marker_dict
    marker_dict = {'size' : node_size,
                   'color' : colours,
                   'line' : {'color' : 'black', 'width' : 3}}

    # Node trace with updated colours
    node_trace = go.Scatter(x = node_x, y = node_y,
                            mode = 'markers+text',
                            hoverinfo = 'none',
                            marker = marker_dict,
                            text = [node_labels[node] for node in graph.nodes],
                            textposition = 'bottom center',
                            textfont = {'size' : text_font_size,
                                        'color' : text_font_color,
                                        'weight' : text_font_weight})
    
    # Define axis_dict
    axis_dict = {'showgrid' : False, 
                 'zeroline' : False,
                 'showticklabels' : False}
    
    # Define title_dict
    title_dict = {'text' : title_text,
                  'font' : {'size' : title_text_size}}
    
    # Define layout
    layout = go.Layout(title = title_dict if title_show == True else None,
                       showlegend = False,
                       height = plot_size,
                       width = plot_size,
                       xaxis = axis_dict,
                       yaxis = axis_dict)
    
    # Create figure
    figure = go.Figure(data = [edge_trace, node_trace], layout = layout)

    return figure

@st.dialog('Check Answer', width = 'small')
def show_check_answer():
    lcol, mcol, rcol = st.columns([0.4,0.2,0.4], gap = 'small')
    if highlighted_node == highest_degree_node:
        with mcol:
            st.image('assets/icons/check_mark.png', width = 100)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 30px; font-weight: normal; text-align: center;"><b>Correct!</b></h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 20px; font-weight: normal;">This is the most well-connected \'hub\' node in the network.</h1>', unsafe_allow_html=True)
        
    elif highlighted_node != highest_degree_node and highlighted_node != None:
        with mcol:
            st.image('assets/icons/question_mark2.png', width = 100)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 30px; font-weight: normal; text-align: center;"><b>Almost!</b></h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 20px; font-weight: normal;">Remember that pathogens will target the node with the <b>most</b> connections.</h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 20px; font-weight: normal;">While this is a well-connected node, there is one with even more!</h1>', unsafe_allow_html=True)
        
    elif highlighted_node == None:
        with mcol:
            st.image('assets/icons/search_mark.png', width = 100)
        st.write('<h1 style="font-family: Aptos, sans-serif; font-size: 30px; font-weight: normal; text-align: center;"><b>No node selected</b></h1>', unsafe_allow_html=True)
        st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 20px; font-weight: normal;">Please select a node first, and then check your answer again!</h1>', unsafe_allow_html=True)
        

## GRAPH

# Import graph
with open('assets/graphs/nine_node.pickle', 'rb') as f:
    graph = pickle.load(f)
# Import positional data
with open('assets/graphs/nine_node_pos.pickle', 'rb') as f:
    pos = pickle.load(f)

# Get node pos
node_x, node_y = af.get_node_pos(graph, pos)
# Get edge pos
edge_x, edge_y = af.get_edge_pos(graph, pos)
# Generate edge trace
edge_trace = af.generate_edge_trace(edge_x, edge_y, weight = 0.75, alpha = 1)

# Set variables
node_size = 50
node_labels = {node : node for node in list(graph.nodes)}

# Get node with highest degree
highest_degree_node = max(graph.degree(), key=lambda x: x[1])[0]

## PAGE LAYOUT

# Title
st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Targeting proteins</h1>', unsafe_allow_html=True)
st.write('\n')
st.write('\n')
st.write('\n')

# Columns
lcol, rcol = st.columns([0.4, 0.6], gap = 'medium', vertical_alignment = 'center')

## CONTENTS

# Left column
with lcol:
    
    ## TEXT
    # Body
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Pathogens like parasites target protein networks for maximum disruption, damage or manipulation.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Given what you know about highly connected hub nodes being important, can you find the best node to attack in this network?</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Select the node below to see its neighbours, and then \'Check Answer\' to see if you\'re correct!</h1>', unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')

    ## BUTTONS
    # Define number of columns
    num_columns = 3
    # Generate columns
    button_cols = st.columns(num_columns)
    # Iterate over graph nodes
    for i, node in enumerate(graph.nodes):
        # Divide by number of columns to get row/column order
        row, col = divmod(i, num_columns)
        # Generate buttons in situ
        with button_cols[col]:
            if st.button(f'Node {node_labels[node]}', key = f'node_button_{node}', use_container_width = True):
                st.session_state.selected_node = node
                

# Define highlighted_node
highlighted_node = st.session_state.selected_node

# Right column
with rcol:

    # Generate highlighted figure
    figure = generate_highlighted_graph(graph, 
                                        node_x = node_x, node_y = node_y, 
                                        edge_trace = edge_trace, 
                                        highlighted_node = highlighted_node,
                                        node_size = 50, 
                                        plot_size = 600,
                                        title_show = False)
    
    # Plot highlighted figure
    st.plotly_chart(figure, use_container_width = True)

# Columns
lrcol_width = 0.3
mcol_width = 0.1
lcol, mcol, rcol = st.columns([lrcol_width, mcol_width ,lrcol_width], gap = 'medium', vertical_alignment = 'top')

with mcol:
    if st.button('Check answer', use_container_width = True):
        show_check_answer()
        st.session_state.selected_node = None


st.write('\n')
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
        st.switch_page('pages/4_nodes_of_interest.py')
with rrcol:
    if st.button('Next', use_container_width = True):
        st.switch_page('pages/6_protein_pathways.py')


