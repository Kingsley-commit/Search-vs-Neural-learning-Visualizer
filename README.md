<!-- centered logo + title -->

 # AI Search & Neural Network Simulator<br>


##  Overview

This project develops an interactive framework to demonstrate and compare two foundational AI
paradigms; uninformed search and neural learning through the simulation of basic Boolean
logic gates. Specifically, Breadth-First Search (BFS) and Depth-Limited Search (DLS) are
implemented and visualized on configurable graphs to evaluate their completeness, time
complexity, and memory consumption. A backpropagation-trained multilayer perceptron is built
to learn the AND, OR, and XOR functions, with real-time plots of training loss and decision
boundaries illustrating the network’s convergence behavior. <br><br>Both modules are integrated into a
cohesive Tkinter-based graphical user interface, enabling users to adjust parameters, observe
algorithmic steps, and compare empirical performance metrics at runtime. Experimental results
confirm that BFS guarantees optimal shallow solutions at the expense of exponential memory
growth, while DLS offers controlled resource use but may miss deeper solutions. <br><br>The neural
network reliably learns linearly separable functions (AND, OR) and captures the non-linear XOR
mapping given sufficient hidden units and epochs. This tool not only clarifies algorithmic tradeoffs—completeness versus resource constraints, exhaustive enumeration versus adaptive
learning—but also serves as a pedagogical aid for understanding AI techniques in both academic
and business contexts 

## Algorithm Design
The session provides complete algorithmic descriptions for the
developed methods: Breadth-First Search (BFS), Depth-Limited Search (DLS) and
Backpropagation Neural Network. The designs include flowchart which defines the structures
of data as well as the procedural logic of control. 

### 1. Breadth-First Search (BFS)
BFS visits nodes of a state-space graph in order from left to right and top to bottom. The algorithm
first visits all unvisited successor nodes at the starting point then spawns another level of nodes if
any remain. Using a FIFO queue as the frontier mechanism ensures the expansion of nodes based
on their ascending depth values. BFS delivers complete and optimal solutions when step costs are
uniform while consuming space and time in the order of bᵈ.<br> 
##### <i>Breadth First Search Algorithm Design</i>
![image](https://github.com/user-attachments/assets/21301a5b-b3fa-4807-81da-ee3b9c211314) <br>
##### <i>Breadth First Search flowchart diagram</i>
![image](https://github.com/user-attachments/assets/9cd8e3d6-e822-4e53-ac61-1f1b7f72e2e8) 

### 2. Depth-Limited Search (DLS)
The depth-first search implementation DLS auto-trims all search paths reaching more than depth
limit L. The algorithm maintains DFS's minimal memory requirements of O(b·L) but becomes
incomplete when the goal exists further than L.<br> 
##### <i>Depth-Limited Search Algorithm Design</i>
![image](https://github.com/user-attachments/assets/781a9895-2b6e-44d2-b5ab-605683f2024e) <br>
##### <i>Depth-Limited Search flowchart diagram</i>
![image](https://github.com/user-attachments/assets/47c942e5-6ebd-453d-8999-886f96b4b768)

### 3. Backpropagation Neural Network
The Backpropagation training method operates on a one-layer feedforward Multilayer Perceptron.
After applying forward propagation to compute layer output activations the algorithm performs
backpropagation to compute weight gradient values for stochastic gradient descent.<br> 
##### <i>A simple illustration of how the backpropagation works by adjustments of weights</i>
![image](https://github.com/user-attachments/assets/20e3382e-e3cc-4e03-a77b-f4f6c4ad3f0b) <br>
##### <i>Backpropagation Neural Network flowchart diagram</i>
![image](https://github.com/user-attachments/assets/ee252f93-4235-48f1-9268-c612a09876ee) <br>

##  User Flow and Interraction
![image](https://github.com/user-attachments/assets/7b9eee77-67aa-4586-b278-dd306016444f)

##  Highlights

- **Single GUI**, two modes: Search vs. Neural  
- **Live metrics**: nodes expanded, frontier size, runtime, training loss  
- **Adjustable**: start/goal nodes, depth limit, learning rate, epochs, hidden units  

##  Installation

1. **Clone**  
   ```bash
   git clone https://github.com/Kingsley-commit/Search-vs-Neural-learning-Visualizer.git
   cd Search-vs-Neural-learning-Visualizer
2. **Create & activate virtualenv (optional)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
3. **Install**
   ```bash
   pip install -r requirements.txt

##  Usage

### 1. Search Visualization

```bash
python main_search_gui.py
```

* Select **BFS** or **DLS**
* Enter **start**, **goal**, and (for DLS) **depth limit**
* Click **Run**—watch the graph explore!

---

### 2. Neural Network Training

```bash
python neural_gui.py
```

* Choose **AND**, **OR**, or **XOR**
* Set **learning rate**, **epochs**, **hidden units**
* Click **Train**—view loss curve & decision boundary live!

---

##  Project Layout

```
ai-search-neural-network/
├─ assets/            # logo.png, demo.gif
├─ search_algorithms/   
│   ├─ stack_queue.py
│   ├─ search_algorithms.py
│   └─ main_search_gui.py
├─ neural_network/
│   ├─ neural_network.py
│   └─ neural_gui.py
├─ requirements.txt
└─ README.md
```

##  Contributing

1. Fork this repo
2. Create a branch: `git checkout -b feature/MyFeature`
3. Commit: `git commit -m "Add MyFeature"`
4. Push: `git push origin feature/MyFeature`
5. Open a Pull Request


