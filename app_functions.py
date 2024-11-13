import numpy as np
import networkx as nx
import pandas as pd
import plotly.graph_objects as go
import random
from tqdm import tqdm

def generate_network(num_nodes: int = 50, edge_chance: float = 0.15) -> nx.Graph:
    '''
    Generates a Networkx graph using the Watts-Strogatz method.
    '''

    graph = nx.watts_strogatz_graph(n = num_nodes, k = 10, p = edge_chance)

    return graph

def get_node_pos(graph: nx. Graph, pos: dict) -> list:
    '''
    Returns a list of positional data for nodes in a given Networkx graph object.
    '''

    node_x = [pos[node][0] for node in graph.nodes()]
    node_y = [pos[node][1] for node in graph.nodes()]
    
    return node_x, node_y

def get_edge_pos(graph: nx.Graph, pos: dict) -> list:
    '''
    Returns a list of positional data for edges in a given Networkx graph object.
    '''

    # Initialise lists
    edge_x = []
    edge_y = []

    # Iterate through graph edges
    for edge in graph.edges():
        # Get values
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        # Extend lists
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    return edge_x, edge_y

def generate_node_trace(node_x: list, node_y: list, 
                        size: int = 20,
                        color = 'indianred', 
                        cmap: str = 'viridis', 
                        cmin: int = 1,
                        cmax: int = 5,
                        alpha = 1,
                        linecolor: str = 'gainsboro', 
                        linewidth: float = 0.75,
                        hoverinfo = 'text',
                        text: str = None,
                        hoverlabel_text_size: int = 13,
                        cbar_show: bool = True, 
                        cbar_title: str = 'Degree',
                        cbar_thickness: int = 15) -> go.Scatter:
    '''
    Returns a plotly graph object node trace.
    '''

    # Define colorbar format dictionary
    cbar_dict = {'thickness' : cbar_thickness,
                 'xanchor' : 'left',
                 'title' : {'text' : cbar_title,
                            #'size' : cbar_title_size,
                            'side' : 'right'}}

    # Define marker format dictionary
    marker_dict = {'size' : size,
                   'color' : color,                                      
                   'colorscale' : cmap,
                   'cmin' : cmin,
                   'cmax' : cmax,
                   'opacity' : alpha,
                   'line' : {'color' : linecolor,
                             'width' : linewidth},
                   'showscale' : cbar_show,
                   'colorbar' : cbar_dict if cbar_show == True else None}
    
    hoverlabel_dict = {'font_size' : hoverlabel_text_size,
                       'align' : 'left'}

    # Generate node trace
    node_trace = go.Scatter(x = node_x, y = node_y,
                            mode = 'markers',
                            marker = marker_dict,
                            hoverinfo = hoverinfo,
                            text = text,
                            hoverlabel = hoverlabel_dict)

    return node_trace

def generate_edge_trace(edge_x: list, edge_y: list, weight: float = 0.5, alpha: float = 0.25) -> go.Scatter:
    '''
    Returns a plotly graph object edge trace.
    '''

    # Define edge format dictionary
    edge_dict = {'width' : weight,
                 'color' : f'rgba(220, 220, 220, {alpha})'}

    # Generate edge trace
    edge_trace = go.Scatter(x = edge_x, y = edge_y,
                            mode = 'lines',
                            line = edge_dict,
                            hoverinfo = 'none')
    
    return edge_trace

def plot_network(node_trace: go.Scatter, edge_trace: go.Scatter,
                 size = 500,
                 title_show: bool = True,
                 title_text: str = 'Network Visualisation',
                 title_text_size: int = 16,
                 tblr_margin: list = [40, 10, 10, 10],
                 annot_show: bool = False,
                 annot_pos: tuple = (0,0),
                 annot_text: str = 'Annotation',
                 annot_text_size: int = 18,
                 annot_text_color: str = 'gainsboro',
                 minlim: int = -1,
                 maxlim: int = 1,
                 xaxis_grid: bool = False,
                 xaxis_line: bool = False, 
                 xaxis_ticks: bool = False,
                 yaxis_grid: bool = False,
                 yaxis_line: bool = False,
                 yaxis_ticks: bool = False) -> go.Figure:
    '''
    Generates a plotly network visualisation from node and edge trace go.Scatter objects.
    '''

    # Define title format dictionary
    title_dict = {'text' : title_text,
                  'font' : {'size' : title_text_size}}
    
    # Define marging format dictionary
    margin_dict = {'t' : tblr_margin[0],
                   'b' : tblr_margin[1],
                   'l' : tblr_margin[2],
                   'r' : tblr_margin[3],}
    
    # Define xaxis format dictionary
    xaxis_dict = {'showgrid' : xaxis_grid,
                  'zeroline' : xaxis_line,
                  'showticklabels' : xaxis_ticks,
                  'range' : [minlim, maxlim]}
    
    # Define yaxis format dictionary
    yaxis_dict = {'showgrid' : yaxis_grid,
                  'zeroline' : yaxis_line,
                  'showticklabels' : yaxis_ticks,
                  'range' : [minlim, maxlim]}
    
    # Define annotation format dictionary
    annot_dict = {'text' : annot_text if annot_show == True else None,
                  'x' : annot_pos[0],
                  'y' : annot_pos[1],
                  'showarrow' : False,
                  'align' : 'left',
                  'xref' : 'paper',
                  'yref' : 'paper',
                  'xanchor' : 'left',
                  'yanchor' : 'bottom',
                  'font' : {'size' : annot_text_size, 'color' : annot_text_color},
                  'bgcolor' : 'rgba(255, 255, 255, 0)'}
    
    # Plot
    figure = go.Figure(data = [edge_trace, node_trace],
                       layout = go.Layout(title = title_dict if title_show == True else None,
                                          height = size,
                                          width = size,
                                          showlegend = False,
                                          hovermode = 'closest',
                                          margin = margin_dict,
                                          annotations = [annot_dict],
                                          xaxis = xaxis_dict,
                                          yaxis = yaxis_dict))

    return figure

def plot_animated_network(num_nodes: int = 10,
                          node_size: int = 25,
                          node_line_color: str = 'black',
                          node_line_width: float = 0.75, 
                          spring_dist: float = 0.2, 
                          num_frames: int = 50,
                          title_show: bool = False,
                          title_text: str = 'Animated Network',
                          title_text_size: int = 16,
                          frame_duration: int = 500,
                          transition_duration: int = 300) -> go.Figure:
    '''
    Returns an animated plotly graph object.
    '''

    # Generate graph
    graph = generate_network(num_nodes)
    # Get positional data
    pos = nx.spring_layout(graph, k = spring_dist)
    # Get degree values
    degrees = [graph.degree[node] for node in graph.nodes]
    # Get min degree value
    min_degree = min(degrees)
    # Get maximum degree value
    max_degree = max(degrees)
    # Scale values for alpha
    alphas = [((value - 1)/(max_degree - 1)) for value in degrees]

    # Get node pos
    node_x, node_y = get_node_pos(graph, pos)
    # Get edge pos
    edge_x, edge_y = get_edge_pos(graph, pos)

    # # Generate start node trace
    # start_node_trace = generate_node_trace(node_x = node_x, node_y = node_y, size = node_size, color = degrees, cmap = 'viridis', cmin = min_degree, cmax = max_degree, alpha = alphas, cbar_show = False)
    # Generate edge trace
    edge_trace = generate_edge_trace(edge_x = edge_x, edge_y = edge_y, alpha = 0.15)

    # Initialise frames list
    frames = []

    # updated_degrees = degrees

    # Iterate through the desired number of frames
    for frame in range(num_frames):
        
        # Select one random index to change between 1 and max_degree
        change_index = random.randint(0, len(degrees) - 1)
        # Edit value at that index
        degrees[change_index] = random.randint(1, max_degree)
    
        # Scale values for alpha
        alphas = [((value - 1)/(max_degree - 1)) for value in degrees]
        # Scale values for size
        sizes = [degree * 1.75 for degree in degrees]

        # Generate node trace
        node_trace = generate_node_trace(node_x = node_x, node_y = node_y, 
                                         size = sizes, color = degrees, 
                                         cmap = 'haline', cmin = min_degree, cmax = max_degree, 
                                         alpha = alphas, 
                                         cbar_show = False, 
                                         linecolor = node_line_color,
                                         linewidth = node_line_width)

        # Append trace data to frames
        frames.append(go.Frame(data = [edge_trace, node_trace]))

    minlim = -1.05
    maxlim = 1.05

    # Define axis format dictionary
    axis_dict = {'showgrid' : False,
                 'zeroline' : False,
                 'showticklabels' : False,
                 'range' : [minlim, maxlim]}
    
    # Define updatemenus format dictionary
    updatemenu_dict = {'type' : 'buttons',
                       'visible' : True,
                       'showactive' : False,
                       'buttons' : [{'label' : 'Play',
                                     'method' : 'animate',
                                     'args' : [None, {'frame' : {'duration' : frame_duration, 
                                                                 'redraw' : True},
                                                      'fromcurrent' : True,
                                                      'mode' : 'immediate',
                                                      'transition' : {'duration' : transition_duration, 'easing' : 'cubic-bezier(1, 0, 0, 1)'},
                                                      'loop' : True}]}]}

    # Plot
    figure = go.Figure(data = [frames[0].data[0], frames[0].data[1]],
                       layout = go.Layout(height = 800, 
                                          width = 800,
                                          title = title_text if title_show == True else None,
                                          showlegend = False,
                                          xaxis = axis_dict,
                                          yaxis = axis_dict,
                                          updatemenus = [updatemenu_dict]),
                       frames = frames)
    
    # Configure autoplay
    
    return figure
