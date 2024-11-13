# import streamlit as st

# import app_functions as af
# import networkx as nx
# import pickle

# ## PAGE CONFIG
# # Set sidebar and layout
# st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# # Hide title anchors
# st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

# ## SESSION STATE

# ## FUNCTIONS

# def reveal_drug_graph()
    
# ## GRAPH
# # Import graph
# with open('assets/graphs/drug_effect_graph.pickle', 'rb') as f:
#     graph = pickle.load(f)
# # Import positional data
# with open('assets/graphs/drug_effect_pos.pickle', 'rb') as f:
#     pos = pickle.load(f)

# # Get node pos
# node_x, node_y = af.get_node_pos(graph, pos)
# # Get edge pos
# edge_x, edge_y = af.get_edge_pos(graph, pos)

# ## BARPLOT(S)


# ## PAGE LAYOUT

# # Columns
# lcol, rcol = st.columns([0.5, 0.5], gap = 'medium', vertical_alignment = 'center')

# ## CONTENTS

# with lcol:
#     st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Drug effects</h1>', unsafe_allow_html=True)
#     st.write('\n')
#     st.write('\n')
#     st.write('\n')

# with rcol:
#     # Background graph of all red nodes
#     # On button press
#         # Increase alpha of drug nodes
#         # Update barplot(s)
#             # % nodes shown
#             # Number of drugs x 25% for negative effects

#     st.write('graph goes here with barplot(s) to the right')

# ## BACK/NEXT BUTTONS

### THIS FIRST PASS WORKS!! ###

# import streamlit as st
# import plotly.graph_objects as go
# import networkx as nx
# import numpy as np
# from matplotlib import cm

# # Simulated graph with positional data for demonstration
# G = nx.erdos_renyi_graph(20, 0.2)  # Replace with your actual graph
# np.random.seed(42)
# for i, node in enumerate(G.nodes()):
#     G.nodes[node]['disease'] = np.random.rand()
#     G.nodes[node]['cluster'] = i % 3
#     G.nodes[node]['drug_1'] = np.random.choice([0, 1])
#     G.nodes[node]['drug_2'] = np.random.choice([0, 1])
#     G.nodes[node]['drug_3'] = np.random.choice([0, 1])
#     G.nodes[node]['drug_4'] = np.random.choice([0, 1])

# # Positional data (example positions, replace with your edge_x, edge_y, node_x, node_y)
# pos = nx.spring_layout(G)
# node_x = [pos[n][0] for n in G.nodes()]
# node_y = [pos[n][1] for n in G.nodes()]
# edge_x, edge_y = [], []
# for edge in G.edges():
#     x0, y0 = pos[edge[0]]
#     x1, y1 = pos[edge[1]]
#     edge_x.extend([x0, x1, None])
#     edge_y.extend([y0, y1, None])

# # Define session state to track highlighted drug
# if 'highlighted_drug' not in st.session_state:
#     st.session_state.highlighted_drug = None

# # Create color scale based on 'disease' attribute using Reds palette
# norm = cm.ScalarMappable(cmap="Reds")
# norm.set_clim(0, 1)  # Disease values are between 0 and 1
# node_colors = [norm.to_rgba(G.nodes[node]['disease']) for node in G.nodes()]

# # Function to create the graph figure
# def create_graph(highlighted_drug=None):
#     fig = go.Figure()

#     # Draw edges
#     fig.add_trace(go.Scatter(
#         x=edge_x, y=edge_y,
#         line=dict(width=0.5, color='gray'),
#         hoverinfo='none',
#         mode='lines'
#     ))

#     # Draw nodes
#     for i, node in enumerate(G.nodes()):
#         drug_value = G.nodes[node].get(highlighted_drug, 0) if highlighted_drug else 0
#         node_opacity = 1 if drug_value else 0.5  # Highlighted nodes are fully opaque
#         node_color = 'green' if drug_value else f'rgba({node_colors[i][0]*255}, {node_colors[i][1]*255}, {node_colors[i][2]*255}, {node_opacity})'
        
#         fig.add_trace(go.Scatter(
#             x=[node_x[i]], y=[node_y[i]],
#             mode='markers',
#             marker=dict(
#                 size=10,
#                 color=node_color
#             ),
#             name=f"Node {node}",
#             text=f"Disease: {G.nodes[node]['disease']:.2f}",
#             hoverinfo='text'
#         ))

#     fig.update_layout(showlegend=False)
#     return fig

# # Buttons to highlight nodes by drug association
# drugs = ['drug_1', 'drug_2', 'drug_3', 'drug_4']
# for drug in drugs:
#     if st.button(f"Highlight {drug.capitalize()}"):
#         st.session_state.highlighted_drug = drug if st.session_state.highlighted_drug != drug else None

# # Generate the graph based on the currently highlighted drug
# fig = create_graph(st.session_state.highlighted_drug)
# st.plotly_chart(fig)

### SECOND IMPLEMENTATION ALSO FUNCTIONS, JUST WITHOUT BUTTON FORMATTING WHEN TOGGLED ###

# import streamlit as st
# import plotly.graph_objects as go
# import networkx as nx
# import numpy as np
# from matplotlib import cm

# # Simulated graph with positional data for demonstration
# G = nx.erdos_renyi_graph(20, 0.2)  # Replace with your actual graph
# np.random.seed(42)
# for i, node in enumerate(G.nodes()):
#     G.nodes[node]['disease'] = np.random.rand()
#     G.nodes[node]['cluster'] = i % 3
#     G.nodes[node]['drug_1'] = np.random.choice([0, 1])
#     G.nodes[node]['drug_2'] = np.random.choice([0, 1])
#     G.nodes[node]['drug_3'] = np.random.choice([0, 1])
#     G.nodes[node]['drug_4'] = np.random.choice([0, 1])

# # Positional data (example positions, replace with your edge_x, edge_y, node_x, node_y)
# pos = nx.spring_layout(G)
# node_x = [pos[n][0] for n in G.nodes()]
# node_y = [pos[n][1] for n in G.nodes()]
# edge_x, edge_y = [], []
# for edge in G.edges():
#     x0, y0 = pos[edge[0]]
#     x1, y1 = pos[edge[1]]
#     edge_x.extend([x0, x1, None])
#     edge_y.extend([y0, y1, None])

# # Initialize session state to track highlighted drugs
# if 'highlighted_drugs' not in st.session_state:
#     st.session_state.highlighted_drugs = {'drug_1': False, 'drug_2': False, 'drug_3': False, 'drug_4': False}

# # Create color scale based on 'disease' attribute using Reds palette
# norm = cm.ScalarMappable(cmap="Reds")
# norm.set_clim(0, 1)  # Disease values are between 0 and 1
# node_colors = [norm.to_rgba(G.nodes[node]['disease']) for node in G.nodes()]

# # Function to create the graph figure
# def create_graph(highlighted_drugs):
#     fig = go.Figure()

#     # Draw edges
#     fig.add_trace(go.Scatter(
#         x=edge_x, y=edge_y,
#         line=dict(width=0.5, color='gray'),
#         hoverinfo='none',
#         mode='lines'
#     ))

#     # Draw nodes with appropriate color and opacity
#     for i, node in enumerate(G.nodes()):
#         # Check if the node is affected by any selected drugs
#         is_highlighted = any(G.nodes[node][drug] == 1 for drug, selected in highlighted_drugs.items() if selected)
#         node_opacity = 1 if is_highlighted else 0.5
#         node_color = 'green' if is_highlighted else f'rgba({node_colors[i][0]*255}, {node_colors[i][1]*255}, {node_colors[i][2]*255}, {node_opacity})'
        
#         fig.add_trace(go.Scatter(
#             x=[node_x[i]], y=[node_y[i]],
#             mode='markers',
#             marker=dict(
#                 size=10,
#                 color=node_color
#             ),
#             name=f"Node {node}",
#             text=f"Disease: {G.nodes[node]['disease']:.2f}",
#             hoverinfo='text'
#         ))

#     fig.update_layout(showlegend=False)
#     return fig

# # Buttons to toggle visibility for each drug association
# for drug in st.session_state.highlighted_drugs.keys():
#     if st.button(f"Toggle {drug.capitalize()}"):
#         # Toggle the selected state of the drug
#         st.session_state.highlighted_drugs[drug] = not st.session_state.highlighted_drugs[drug]

# # Generate the graph based on the currently highlighted drugs
# fig = create_graph(st.session_state.highlighted_drugs)
# st.plotly_chart(fig)


### THIS NEEDS TO BE REFINED, AND UPDATE THE SECOND BUTTON ASSOCIATED WITH DRUGS IN REAL TIME

import streamlit as st

import app_functions as af
import plotly.graph_objects as go
import networkx as nx
import numpy as np
from matplotlib import cm
import pickle

## PAGE CONFIG
# Set sidebar and layout
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Hide title anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

## FUNCTION
# Create graph
def create_graph(graph, highlighted_drugs, size: int = 700):
    figure = go.Figure()

    edge_trace = af.generate_edge_trace(edge_x,
                                        edge_y,
                                        weight = 0.5,
                                        alpha = 0.25)
    
    figure.add_trace(edge_trace)

    # Draw nodes with colour and opacity
    for i, node in enumerate(graph.nodes):
        # Check if node is affected by selected drugs
        is_highlighted = any(graph.nodes[node][drug] == 1 for drug, selected_drug in highlighted_drugs.items() if selected_drug)
        node_opacity = 1 if is_highlighted else 0.5
        node_color = 'rgb(41, 175, 128)' if is_highlighted else f'rgba({node_colors[i][0]*255}, {node_colors[i][1]*255}, {node_colors[i][2]*255}, {node_opacity})'
    
    # Draw nodes with appropriate color and opacity
    for i, node in enumerate(graph.nodes()):
        # Check if the node is affected by any selected drugs
        is_highlighted = any(graph.nodes[node][drug] == 1 for drug, selected_drug in highlighted_drugs.items() if selected_drug)
        node_opacity = 1 if is_highlighted else 0.5
        node_color = 'rgb(41, 175, 128)' if is_highlighted else f'rgba({node_colors[i][0]*255}, {node_colors[i][1]*255}, {node_colors[i][2]*255}, {node_opacity})'

        figure.add_trace(go.Scatter(
            x=[node_x[i]], y=[node_y[i]],
            mode='markers',
            marker=dict(
                size=20,
                color=node_color,
                line = {'color' : 'black',
                        'width' : 0.75}
            ),
            name=f"Node {node}",
            text=f"Disease: {graph.nodes[node]['disease']:.2f}",
            hoverinfo='none'
        ))

    minlim = -1.05
    maxlim = 1.05

    # Define axis format dictionary
    axis_dict = {'showgrid' : False,
                 'zeroline' : False,
                 'showticklabels' : False,
                 'range' : [minlim, maxlim]}

    figure.update_layout(showlegend=False,
                         xaxis = axis_dict,
                         yaxis = axis_dict,
                         height = size,
                         width = size)
    
    return figure

def calculate_total_highlight_percentage():
    total_nodes = graph.number_of_nodes()
    highlighted_nodes = sum(
        any(graph.nodes[node][drug] == 1 for drug, selected in st.session_state.highlighted_drugs.items() if selected)
        for node in graph.nodes()
    )
    percentage = (highlighted_nodes / total_nodes) * 100
    
    return percentage

## SESSION STATE
if 'highlighted_drugs' not in st.session_state:
    st.session_state.highlighted_drugs = {'Drug 1': False, 'Drug 2': False, 'Drug 3': False, 'Drug 4': False}

## GRAPH
# Import graph
with open('assets/graphs/drug_effect_graph.pickle', 'rb') as f:
    graph = pickle.load(f)
# Import positional data
with open('assets/graphs/drug_effect_pos.pickle', 'rb') as f:
    pos = pickle.load(f)

# Get node pos
node_x, node_y = af.get_node_pos(graph, pos)
# Get edge pos
edge_x, edge_y = af.get_edge_pos(graph, pos)

# Normalised colour scale
norm = cm.ScalarMappable(cmap="Reds")
norm.set_clim(0, 1)  # Disease values are between 0 and 1
node_colors = [norm.to_rgba(graph.nodes[node]['disease']) for node in graph.nodes()]

## CONTENTS

# Title
st.write('<h1 style="font-family: Consolas, sans-serif; font-size: 60px; font-weight: normal;">Drug effects</h1>', unsafe_allow_html=True)

# Set columns
lcol, rcol = st.columns([0.4, 0.6], gap = 'medium', vertical_alignment = 'center')

with lcol:

    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Drugs can target multiple pathways, and therefore large areas of networks.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">It is possible to study their effects on protein networks to observe how they achieve their <span style="color: rgb(41, 175, 128);"><b>beneficial effects</b></span>.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">However, drugs will always come with <span style="color: rgb(220, 227, 25);"><b>side effects</b></span>, especially when used in combination.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">The example host network shown here has experienced <span style="color: indianred;"><b>negative effects</b></span> due to an infection.</h1>', unsafe_allow_html=True)
    st.write('<h1 style="font-family: \'Segoe UI\', sans-serif; font-size: 24px; font-weight: normal;">Toggle combinations of drugs below ON or OFF to maximise beneficial effects on the network, while keeping the side effects underneath the danger level.', unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')

    # Create a 2x2 grid of buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"Drug 1 {'ON' if st.session_state.highlighted_drugs['Drug 1'] else 'OFF'}",
                     use_container_width = True):
            st.session_state.highlighted_drugs['Drug 1'] = not st.session_state.highlighted_drugs['Drug 1']
            st.rerun()
        if st.button(f"Drug 3 {'ON' if st.session_state.highlighted_drugs['Drug 3'] else 'OFF'}",
                     use_container_width = True):
            st.session_state.highlighted_drugs['Drug 3'] = not st.session_state.highlighted_drugs['Drug 3']
            st.rerun()

    with col2:
        if st.button(f"Drug 2 {'ON' if st.session_state.highlighted_drugs['Drug 2'] else 'OFF'}",
                     use_container_width = True):
            st.session_state.highlighted_drugs['Drug 2'] = not st.session_state.highlighted_drugs['Drug 2']
            st.rerun()
        if st.button(f"Drug 4 {'ON' if st.session_state.highlighted_drugs['Drug 4'] else 'OFF'}",
                     use_container_width = True):
            st.session_state.highlighted_drugs['Drug 4'] = not st.session_state.highlighted_drugs['Drug 4']
            st.rerun()

with rcol:
    # Generate the graph based on the currently highlighted drugs
    graph_figure = create_graph(graph, st.session_state.highlighted_drugs)
    st.plotly_chart(graph_figure, use_container_width = True)

    # Calculate barplot of % coverage
    total_percentage = calculate_total_highlight_percentage()
    
    percentage_coverage_barplot = go.Figure(go.Bar(
        x=[total_percentage],
        y=[""],
        orientation='h',
        marker=dict(color='rgb(41, 175, 128)')
    ))

    percentage_coverage_barplot.update_layout(
        title='',
        xaxis = dict(range = [0,100],
                     title = dict(text = 'Beneficial Effect (%)',
                                  font = dict(size = 16, weight = 'bold'))),
        yaxis_title="",   # Set range to 0-100% for better context
        height = 80
    )

    percentage_coverage_barplot.add_annotation(
        x=total_percentage, 
        y="",
        text=f"{total_percentage:.2f}%",
        showarrow=False,
        xshift=0,  # Small shift to position the label clearly past the bar's end
        yshift=12,
        font=dict(size=20, color="rgb(41, 175, 128)", weight = 'bold')
    )

    st.plotly_chart(percentage_coverage_barplot)

    # Generate barplot of negative effects
    total_score = sum(25 for drug, selected in st.session_state.highlighted_drugs.items() if selected)
    
    # Generate barplot
    percentage_negative_barplot = go.Figure(go.Bar(x = [total_score],
                                                   y = [''],
                                                   orientation = 'h',
                                                   marker = dict(color = 'rgb(220, 227, 25)')))
    
    # Set layout
    percentage_negative_barplot.update_layout(title = '',
                                              xaxis = dict(range = [0,100],
                                                           title = dict(text = 'Side Effects (%)',
                                                                        font = dict(size = 16, weight = 'bold'))),
                                              yaxis_title = '',
                                              height = 80)
    
    # Add vline
    percentage_negative_barplot.add_shape(
    type="line",
    x0=50, x1=50, y0=-0.5, y1=0.5,  # Line position
    line=dict(color="red", width=10, dash="dash")
    )

    # Add vline annotation
    percentage_negative_barplot.add_annotation(
    x=50, yshift = 15, 
    text="Danger",
    showarrow=False,
    arrowhead=2,
    # ax=20,  # Offset for the annotation arrow
    # ay=-30,
    font=dict(size=16, color="red", weight = 'bold')
    )

    st.plotly_chart(percentage_negative_barplot)

    

## BACK/NEXT BUTTONS
lrcol_width = 0.4
mcol_width = 0.4

# Columns
llcol, lcol, mcol, rcol, rrcol = st.columns([lrcol_width, lrcol_width, lrcol_width, lrcol_width, lrcol_width,], gap = 'large', vertical_alignment = 'top')
with llcol:
    if st.button('Back', use_container_width = True):
        st.switch_page('pages/9_canada.py')
with rrcol:
    if st.button('Next', use_container_width = True):
        st.switch_page('pages/11_project_objectives.py')
