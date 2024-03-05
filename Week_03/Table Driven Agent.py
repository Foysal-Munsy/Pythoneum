# Store the agent fucntion as a table
table={('A','Clean'):'Go Right',
       ('A','Dirty'):'Remove Dirt',
       ('B','Clean'):'Go Left',
       ('B','Dirty'):'Remove Dirt'}

percepts = [] #to store percept history
def table_driven_agent(percept):
    print('Perception Received: ' + str(percept))
    percepts.append(percept) # updating percept history
    action = table[percept]
    return action

#lets simulate it
import random  #it can generaten random numbers

#simulating the first perception randomly
Location = random.choice(['A','B'])
Condition = random.choice(['Clean','Dirty'])

while True:
    action = table_driven_agent((Location,Condition))
    print('Action Performed: '+ action)

#user control to allow next perception
    cmd = input('Type b to exit! or any key to continue.')
    if(cmd == 'b'):break

# simulating the next perception
# if the prev= "Go Right" then next loc = B is obvious
if action == 'Go Right':
    Location = 'B'
    Condition = random.choice(['Clean','Dirty'])
# if prev = 'Go Left' then next loc = 'A' is obvious
elif action == 'Go Left':
    Location = 'A'
    Condition = random.choice(['Clean','Dirty'])
# if the prev = 'Remove Dirt' then next loc = remains same
# and status = Clean is obvious
else:
    Condition = 'Clean'