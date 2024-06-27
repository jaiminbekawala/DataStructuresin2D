import turtle
from collections import deque, defaultdict

def find_smallest_list(numbers):
    return min(numbers)

def find_smallest_stack(stack):
    smallest = float('inf')
    while stack:
        smallest = min(smallest, stack.pop())
    return smallest

def find_smallest_queue(queue):
    smallest = float('inf')
    while queue:
        smallest = min(smallest, queue.popleft())
    return smallest

class TreeNode:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

def find_smallest_bst(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.value

class Graph:
    def _init_(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_smallest_graph(self):
        smallest = float('inf')
        for node in self.graph:
            smallest = min(smallest, node)
            for neighbor in self.graph[node]:
                smallest = min(smallest, neighbor)
        return smallest

def draw_rectangle_with_text(smallest_number):
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.title("Smallest Number Visualization")
    
    # Set up the turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(1)
    
    # Draw a rectangle
    pen.penup()
    pen.goto(-100, 50)
    pen.pendown()
    pen.forward(200)  # Width
    pen.right(90)
    pen.forward(100)  # Height
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(100)
    
    # Display the smallest number
    pen.penup()
    pen.goto(0, 0)
    pen.write(f"Min (List): {smallest_number}", align="center", font=("Arial", 16, "normal"))
    
    # Keep the window open until clicked
    screen.exitonclick()

def main():
    X = float(input("Enter the first number (X): "))
    Y = float(input("Enter the second number (Y): "))
    Z = float(input("Enter the third number (Z): "))
    numbers = [X, Y, Z]

    smallest_list = find_smallest_list(numbers)

    stack = numbers[:]
    smallest_stack = find_smallest_stack(stack)

    queue = deque(numbers)
    smallest_queue = find_smallest_queue(queue)

    bst_root = None
    for number in numbers:
        bst_root = insert_bst(bst_root, number)
    smallest_bst = find_smallest_bst(bst_root)

    graph = Graph()
    for i in range(len(numbers) - 1):
        graph.add_edge(numbers[i], numbers[i + 1])
    smallest_graph = graph.find_smallest_graph()

    
    draw_rectangle_with_text(smallest_list)

if __name__ == "__main__":
    main()