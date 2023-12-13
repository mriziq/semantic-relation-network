See PDF for full write up.

# SEMANTIC RELATIONAL WEIGHT GENERATION SYSTEM
APPLICATIONS FOR CONTENT METADATA

Amer K. Mriziq
INFO 202 Information Organization and Retrieval
School of Information, UC Berkeley Fall 2023

## How to Use
- Install the requirements 
- Run the script `python3 main.py`
- Open the network html file found at `graph.html`

## How it Works
The implementation involves three key components:

1. Semantic Relational Graph: I created a function, `create_similarity_graph_and_distance_matrix`, to construct a network graph and a distance matrix. In this graph, nodes represent words, and edges connect words with a cosine similarity above 0.3. I transformed the edge weights from the -1 to 1 cosine similarity scale to a more interpretable 0-1 scale.

2. Hierarchical Cluster Diagram: Using the `create_hierarchical_cluster_network` function, I leveraged the distance matrix to create a dendrogram that visually represents word groupings based on semantic distances.

3. Network Visualization: With the `visualize_graph` function, I utilized Pyvis to generate an interactive network diagram, showcasing words and their transformed similarity scores.

## Hyperparameters

The similarity threshold is the hyperparameter in which the system operator can adjust. Adjusting the threshold significantly impacted the network's density. A lower threshold included more edges, leading to a denser graph, while a higher threshold resulted in a sparser, more manageable network. The transformation of similarity into relational weights posed a challenge. I needed to decide whether the network should represent only positive relations or encompass all relations, including negative ones. This system’s linear transformation and similarity threshold can be combined to change the underlying network to represent both positive and negative relationships. 


