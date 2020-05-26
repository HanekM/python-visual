import pygal
from random import randint

class Die():
    """Initialization"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        
    def roll(self):
        """Returns random number 1-6"""
        return randint(1, self.num_sides)

#Creating die d6   
die_1 = Die()
die_2 = Die()
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#for analysing results    
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#visualizing results with pygal
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
#hist.x_labels = ['2', '2', '3', '4', '5', '6', '7', '8',
#                 '9', '10', '11', '12']
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add('D6 + D6', frequencies)
hist.render_to_file("die_visual_two_dies.svg")


