from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
def map_world():
    world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
    map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
    room_graph=literal_eval(open(map_file, "r").read())
    world.load_graph(room_graph)

# Print an ASCII map
    world.print_rooms()

    player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
    traversal_path = []
    directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    path = []
    rooms_visited = {}

    rooms_visited[player.current_room.id] = player.current_room.get_exits()    

    while len(rooms_visited) < len(room_graph) -1:              
        
        if player.current_room.id not in rooms_visited:
            rooms_visited[player.current_room.id] = player.current_room.get_exits()
            random.shuffle(rooms_visited[player.current_room.id])
            last_direction = path[-1]
            rooms_visited[player.current_room.id].remove(last_direction)
        
        while len(rooms_visited[player.current_room.id]) < 1:
            last_direction = path.pop()
            traversal_path.append(last_direction)
            player.travel(last_direction)

        move_direction = rooms_visited[player.current_room.id].pop(0)
        traversal_path.append(move_direction)
        path.append(directions[move_direction])
        player.travel(move_direction)
        
        print('path', path)
        print(f"traversal {traversal_path}")



# TRAVERSAL TEST
    visited_rooms = set()
    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)

    for move in traversal_path:
        player.travel(move)
        visited_rooms.add(player.current_room)

    if len(visited_rooms) == len(room_graph):
        print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    else:
        print("TESTS FAILED: INCOMPLETE TRAVERSAL")
        print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


map_world()
#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
