# ==========================================
# Imports
# ==========================================
import networkx as nx


# ==========================================
# Calculate global clustering coefficient
# ==========================================
def calculate_gcc(G):
    gcc = nx.transitivity(G)
    return gcc
