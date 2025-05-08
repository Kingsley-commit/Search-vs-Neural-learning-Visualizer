from stack_queue import Stack, Queue  # my custom implementations
import time

def dls(graph, root, goal, limit):
    start_time = time.time()
    # keep track of nodes we visit
    path = []
    seen = set()  
    
    # need two stacks - one for nodes and one for depths
    nodes = Stack(100)  # should be enough for most cases
    depths = Stack(100)
    
    # start from root node
    nodes.push(root)
    depths.push(0)
    
    while not nodes.is_empty():  # while we still have nodes to explore
        current = nodes.pop()
        current_depth = depths.pop()
        
        if current in seen:
            continue  # skip if we've been here
            
        # debugging help
        print(f"Visiting Node: {current} (Depth: {current_depth})")
        path.append(current)
        seen.add(current)
        
        if current == goal:  # found it!
            break
        
        # only go deeper if we haven't hit the limit
        if current_depth == limit and current != goal:
            print("Goal not within limit")
        elif current_depth < limit:
            # reversed so we explore right-to-left
            # might change this later if needed
            for next_node in sorted(graph.neighbors(current), reverse=True):
                if next_node not in seen:
                    nodes.push(next_node)
                    depths.push(current_depth + 1)

        
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.9f} seconds")
    return path


def bfs(graph, root, goal):
    start_time = time.time()
    # similar to DLS but using a queue instead
    path = []
    seen = set()
    
    # just need one queue for BFS
    queue = Queue(100)  # same size as DLS for consistency
    queue.enqueue(root)
    
    while not queue.is_empty():
        current = queue.dequeue()
        if current in seen:
            continue
            
        print(f"Visiting Node: {current}")  # for debugging
        path.append(current)
        seen.add(current)
        
        if current == goal:
            break  # found what we're looking for
            
        # explore neighbors in sorted order
        # makes output more predictable
        for next_node in sorted(graph.neighbors(current)):
            if next_node not in seen:
                queue.enqueue(next_node)
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.9f} seconds")
    return path