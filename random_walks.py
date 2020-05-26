import matplotlib.pyplot as plt
from random import choice
import time as tm

class RandomWalk():
    """Class for generating random walks"""
    def __init__(self, num_points=5000):
        self.num_points = num_points
        
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # choicing direction
            # 1 - right / -1 -left
            x_direction = choice([1, -1])
            # random magnitude 0-4
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            #cancelling zeros movements
            if x_step == 0 and y_step == 0:
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
           
while True :
    t0 = tm.time()
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c=point_number, s=5,
                edgecolor='none', cmap=plt.cm.Blues)
    
    # estimate start and end points
    plt.scatter(0,0, c='red', edgecolor='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolor='none', s=50)
    plt.title("Random walks")
    plt.xlabel("x axis")
    plt.ylabel("y axis") 
    plt.figure(figsize=(10,6))
    plt.show()
    t1 =tm.time()
    # for 50,000 elements it takes 1.00 - 1.3 s
    # for 5,000 elements it takes about 0.21 - 0.28 s
    print(t1-t0)
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

