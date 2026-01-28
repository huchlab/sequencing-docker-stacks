from liana.method import build_prior_network, find_causalnet

# Test: Basic causal network inference
pkn = [
    ("A", 1, "B"),
    ("B", 1, "C"),
]

inputs = {"A": 1}
outputs = {"C": 1}

graph = build_prior_network(pkn, inputs, outputs)
find_causalnet(graph, inputs, outputs, seed=42, max_runs=50)
