import liana as li
import networkx as nx
import pandas as pd

# Create a minimal prior graph
prior_graph = nx.DiGraph()
prior_graph.add_edges_from([("A", "B"), ("B", "C")])

# Create input scores
input_scores = pd.Series({"A": 1.5, "B": 0.0, "C": 0.0})

# Create output scores
output_scores = pd.Series({"A": 0.0, "B": 0.8, "C": 1.0})

# Create node weights
node_weights = pd.Series({"A": 0.8, "B": 0.7, "C": 0.6})

li.mt.find_causalnet(prior_graph, input_scores, output_scores, node_weights)
