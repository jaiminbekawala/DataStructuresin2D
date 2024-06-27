from collections import deque
import matplotlib.pyplot as plt
#Find the minimun number between X,Y,Z
def min_of_list(numbers):
    return min(numbers)

def min_of_stack(stack):
    min_stack = float('inf')
    while stack:
        min_stack = min(min_stack, stack.pop())
    return min_stack
    
def min_of_queue(queue):
    min_queue = float('inf')
    while queue:
        min_queue = min(min_queue, queue.popleft())
    return min_queue

def main():
    X = float(input("Enter the first number (X): "))
    Y = float(input("Enter the second number (Y): "))
    Z = float(input("Enter the third number (Z): "))
    numbers = [X, Y, Z]

    
    min_list = min_of_list(numbers)
    stack = numbers[:]
    min_stack = min_of_stack(numbers)
    queue = deque(numbers)
    min_queue = min_of_queue(numbers)
    
    #Creating a circle using pyplot 
    figure, axes = plt.subplots()
    Drawing_uncolored_circle = plt.Circle( (0.5, 0.5 ), 0.3,fill = True )
    #Add number to the plot
    plt.text(0.5,0.5, float(min_stack),fontsize=20)
    axes.set_aspect( 1 )
    axes.add_artist( Drawing_uncolored_circle )
    plt.title( 'Circle' )
    #Remove axes for clear presentation
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
  main()