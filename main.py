import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/twitter_data.csv')

# Create a directed graph from the dataset (you can modify this according to your data)
G = nx.DiGraph()

# Add nodes and edges (modify according to the data structure)
for _, row in df.iterrows():
    G.add_node(row['user_id'], name=row['username'])
    if row['follower_id']:
        G.add_edge(row['user_id'], row['follower_id'])

# Perform analysis - Find strongly connected components
strongly_connected = list(nx.strongly_connected_components(G))

# Calculate PageRank
pagerank = nx.pagerank(G)

# Visualize the network
plt.figure(figsize=(12, 12))
nx.draw(G, with_labels=True, node_size=50, font_size=10)
plt.title('Twitter Network Visualization')
plt.show()

# Print the analysis results
print(f"Number of strongly connected components: {len(strongly_connected)}")
print(f"PageRank of top users: {sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:5]}")
