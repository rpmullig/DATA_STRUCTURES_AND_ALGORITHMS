from utilities import *

def flood(color_of_tile, flooded_list, screen_size):
	

	print flooded_list

	added = False
	
	for x in range(len(flooded_list)):
		element = flooded_list[x]
	
		if in_bounds(down(element), screen_size):
			if color_of_tile[element] == color_of_tile[down(element)]:
				if down(element) not in flooded_list:
					flooded_list.append(down(element))	
					added = True
					
		if in_bounds(up(element), screen_size):
			if color_of_tile[element] == color_of_tile[up(element)]:
				if up(element) not in flooded_list:
					flooded_list.append(up(element))	
					added = True
					
					
		if in_bounds(left(element), screen_size):
			if color_of_tile[element] == color_of_tile[left(element)]:
				if left(element) not in flooded_list:
					flooded_list.append(left(element))	
					added = True
					
		if in_bounds(right(element), screen_size):
			if color_of_tile[element] == color_of_tile[right(element)]:
				if right(element) not in flooded_list:
					flooded_list.append(right(element))	
					added = True
					
	if added:
		flood(color_of_tile, flooded_list, screen_size)
	
	else:
		print color_of_tile[flooded_list[0]]
		print flooded_list
	
		return flooded_list
