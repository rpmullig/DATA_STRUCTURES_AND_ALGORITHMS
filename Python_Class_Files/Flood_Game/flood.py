from utilities import *

def flood(color_of_tile, flooded_list, screen_size):


	added = False
	new_elements = []


	for x in range(len(flooded_list)):

                element = flooded_list[x]

		if (in_bounds(down(element), screen_size)) and (color_of_tile[element] == color_of_tile[down(element)]) and (down(element) not in flooded_list):
					flooded_list.append(down(element))
                                        new_elements.append(down(element))
					added = True

		if (in_bounds(up(element), screen_size)) and (color_of_tile[element] == color_of_tile[up(element)]) and (up(element) not in flooded_list):
					flooded_list.append(up(element))
                                        new_elements.append(up(element))
					added = True


		if (in_bounds(left(element), screen_size)) and (color_of_tile[element] == color_of_tile[left(element)]) and (left(element) not in flooded_list):
					flooded_list.append(left(element))
					new_elements.append(left(element))
                                        added = True

		if (in_bounds(right(element), screen_size)) and (color_of_tile[element] == color_of_tile[right(element)]) and (right(element) not in flooded_list):
					flooded_list.append(right(element))
					new_elements.append(right(element))
                                        added = True

	if added:
                flood_recure(color_of_tile, new_elements, flooded_list, screen_size)

	else:
		print color_of_tile[flooded_list[0]]
		print flooded_list

		return flooded_list



def flood_recure(color_of_tile, new_elements, flooded_list, screen_size):

	added = False

	for x in range(len(new_elements)):

                element = new_elements[x]

		if (in_bounds(down(element), screen_size)) and (color_of_tile[element] == color_of_tile[down(element)]) and (down(element) not in flooded_list):
					flooded_list.append(down(element))
                                        new_elements.append(down(element))
					added = True

		if (in_bounds(up(element), screen_size)) and (color_of_tile[element] == color_of_tile[up(element)]) and (up(element) not in flooded_list):
					flooded_list.append(up(element))
                                        new_elements.append(up(element))
					added = True


		if (in_bounds(left(element), screen_size)) and (color_of_tile[element] == color_of_tile[left(element)]) and (left(element) not in flooded_list):
					flooded_list.append(left(element))
					new_elements.append(left(element))
                                        added = True

		if (in_bounds(right(element), screen_size)) and (color_of_tile[element] == color_of_tile[right(element)]) and (right(element) not in flooded_list):
					flooded_list.append(right(element))
					new_elements.append(right(element))
                                        added = True

	if added:
                flood_recure(color_of_tile, new_elements, flooded_list, screen_size)

	else:
		print color_of_tile[flooded_list[0]]
		print flooded_list

		return flooded_list
