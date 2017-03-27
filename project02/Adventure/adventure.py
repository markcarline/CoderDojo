import random

#get players name
name = input('Welcome Adventurer - What is your name? ')

#if there is info on a room, display that, if not, just the name.. using msg at mo to test, but will
#change to description
def msg(room):
    if room['msg'] == '': # there is no custom msg
        return "You have entered the " + room['name'] + ' - '
    else:
        return room['msg']

def get_dir(room, dir):
    if dir =='N':
        choice = 0
    elif dir =='E':
        choice = 1
    elif dir =='S':
        choice = 2
    elif dir =='W':
        choice = 3
    else:
        return -1

    if room['directions'][choice] == 0:
        return 4
    else:
        return choice

#set dirs to all the zeros 0
dirs = (0, 0, 0, 0)

#dictionary of each room
entrance = {'name':'Entrance', 'description':'You have entered the entrance', 'directions':dirs, 'msg':''}
hallway = {'name':'Hallway', 'description':'You have entered the hallway', 'directions':dirs, 'msg':''}
livingroom = {'name':'Living Room', 'description':'You have entered the living room', 'directions':dirs, 'msg':''}
familyroom = {'name':'Family Room', 'description':'You have entered the family room', 'directions':dirs, 'msg':''}
kitchen = {'name':'Kitchen', 'description':'You have entered  the kitchen', 'directions':dirs, 'msg':''}
diningroom = {'name':'Dining Room', 'description':'You have entered the dining room', 'directions':dirs, 'msg':''}

#directions are tuples: rooms to the N, E, S, W
entrance['directions'] = (hallway, livingroom, 0, 0)
hallway['directions'] = (0, familyroom, entrance, kitchen)
livingroom['directions'] = (familyroom, 0, 0, entrance)
familyroom['directions'] = (0, 0, livingroom, hallway)
kitchen['directions'] = (0, hallway, 0, diningroom)
diningroom['directions'] = (0, kitchen, 0, 0)

#find the treasure map
rooms = [hallway, livingroom, kitchen, diningroom, familyroom]
room_with_map = random.choice(rooms)
room = entrance
got_map = False
print('Hello ' + name + ', can you find the treasure map?')

in_play = True
while in_play == True:
    if room == room_with_map:
        print('Well done, you have found the treasure map - You will be rich beyond your wildest dreams!!')
        in_play = False
        break
    else:
        print(msg(room))

    stopped = True
    while stopped == True:
        dir = input("Which way do you want to go: N, E, S, or W? ")
        choice = get_dir(room, dir)
        if choice == -1:
            print('Please enter N, E, S or W?')
        elif choice == 4:
            print('You cannot go in that direction.')
        else:
            room = room['directions'][choice]
            stopped = False
    

