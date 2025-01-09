import networkx as nx
import matplotlib.pyplot as plt

def get_distance(source, destination):
    # Loop through connections to find the matching pair
    for city1, city2, distance in connections:
        if (source == city1 and destination == city2) or (source == city2 and destination == city1):
            return distance
    return None  # No distance found

# Create a graph
city_network = nx.Graph()

# Add cities (nodes) with population as a node attribute
cities = {
    "Peshawar": 500000,  # Population in thousands
    "Karachi": 1200000,
    "Islamabad": 800000,
    "Lahore": 600000,
    "Quetta": 1500000,
    "Multan": 200000,
    "Sargodah": 300000,
    "Sakardu": 400000,
    "Sukhur": 230000,
    "Mardan": 320000,
    "Chikdara": 43000,
    "Abbotabad": 230000,
    "Lasbela": 400000,
    "Gawadar": 250000,
    "Lower Dir": 300000,
    "Chitral": 600000,
    "Hyderabad": 700000,
    "Bahawalpur": 500000,
    "Rawalpindi": 950000,
    "Faisalabad": 1100000,
    "Dera Ismail Khan": 220000,
}
    
for city, population in cities.items():
    city_network.add_node(city, population=population)

# Add connections (edges) with distance as an edge attribute
connections = [
    ("Peshawar", "Lahore", 200),       # Distance in km
    ("Lahore", "Karachi", 150),
    ("Karachi", "Islamabad", 300),
    ("Islamabad", "Quetta", 400),
    ("Quetta", "Peshawar", 100),
    ("Lahore", "Faisalabad", 50),
    ("Peshawar", "Mardan", 70),
    ("Islamabad", "Abbottabad", 120),
    ("Karachi", "Hyderabad", 160),
    ("Chitral", "Lower Dir", 150),
    ("Hyderabad", "Bahawalpur", 250),
    ("Rawalpindi", "Lahore", 250),
    ("Multan", "Sargodah", 180),
    ("Lasbela", "Gawadar", 190),
    ("Quetta", "Lasbela", 80),
    ("Sukhur", "Karachi", 400),
    ("Dera Ismail Khan", "Rawalpindi", 300),
    ("Chitral", "Abbottabad", 340),
    ("Lower Dir", "Mardan", 110),
    ("Faisalabad", "Multan", 220),
    ("Bahawalpur", "Sargodah", 200),
    ("Islamabad", "Chikdara", 290),
    ("Mardan", "Chitral", 280),
    ("Quetta", "Gawadar", 240),
    ("Hyderabad", "Sukhur", 180),
    ("Lahore", "Rawalpindi", 270),
    ("Gawadar", "Karachi", 320),
    ("Multan", "Bahawalpur", 90),
    ("Sargodah", "Rawalpindi", 140),
    ("Abbotabad","Chikdara", 120),
    ("Abbotabad", "Sakardu", 230),
]

for city1, city2, distance in connections:
    city_network.add_edge(city1, city2, distance=distance)

# Ensure all nodes have a population attribute
for node in city_network.nodes:
    if "population" not in city_network.nodes[node]:
        city_network.nodes[node]["population"] = 0  # Default population value

# Draw the graph with populations as labels
pos = nx.spring_layout(city_network, seed=42)  # Generate positions for nodes
node_sizes = [city_network.nodes[city]["population"] / 1000 for city in city_network.nodes]  # Scale node size

# Plot the graph
fig, ax = plt.subplots(figsize=(10, 8))
nx.draw(
    city_network,
    pos,
    with_labels=True,
    node_size=node_sizes,
    node_color="lightblue",
    edge_color="gray",
    font_size=10,
    font_weight="bold",
    ax=ax,
)

# Add edge labels (distances)
edge_labels = nx.get_edge_attributes(city_network, "distance")
nx.draw_networkx_edge_labels(city_network, pos, edge_labels=edge_labels)

plt.title("City Network with Populations and Distances")
plt.show()

# Input for source and destination cities
source = input("Enter source city: ")
destination = input("Enter destination city: ")

if source not in city_network.nodes or destination not in city_network.nodes:
    print("one are more node not present in the list")
else:
    return 
# Get the distance between the cities
distance = get_distance(source, destination)

# Display the result
if distance is not None:
    print(f"The distance between {source} and {destination} is {distance} km.")
else:
    print(f"No distance information available between {source} and {destination}.")
