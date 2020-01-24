from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

def run_code():

    # Load world
    world = World()


    # You may uncomment the smaller graphs for development and testing purposes.
    # map_file = "maps/test_line.txt"
    # map_file = "maps/test_cross.txt"
    map_file = "maps/test_loop.txt"
    # map_file = "maps/test_loop_fork.txt"
    #map_file = "maps/main_maze.txt"

    # Loads the map into a dictionary
    room_graph=literal_eval(open(map_file, "r").read())
    world.load_graph(room_graph)

    # Print an ASCII map
    world.print_rooms()

    player = Player(world.starting_room)

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
        
        
        

    # def bfs(dictionary, room):
    #     visited = set()
    #     queue = Queue()
    #     path = [room]
    #     queue.enqueue([room])
        
    #     while queue.size() > 0:
    #         room_id = queue.dequeue()
    #         rooms_entered = room_id[0]

    #         if rooms_entered == '?':
    #             path = room_id[1:]
    #             break

    #         if rooms_entered not in visited:
    #             visited.add(rooms_entered)
    #             for e in dictionary[rooms_entered]:
    #                 node = dictionary[rooms_entered][e]
    #                 new_path = list(path)
    #                 new_path.append(node)
    #                 queue.enqueue(new_path)

    #     directions = []

    #     while len(path) > 1:
    #         location = path.pop()
    #         for route in dictionary[location]:
    #             if dictionary[location][route] == path[-1]:
    #                 directions.append(route)
    #     return directions

    # def other_way(d):
    #     if d == 'e':
    #         return 'w'
    #     elif d == 'w':
    #         return 'e'
    #     elif d == 's':
    #         return 'n'
    #     elif d == 'n':
    #         return 's'


    # Fill this out with directions to walk
    # traversal_path = ['n', 'n']
   
    # visited = {}
    # count = 0

    # while len(visited) < len(room_graph):
    #     room = player.current_room.id

    #     if room not in visited:
    #         visited[room] = {direction: '?' for direction in player.current_room.get_exits()}

    #     unexplored = [direction for direction in visited[room] if visited[room][direction] == '?']
        

    #     if len(unexplored) > 0:
    #         direction = unexplored[(random.randint(0, len(unexplored) -1))]
    #         player.travel(direction)

    #         traversal_path.append(direction)

    #         new_room = player.current_room.id

    #         visited[room][direction] = new_room

    #         if new_room not in visited:
    #             visited[new_room] = {direction: '?' for direction in player.current_room.get_exits()}
    #             opp_dir = other_way(direction)
    #             visited[new_room][opp_dir] = room

    #     else:
    #         directions = bfs(visited, room)
    #         traversal_path = traversal_path + directions
    #         for direction in directions:
    #             player.travel(direction)






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

    

run_code()


    

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
