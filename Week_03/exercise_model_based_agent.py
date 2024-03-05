# Description for the implementation
""" # Agent Description: The aim of the agent is to simulate a football match. 
# It receives perceptions about the location and condition of the game 
# (whether a goal was scored or a foul was committed), and based on these perceptions, 
# it performs actions such as scoring a goal with the right or left foot, or giving a red card for a foul.
 """
# Sensors: The agent has two sensors:
# Location Sensor: Detects the current location of the game (either 'A' or 'B').
# Condition Sensor: Detects the current condition of the game (either 'Goal' or 'Fouls').
# Sensor Values: The sensor values can be:
# Location Sensor Values: 'A' or 'B'.
# Condition Sensor Values: 'Goal' or 'Fouls'.
# Actions: The agent can perform the following actions:
# 'Right Foot Goal'
# 'Left Foot Goal'
# 'Red Card'

""" Agent Function: The agent function maps the perceptual history to an action. 
    In this case, the agent function is implemented as a table lookup (the table dictionary). 
    The agent receives a perception (a tuple of location and condition), appends it to the perceptual 
    history (percepts list), and then looks up the corresponding action in the table. 
    The chosen action is then returned by the function. """
######
table={('A','Goal'):'Right Foot Goal',
       ('A','Fouls'):'Red Card',
       ('B','Goal'):'Left Foot Goal',
       ('B','Fouls'):'Red Card'}

percepts = [] 
def table_driven_agent(percept):
    print('Perception Received: ' + str(percept))
    percepts.append(percept) 
    action = table[percept]
    return action

import random  #it can generaten random numbers

Location = random.choice(['A','B'])
Condition = random.choice(['Goal','Fouls'])

while True:
    action = table_driven_agent((Location,Condition))
    print('Action Performed: '+ action)

    cmd = input('Whitsle or type b for exit the football match! or any key to continue extra time.')
    if(cmd == 'b'):break

# simulating the next perception
# if the prev= "Right Foot Goal" then next loc = B is obvious
if action == 'Right Foot Goal':
    Location = 'B'
    Condition = random.choice(['Goal','Fouls'])
# if prev = 'Left Foot Goal' then next loc = 'A' is obvious
elif action == 'Left Foot Goal':
    Location = 'A'
    Condition = random.choice(['Goal','Fouls'])
# if the prev = 'Red Card' then next loc = remains same
# and status = Goal is obvious
else:
    Condition = 'Goal'