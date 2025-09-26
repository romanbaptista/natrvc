
import streamlit as st

## PAGES

home = st.Page(page = 'pages/1_home.py',
               title = 'Home',
               icon = ':material/home:',
               default = True)

what_are_networks = st.Page(page = 'pages/2_what_are_networks.py',
                            title = 'What are networks?',
                            icon = ':material/question_mark:')

everyday_networks = st.Page(page = 'pages/3_everyday_networks.py',
                            title = 'Everyday networks',
                            icon = ':material/notifications:')

nodes_of_interest = st.Page(page = 'pages/4_nodes_of_interest.py',
                            title = 'Nodes of interest',
                            icon = ':material/search:')

targeting_proteins = st.Page(page = 'pages/5_targeting_proteins.py',
                             title = 'Targeting proteins',
                             icon = ':material/adjust:')

protein_pathways = st.Page(page = 'pages/6_protein_pathways.py',
                           title = 'Protein pathways',
                           icon = ':material/conversion_path:')

host_pathogen_interactions = st.Page(page = 'pages/7_host_pathogen_interactions.py',
                                     title = 'Host pathogen interactions',
                                     icon = ':material/link:')

using_ai = st.Page(page = 'pages/8_using_ai.py',
                   title = 'Using AI',
                   icon = ':material/smart_toy:')

ap_drugs = st.Page(page = 'pages/9_ap_drugs.py',
                 title = 'Anti-parasitic Drugs',
                 icon = ':material/microbiology:')

temporal_networks = st.Page(page = 'pages/10_temporal_networks.py',
                            title = 'Temporal Networks',
                            icon = ':material/history:')

drug_effects = st.Page(page = 'pages/10_drug_effects.py',
                 title = 'Drug effects',
                 icon = ':material/pill:')

drug_repurposing = st.Page(page = 'pages/11_project_objectives.py',
                 title = 'Project Objectives',
                 icon = ':material/task_alt:')

## NAVIGATION

nav = st.navigation(pages = [home,
                             what_are_networks, 
                             everyday_networks, 
                             nodes_of_interest, 
                             targeting_proteins, 
                             protein_pathways, 
                             host_pathogen_interactions, 
                             using_ai, 
                             ap_drugs,
                             temporal_networks,
                             drug_repurposing])
nav.run()