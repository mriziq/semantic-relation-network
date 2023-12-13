import gensim.downloader as api
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import dendrogram, linkage

def create_similarity_graph_and_distance_matrix(words, model, threshold):
    graph = nx.Graph()
    distances = []  # List to store distances

    # Add nodes
    for word in words:
        graph.add_node(word)

    # Calculate pairwise similarity and add edges
    for i in range(len(words)):
        row = []
        for j in range(len(words)):
            if i == j:
                # Distance to itself is 0
                row.append(0)
                continue

            word1 = words[i]
            word2 = words[j]
            similarity = model.similarity(word1, word2) if word1 in model and word2 in model else 0
            transformed_similarity = (similarity + 1) / 2
            distance = 1 - similarity  # Convert similarity to distance
            row.append(distance)
            
            if i < j and similarity > threshold:  # Avoid duplicate edges and ensure threshold
                # Add an edge with transformed similarity as weight
                graph.add_edge(word1, word2, weight=transformed_similarity)

        distances.append(row)
    
    # Convert the distances list to a symmetric matrix
    distance_matrix = squareform(distances)
    return graph, distance_matrix

# Generate a Network diagram of Similarity Graph
def visualize_graph(graph):
    """
    Visualize a graph using Pyvis.

    :param graph: A networkx graph object
    """
    # Create a Pyvis network
    net = Network(notebook=True, height="750px", width="100%")

    # Add nodes and edges from the networkx graph
    for node, node_attrs in graph.nodes(data=True):
        net.add_node(node, label=node, title=str(node))

    for source, target, edge_attrs in graph.edges(data=True):
        weight = edge_attrs.get("weight", 0)  # default weight to 0 if not specified
        # Convert weight to Python native float for JSON serialization
        weight = float(weight)
        title = f"{source} - {target}: {weight:.2f}"
        net.add_edge(source, target, title=title, value=weight)

    net.toggle_physics(False)
    # Show the graph
    net.show("graph.html")

# Create a Hierarchical cluster network
def create_hierarchical_cluster_network(words, distance_matrix):
    Z = linkage(squareform(distance_matrix), 'ward')

    plt.figure(figsize=(10, 8))
    dendrogram(Z, labels=words)
    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("Words")
    plt.ylabel("Distance")
    plt.show()


# Load model
word2vec_model = api.load("word2vec-google-news-300")

# Ask user for input
input_string = input("Enter comma-separated words: ")
words = [word.strip() for word in input_string.split(",")]
input_threshold = float(input("Set the similarity threshold (e.g., 0.3): "))

# Create graph and distance matrix
similarity_graph, distance_matrix = create_similarity_graph_and_distance_matrix(words, word2vec_model, input_threshold)

print(similarity_graph)
print(distance_matrix)

# Call the function with the created graph
visualize_graph(similarity_graph)

# Create and display hierarchical cluster network
create_hierarchical_cluster_network(words, distance_matrix)