import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

class NeuralNetworkGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Group 5: Implementation of Backpropagation Neural Network")
        self.root.geometry("900x700")
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.tab_control = ttk.Frame(self.notebook)
        self.tab_visualization = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_control, text="Control Panel")
        self.notebook.add(self.tab_visualization, text="Visualization")
        
        # Control Panel Tab
        self.setup_control_panel()
        
        # Visualization Tab
        self.setup_visualization_panel()
        
        # Initialize network
        self.nn = None
        self.losses = []
        self.current_gate = None
        
    def setup_control_panel(self):
        # Gate selection
        gate_frame = ttk.LabelFrame(self.tab_control, text="Logic Gate Selection", padding=10)
        gate_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.gate_var = tk.StringVar(value="AND")
        ttk.Radiobutton(gate_frame, text="AND", variable=self.gate_var, value="AND").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(gate_frame, text="OR", variable=self.gate_var, value="OR").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(gate_frame, text="XOR", variable=self.gate_var, value="XOR").pack(side=tk.LEFT, padx=5)
        
        # Network configuration
        config_frame = ttk.LabelFrame(self.tab_control, text="Network Configuration", padding=10)
        config_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(config_frame, text="Hidden Layer Size:").grid(row=0, column=0, sticky=tk.W)
        self.hidden_size = tk.IntVar(value=4)
        ttk.Entry(config_frame, textvariable=self.hidden_size, width=5).grid(row=0, column=1, sticky=tk.W)
        
        ttk.Label(config_frame, text="Learning Rate:").grid(row=1, column=0, sticky=tk.W)
        self.learning_rate = tk.DoubleVar(value=0.1)
        ttk.Entry(config_frame, textvariable=self.learning_rate, width=5).grid(row=1, column=1, sticky=tk.W)
        
        ttk.Label(config_frame, text="Epochs:").grid(row=2, column=0, sticky=tk.W)
        self.epochs = tk.IntVar(value=10000)
        ttk.Entry(config_frame, textvariable=self.epochs, width=5).grid(row=2, column=1, sticky=tk.W)
        
        # Training controls
        train_frame = ttk.LabelFrame(self.tab_control, text="Training", padding=10)
        train_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(train_frame, text="Train Network", command=self.train_network).pack(side=tk.LEFT, padx=5)
        ttk.Button(train_frame, text="Test Network", command=self.test_network).pack(side=tk.LEFT, padx=5)
        
        # Results display
        result_frame = ttk.LabelFrame(self.tab_control, text="Results", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.result_text = tk.Text(result_frame, height=10, wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.configure(yscrollcommand=scrollbar.set)
    
    def setup_visualization_panel(self):
        # Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(8, 5))
        self.ax.set_title("Training Loss Over Epochs")
        self.ax.set_xlabel("Epoch")
        self.ax.set_ylabel("Loss")
        self.ax.grid(True)
        
        # Canvas for embedding matplotlib in Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab_visualization)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Decision boundary plot
        self.fig2, self.ax2 = plt.subplots(figsize=(6, 6))
        self.ax2.set_title("Decision Boundary")
        self.ax2.set_xlabel("Input 1")
        self.ax2.set_ylabel("Input 2")
        self.ax2.set_xlim(-0.5, 1.5)
        self.ax2.set_ylim(-0.5, 1.5)
        
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.tab_visualization)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def train_network(self):
        # Get selected gate
        gate = self.gate_var.get()
        self.current_gate = gate
        
        # Define input and output
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        
        if gate == "AND":
            y = np.array([[0], [0], [0], [1]])
        elif gate == "OR":
            y = np.array([[0], [1], [1], [1]])
        elif gate == "XOR":
            y = np.array([[0], [1], [1], [0]])
        
        # Initialize network
        input_size = 2
        hidden_size = self.hidden_size.get()
        output_size = 1
        learning_rate = self.learning_rate.get()
        epochs = self.epochs.get()
        
        self.nn = NeuralNetwork(input_size, hidden_size, output_size)
        
        # Train network
        self.result_text.insert(tk.END, f"Training {gate} gate network...\n")
        self.result_text.see(tk.END)
        self.root.update()
        
        self.losses = self.nn.train(X, y, epochs, learning_rate)
        
        self.result_text.insert(tk.END, f"Training completed for {gate} gate!\n")
        self.result_text.see(tk.END)
        
        # Update visualization
        self.update_plots()
    
    def test_network(self):
        if self.nn is None:
            messagebox.showerror("Error", "Please train the network first!")
            return
        
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        predictions = self.nn.predict(X)
        
        start = time.perf_counter()
        elapsed_microseconds = (time.perf_counter() - start) * 1_000_000
        
        self.result_text.insert(tk.END, f"\nTesting {self.current_gate} gate:\n")
        for i, (input_pair, prediction) in enumerate(zip(X, predictions)):
            self.result_text.insert(tk.END, f"Input: {input_pair} -> Output: {prediction[0]}\n")
        self.result_text.insert(tk.END, f"\nTesting completed in {elapsed_microseconds:.2f} micro seconds\n")
        self.result_text.see(tk.END)

        # Update decision boundary
        self.plot_decision_boundary()
    
    def update_plots(self):
        # Clear previous plot
        self.ax.clear()
        
        # Plot losses
        self.ax.plot(self.losses, label=f'{self.current_gate} Gate')
        self.ax.set_title("Training Loss Over Epochs")
        self.ax.set_xlabel("Epoch")
        self.ax.set_ylabel("Loss")
        self.ax.legend()
        self.ax.grid(True)
        
        # Redraw canvas
        self.canvas.draw()
    
    def plot_decision_boundary(self):
        if self.nn is None:
            return
            
        self.ax2.clear()
        
        # Create a grid of points
        x_min, x_max = -0.5, 1.5
        y_min, y_max = -0.5, 1.5
        h = 0.01
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        
        # Predict for each point in the grid
        Z = self.nn.forward(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        
        # Plot decision boundary
        self.ax2.contourf(xx, yy, Z, levels=[0, 0.5, 1], cmap=plt.cm.Paired, alpha=0.8)
        
        # Plot training points
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        if self.current_gate == "AND":
            y = np.array([0, 0, 0, 1])
        elif self.current_gate == "OR":
            y = np.array([0, 1, 1, 1])
        elif self.current_gate == "XOR":
            y = np.array([0, 1, 1, 0])
        
        self.ax2.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap=plt.cm.Paired, edgecolors='k')
        
        self.ax2.set_title(f"{self.current_gate} Gate Decision Boundary")
        self.ax2.set_xlabel("Input 1")
        self.ax2.set_ylabel("Input 2")
        self.ax2.set_xlim(-0.5, 1.5)
        self.ax2.set_ylim(-0.5, 1.5)
        
        self.canvas2.draw()

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with random values
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.weights2 = np.random.randn(hidden_size, output_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.bias2 = np.zeros((1, output_size))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        # Forward propagation
        self.hidden = self.sigmoid(np.dot(X, self.weights1) + self.bias1)
        self.output = self.sigmoid(np.dot(self.hidden, self.weights2) + self.bias2)
        return self.output
    
    def backward(self, X, y, output, learning_rate):
        # Backward propagation
        error = y - output
        d_output = error * self.sigmoid_derivative(output)
        
        error_hidden = d_output.dot(self.weights2.T)
        d_hidden = error_hidden * self.sigmoid_derivative(self.hidden)
        
        # Update weights and biases
        self.weights2 += self.hidden.T.dot(d_output) * learning_rate
        self.bias2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
        self.weights1 += X.T.dot(d_hidden) * learning_rate
        self.bias1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate
    
    def train(self, X, y, epochs, learning_rate):
        losses = []
        for i in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output, learning_rate)
            loss = np.mean(np.square(y - output))
            losses.append(loss)
        return losses
    
    def predict(self, X):
        return np.round(self.forward(X))

if __name__ == "__main__":
    root = tk.Tk()
    app = NeuralNetworkGUI(root)
    root.mainloop()