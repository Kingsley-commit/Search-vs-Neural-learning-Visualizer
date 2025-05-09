<!-- centered logo + title -->
<p align="center">
  <br />
  <strong><big>AI Search & Neural Network Simulator</big></strong>
  <br />
</p>

## 🚀 Overview

**AI Search & Neural Network Simulator** is a Python desktop app that lets you:

- **Visualize** classic graph-search:  
  - Breadth-First Search (BFS)  
  - Depth-Limited Search (DLS)
- **Train** a simple backpropagation neural network on logic gates (AND, OR, XOR)
- **Interact** with real-time animations, loss curves, and decision boundaries

<p align="center">
  <img src="assets/demo.gif" alt="Demo" width="600" />
</p>

## ✨ Highlights

- **Single GUI**, two modes: Search vs. Neural  
- **Live metrics**: nodes expanded, frontier size, runtime, training loss  
- **Adjustable**: start/goal nodes, depth limit, learning rate, epochs, hidden units  

## 🛠️ Installation

1. **Clone**  
   ```bash
   git clone https://github.com/yourusername/ai-search-neural-network.git
   cd ai-search-neural-network
2. **Create & activate virtualenv (optional)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
3. **Install**
   ```bash
   pip install -r requirements.txt

## ▶️ Usage

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

## 📂 Project Layout

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

## 🤝 Contributing

1. Fork this repo
2. Create a branch: `git checkout -b feature/MyFeature`
3. Commit: `git commit -m "Add MyFeature"`
4. Push: `git push origin feature/MyFeature`
5. Open a Pull Request

Released under the **MIT License**. See [LICENSE](LICENSE).

> Made with ❤️ for teaching AI fundamentals

