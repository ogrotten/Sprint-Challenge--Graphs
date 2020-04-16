def output(self, input):
	# viz = []
	# # Create for first X pairs x is total //2
	# for i in range(num_users * avg_friendships // 2):
	# 	friendship = possible_friendships[i]
	# 	self.add_friendship(friendship[0], friendship[1])
	# 	viz.append(f"\t{friendship[0]}->{friendship[1]}\n")
	
	# vizstring = "".join([str(e) for e in viz])

	vizstring = "".join([str(e) for e in input])

	vizexp = 'digraph prof\n{\nedge [arrowhead="none"]\n' + vizstring + '}\n'
	FN = "./friendmap.dot"
	with open(FN, "w") as file:
		file.write(vizexp)
