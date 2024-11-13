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

if 'selected_pathway' not in st.session_state:
    st.session_state.selected_pathway = None

## FUNCTIONS

def highlight_pathway_nodes(graph, pathway):
    '''
    Takes a graph and a pathway name to generate node colouring/opacity based on a given pathway.
    '''
    
    # Define colors
    pathway_color = 'rgb(41, 175, 128)'  # Color for nodes associated with the pathway
    hub_color = 'rgb(220, 227, 25)'      # Color for hub nodes associated with multiple pathways
    other_color = 'grey'                 # Color for nodes not associated with the pathway

    # Define alpha values
    pathway_alpha = 1
    hub_alpha = 1
    other_alpha = 0.25

    # Initialize color list
    colours = []
    alphas = []

    # Iterate over all nodes
    for node in graph.nodes:
        # Check if node is associated with the pathway
        is_in_pathway = graph.nodes[node].get(pathway) == 1

        # Check if node is a hub (associated with multiple pathways)
        is_hub = sum(attr == 1 for attr in graph.nodes[node].values()) > 1

        # Assign colors based on conditions
        if is_in_pathway and is_hub:
            colours.append(hub_color)  # Hub node in the pathway
            alphas.append(hub_alpha)
        elif is_in_pathway:
            colours.append(pathway_color)  # Node in the pathway only
            alphas.append(pathway_alpha)
        else:
            colours.append(other_color)  # Node not in the pathway
            alphas.append(other_alpha)
    
    return colours, alphas

def highlight_pathway_edges(graph, pathway):
    '''
    Takes a graph and a pathway name to generate edge colouring/opacity based on a given pathway.
    '''

    # Define colours
    pathway_colour = 'gainsboro'
    non_pathway_colour = 'grey'

    colours = []
    alphas = []

    # Get nodes in the pathway
    pathway_nodes = [node for node, data in graph.nodes(data=True) if data.get(pathway) == 1]

    # Set color and alpha based on whether both nodes in an edge are in the pathway
    for u, v in graph.edges:
        if u in pathway_nodes and v in pathway_nodes:
            colours.append(pathway_colour)  # Edge is within the pathway
            alphas.append(1)
        else:
            colours.append(non_pathway_colour)  # Edge is outside the pathway
            alphas.append(0.25)

    return colours, alphas

def generate_highlighted_pathway_graph(graph: nx.Graph, 
                                       node_x: list, 
                                       node_y: list,
                                       edge_x: list,
                                       edge_y: list,
                                    #    edge_trace,
                                       highlighted_pathway = None,
                                       plot_size: int = 600,
                                       node_size: int = 50,
                                       title_show: bool = False,
                                       title_text: str = 'Network Graph',
                                       title_text_size: int = 18):
    '''
    Generates an updated version of an existing graph
    '''

    # Generate node colour/opacity
    if highlighted_pathway is not None:
        node_colours, node_alphas = (highlight_pathway_nodes(graph, highlighted_pathway))
    else:
        node_colours =  ['grey'] * len(graph.nodes)
        node_alphas = [1] * len(graph.nodes)
    
    # Define marker_dict
    marker_dict = {'size' : node_size,
                   'color' : node_colours,
                   'opacity' : node_alphas,
                   'line' : {'color' : 'black', 'width' : 3}}

    # Node trace with updated colours/opacity
    node_trace = go.Scatter(x = node_x, y = node_y,
                            mode = 'markers+text',
                            hoverinfo = 'none',
                            marker = marker_dict)
    
    # Generate node colour/opacity
    if highlighted_pathway is not None:
        edge_colours, edge_alphas = (highlight_pathway_edges(graph, highlighted_pathway))
    else:
        edge_colours = ['grey'] * len(graph.edges)
        edge_alphas = [0.25] * len(graph.edges)

    # Define edge line dict
    line_dict = {'color' : edge_colours,
                    'width' : 2}

    # Edge trace with updated colours/opacity
    # edge_trace = go.Scatter(x = edge_x, y = edge_y,
    #                         mode = 'lines',
    #                         line = line_dict,
    #                         opacity = edge_alphas)

    # Attempt to generate individual traces
    # Initialize list to hold edge traces
    edge_traces = []

    # Loop through edges to create individual traces
    for i, (u, v) in enumerate(graph.edges):
        # Create the trace for each edge with the specified color and opacity
        trace = go.Scatter(
            x=[pos[u][0], pos[v][0], None],  # None to break line between edges
            y=[pos[u][1], pos[v][1], None],
            mode="lines",
            line=dict(color=edge_colours[i], width=2),
            opacity=edge_alphas[i]
        )
        edge_traces.append(trace)

    # Define axis_dict
    axis_dict = {'showgrid' : False, 
                 'zeroline' : False,
                 'showticklabels' : False}
    
    # Define title_dict
    title_dict = {'text' : title_text,
                  'font' : {'size' : title_text_size}}
    
    # Define annotation dictionary
    annot_dict = {'text' : '<span style="color: grey;"><b>Grey</b></span> = Non-member<br><span style="color: rgb(41, 175, 128);"><b>Green</b></span> = Member<br><span style="color: rgb(220, 227, 25);"><b>Yellow</b></span> = Joint member',
                  'x' : 0,
                  'y': 0.045,
                  'showarrow' : False,
                  'align' : 'left',
                  'xref' : 'paper',
                  'yref' : 'paper',
                  'xanchor' : 'left',
                  'yanchor' : 'bottom',
                  'font' : {'size' : 16, 'color' : 'gainsboro'},
                  'bgcolor' : 'rgba(255, 255, 255, 0)'}
    
    # Define layout
    layout = go.Layout(title = title_dict if title_show == True else None,
                       showlegend = False,
                       height = plot_size,
                       width = plot_size,
                       xaxis = axis_dict,
                       yaxis = axis_dict,
                       annotations = [annot_dict])
    
    # Create figure
    figure = go.Figure(data = edge_traces + [node_trace], layout = layout)

    return figure

## GRAPH
# Import graph
with open('assets/graphs/pathway_graph.pickle', 'rb') as f:
    graph = pickle.load(f)
# Import positional data
with open('assets/graphs/pathway_pos.pickle', 'rb') as f:
    pos = pickle.load(f)

# Get node pos
node_x, node_y = af.get_node_pos(graph, pos)
# Get edge pos
edge_x, edge_y = af.get_node_pos(graph, pos)

# Generate edge trace
# edge_trace = af.generate_edge_trace(edge_x, edge_y, weight = 0.5, alpha = 0.25) # Removed temporarily to test updating opacitys

# Define pathways
pathways = ['Transport', 'Metabolism', 'DNA', 'Cell Division', 'Immune System', 'Apoptosis']

## PAGE LAYOUT

## CONTENTS

# Title
st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Host-pathogen interactions</h1>', unsafe_allow_html=True)


# Columns
lcol, rcol = st.columns([0.4, 0.6], gap = 'medium', vertical_alignment = 'center')

# Left column
with lcol:

    ## TEXT
    # Body
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">HPIs describe the proteins that a pathogen targets in a host.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Knowing protein targets and their wider pathways is important to uncover the mechanisms of different pathogens.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Knowing their plans of attack lets you develop more effective treatments against them.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Select the pathway options below to see how targeting one protein can affect a large area of a network.</h1>', unsafe_allow_html=True)
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')

    ## BUTTONS
    # Define number of columns
    num_columns = 3
    # Generate columns
    button_cols = st.columns(num_columns)
    # Iterate over pathways
    for i, pathway in enumerate(pathways):
        # Divide by number of columns to get row/column order
        row, col = divmod(i, num_columns)
        # Generate buttons in situ
        with button_cols[col]:
            if st.button(f'{pathway}', key = f'pathway_button_{pathway}', use_container_width = True):
                st.session_state.selected_pathway = pathway

# Define highlighted pathway
highlighted_pathway = st.session_state.selected_pathway

# Right column
with rcol:

    # Generate highlighted figure
    figure = generate_highlighted_pathway_graph(graph,
                                                node_x = node_x, node_y = node_y,
                                                edge_x = edge_x, edge_y = edge_y,
                                                highlighted_pathway = highlighted_pathway,
                                                node_size = 25,
                                                plot_size = 600,
                                                title_show = False)
    
    # Plot highlighted figure
    st.plotly_chart(figure, use_container_width = True)

## PATHWAY DESCRIPTIONS

# Store pathway descriptions
pathway_desc = {
    'Transport' : 'Transport pathways move nutrients, ions and waste products across cellular membranes.<br><br>Pathogens can manipulate host transport systems to gain entry into cells or disrupt the transport of immune signaling molecules.',
    'Metabolism' : 'Metabolism encompasses the set of chemical reactions that provide energy and building blocks for cellular functions.<br><br>Pathogens can hijack the host\'s metabolic machinery to support their growth, and create an good environment for their survival and replication.',
    'DNA' : 'The DNA pathway is responsible for maintaining, repairing, and replicating the cell\'s genetic material.<br><br>Pathogens often directly interact with the host\'s DNA repair and replication machinery to facilitate their own replication.',
    'Cell Division' : 'Cell division is critical for cell proliferation and tissue growth.<br><br>Pathogens can interfere with the host\'s cell cycle machinery to promote rapid cell division, causing more effective spread.',
    'Immune System' : 'Immune pathways include all processes related to the detection and elimination of foreign invaders.<br><br>Pathogens directly interact with immune system proteins, suppressing them, or exploit immune signaling pathways to evade detection.',
    'Apoptosis' : 'Apoptosis, or programmed cell death, is essential for eliminating damaged or infected cells.<br><br>Pathogens can inhibit apoptosis in infected cells to prolong their survival and replication, or cause apoptosis in immune cells to avoid detection.'
}

# Set column widths
lrcol_width = 0.25
mcol_width = 0.9

# Format columns
lcol, mcol, rcol = st.columns([lrcol_width, mcol_width ,lrcol_width], gap = 'small', vertical_alignment = 'top')

with mcol:
    if highlighted_pathway is not None:
        st.write(f'<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">{pathway_desc[highlighted_pathway]}</h1>', unsafe_allow_html=True)
# st.write('\n')
# st.write('\n')
# st.write('\n')


highlighted_pathway = None
st.session_state.selected_pathway = None

## BACK/NEXT BUTTONS
lrcol_width = 0.4
mcol_width = 0.4

# Columns
llcol, lcol, mcol, rcol, rrcol = st.columns([lrcol_width, lrcol_width, lrcol_width, lrcol_width, lrcol_width,], gap = 'large', vertical_alignment = 'top')
with llcol:
    if st.button('Back', use_container_width = True):
        st.switch_page('pages/6_protein_pathways.py')

with rrcol:
    if st.button('Next', use_container_width = True):
        st.switch_page('pages/8_using_ai.py')
