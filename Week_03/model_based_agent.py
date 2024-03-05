world_map = {'A':'Unknown','B':'Unknown'}

def update_map(action,percept,model):
    location = percept[0]
    status = percept[1]

    model[location] = status

    if action == 'Remove Dirt':
        model[location] = 'Clean'
    return model

def model_reflex_agent(percept):
    location = percept[0]
    status = percept[1]
    global world_map
    if world_map['A'] == 'Clean' and world_map['B']=='Clean':
        action = 'Pause'
        return action
    elif status == 'Dirty':
        action = 'Remove Dirt'
    elif location == 'A':
        action = 'Go Right'
    elif location == 'B':
        action = 'Go Left'

    world_map = update_map(action , percept , world_map)
    print('Perception: '+str(percept))
    print('Action Performed: '+ action)
    print('World Map: '+str(world_map))
    return action    

import random
Location = random.choice(['A','B'])
Condition = random.choice(['Clean','Dirty'])

while True:
    print('-----000-----')
    action = model_reflex_agent((Location,Condition))
    if action == 'Go Right':
        Location = 'B'
        Condition = random.choice(['Clean','Dirty'])
    elif action == 'Go Left':
        Location = 'A'
        Condition = random.choice(['Clean','Dirty'])
    elif action == 'Remove Dirt':
        Condition = 'Clean'
    elif action == 'Pause':
        user_input = input('Type b to exit! or any key to continue.')
        if(user_input == 'b'):break
        Location =  random.choice(['A','B'])
        Condition = random.choice(['Clean','Dirty'])
        world_map = {'A':'Unknown', 'B':'Unknown'}
