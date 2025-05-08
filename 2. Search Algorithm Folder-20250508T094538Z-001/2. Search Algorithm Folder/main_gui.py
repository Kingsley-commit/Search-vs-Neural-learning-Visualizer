import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from collections import deque  
from search_algorithms import dls, bfs

G = nx.Graph()  

class SearchNode:  # not using this yet but might need it later
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def path_trace(node):
    path = []
    curr = node
    while curr:  # loop until we hit the start
        path.append(curr.state)
        curr = curr.parent
    path.reverse()  # flip it around to get start->goal order
    return path

def animate_path(path):
    traversal_text.delete('1.0', tk.END)
    # show the search happening step by step
    for i, curr_node in enumerate(path):
        ax.clear()
        # using fixed seed so graph doesn't jump around
        pos = nx.spring_layout(G, seed=42)  

        # draw the basic graph first
        nx.draw(G, pos, with_labels=True, 
                node_color='lightblue',  # nice neutral color
                edge_color='gray', node_size=600, 
                font_size=10, ax=ax)

        # show where we've been
        if i > 0:
            nx.draw_networkx_nodes(G, pos, 
                                 nodelist=path[:i], 
                                 node_color='lightblue',
                                 edgecolors='black', 
                                 linewidths=2, 
                                 node_size=1200, ax=ax)

        # highlight current node we're looking at
        nx.draw_networkx_nodes(G, pos, 
                             nodelist=[curr_node], 
                             node_color='orange',
                             edgecolors='black', 
                             linewidths=4, 
                             node_size=800, ax=ax)
        update_traversal_display(curr_node)
        canvas.draw()
        root.update()
        time.sleep(1)  # pause between steps - might make this configurable

def get_user_input(prompt, expect_number=False):
    # helper for getting input from user
    popup = tk.Toplevel()
    popup.title(prompt)
    tk.Label(popup, text=prompt).pack(pady=10)
    entry = tk.Entry(popup)
    entry.pack(pady=5)
    result = []  # using list to store result (tkinter callback limitation)
    
    def on_submit():
        val = entry.get()
        if expect_number:
            try:
                val = int(val)
            except ValueError:
                val = None
        result.append(val)
        popup.destroy()
    
    tk.Button(popup, text="OK", command=on_submit).pack(pady=10)
    popup.grab_set()  # make popup modal
    root.wait_window(popup)
    return result[0] if result else None

def run_search():
    # get start and end nodes from user
    
    start = get_user_input("Starting node:")
    end = get_user_input("Goal node:")
    if not start or not end:
        print("Need both start and end nodes!")
        return

    if start not in G.nodes or end not in G.nodes:
        print("Those nodes aren't in the graph!")
        return

    # figure out which algorithm to use
    algo = algorithm_var.get()
    if algo == "Depth-Limited Search":
        # need depth limit for DLS
        depth = get_user_input("Max depth:", expect_number=True)
        if depth is None:
            print("Need a valid depth limit!")
            return
        result = dls(G, start, end, int(depth))
    else:  # must be BFS
        result = bfs(G, start, end)
    if result:
        print(f"Found path: {result}")
        animate_path(result)
    else:
        print("Couldn't find a path :(")
    
    

def add_new_node():
    # grab node name and add to graph
    node = node_entry.get().strip()
    if node:  # make sure we got something
        G.add_node(node)
        update_graph()
        node_entry.delete(0, tk.END)

def add_new_edge():
    edge = edge_entry.get().strip()
    if edge:
        try:
            # expect format like "A,B" or "A, B"
            n1, n2 = edge.split(',')
            n1, n2 = n1.strip(), n2.strip()
            G.add_edge(n1, n2)
            update_graph()
            edge_entry.delete(0, tk.END)
        except ValueError:
            print("Edge should be 'NodeA,NodeB'")

def update_graph():
    # redraw the graph
    ax.clear()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, 
            node_color='lightblue', 
            edge_color='gray',
            node_size=1200, 
            font_size=15, ax=ax)
    canvas.draw()

def update_traversal_display(visited_node):
    traversal_text.insert(tk.END, f"{visited_node}\n")
    traversal_text.see(tk.END) 

# Main window setup
root = tk.Tk()
root.title("Graph Search Visualizer")
root.geometry("1000x700")  # decent size for most screens

# Setup frames
input_frame = tk.Frame(root)
input_frame.pack(side=tk.TOP, pady=20)

graph_frame = tk.Frame(root)
graph_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

traversal_frame = tk.Frame(root)
traversal_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

tk.Label(traversal_frame, text="Traversal Path", font=('Arial', 12)).pack(pady=5)

traversal_text = tk.Text(traversal_frame, height=20, width=30, font=('Arial', 12))
traversal_text.pack(pady=5)

# Node input
tk.Label(input_frame, text="Node:").grid(row=0, column=0, padx=5)
node_entry = tk.Entry(input_frame)
node_entry.grid(row=0, column=1, padx=5)

# Edge input
tk.Label(input_frame, text="Edge (A,B):").grid(row=0, column=2, padx=5)
edge_entry = tk.Entry(input_frame)
edge_entry.grid(row=0, column=3, padx=5)

# Algorithm dropdown
tk.Label(input_frame, text="Search:").grid(row=0, column=4, padx=5)
algorithm_var = tk.StringVar()
algo_dropdown = ttk.Combobox(input_frame, textvariable=algorithm_var)
algo_dropdown['values'] = ("Depth-Limited Search", "Breadth-First Search")
algo_dropdown.grid(row=0, column=5, padx=5)
algo_dropdown.current(0)  # default to DLS

# Setup matplotlib
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Buttons
tk.Button(input_frame, text="Add Node", command=add_new_node).grid(
    row=1, column=0, columnspan=2, pady=10)
tk.Button(input_frame, text="Add Edge", command=add_new_edge).grid(
    row=1, column=2, columnspan=2, pady=10)
tk.Button(input_frame, text="Start Search", command=run_search).grid(
    row=1, column=4, columnspan=2, pady=10)


root.mainloop()