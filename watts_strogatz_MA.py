#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:15:13 2022

@author: monamez
"""


import networkx
from matplotlib import pyplot
import numpy as np

def watts_strogatz(n,k,beta):
    G = networkx.Graph()
    for i in range(n):
        G.add_node(i)

    # For every node in the graph,
    for i in range(n):
        # Connect to its neighbors 
        # N+1,N+2,...N+K (mod N yadda yadda)
        for j in range(k):
            G.add_edge(i, (i+j+1)%n)
    #


    ### Rewiring step.

    ######
    # ALGORITHM FOR "REWIRING":
    # totally at random (for watts-strogatz)
    edges = list(G.edges)

    # for every node,
    for u in list(G.nodes):
        # find all edges that connect to it.
        neighbors = list(G.neighbors(u))

        neighbors_plus_me = neighbors + [u]
        others = np.setdiff1d(range(n), neighbors_plus_me)
        others = list(others)
        
        # for each of these edges,
        for v in neighbors:
            # flip a weighted coin; w.p. beta
            # connect to any edge except those 
            # already connected.
            if np.random.rand() < beta:
                vnew = np.random.choice(others)
                others.remove( vnew )
                
                G.remove_edge(u,v)
                G.add_edge(u, vnew)
        #
    #
    return G
