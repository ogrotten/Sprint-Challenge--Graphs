from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from darrin import output

# region world
# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

reversedir = {"n": "s", "s": "n", "e": "w", "w": "e"}
reverse = [None]

# route for knowing where I've been.
route = visited = {}  # Note that this is a dictionary, not a set

while len(visited) < len(room_graph):
	local = player.current_room.id
	print("Local", local)
	localexits = player.current_room.get_exits()
	DIR = ""

	if local not in visited:
		# if we haven't just started.
		if reverse[-1]:
			# remove the most recently used dir from exits so we don't loop.
			localexits.remove(reverse[-1])
		visited[local] = localexits

	# if we have directions to go
	if len(visited[local]) > 0:
		# pluck off the last one
		DIR = visited[local].pop()
		# put it in the map
		traversal_path.append(DIR)
		# map the reverse
		reverse.append(reversedir[DIR])
		# MOVETO
		print("Forward", DIR)
		player.travel(DIR)

	# if no place left to go
	else:
		# take off the most recent reverse step
		if reverse[-1]:
			DIR = reverse.pop()
			traversal_path.append(DIR)
			print("BACK", DIR)
			player.travel(DIR)


# output(visited)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
	player.travel(move)
	visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
	print(
		f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
	)
else:
	print("TESTS FAILED: INCOMPLETE TRAVERSAL")
	print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


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
