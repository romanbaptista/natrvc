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
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')

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
