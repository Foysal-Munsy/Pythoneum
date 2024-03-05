
def simple_reflex_agnt(percept):
    print('Received: '+ str(percept))
    location = percept[0]
    status = percept[1]
    if status == 'Foul':
        action = 'Red Card'
    elif location == 'A':
        action = 'Right Foot'
    elif location == 'B':
        action = 'Left Foot'
    return action

import random

Location = random.choice(['A','B'])
Condition = random.choice(['Foul','Dirty'])

while True:
    action = simple_reflex_agnt((Location,Condition))
    print('Perfomed: '+ action)
    user_input = input('Whitsle or type b for exit the football match! or any key to continue extra time.')
    if(user_input == 'b'): break
    if action == 'Right Foot':
        Location = 'B'
        Condition = random.choice(['Foul','Goal'])
    elif action == 'Left Foot':
        Location = 'A'
    else:
        Condition = 'Foul'

