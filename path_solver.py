import json
import sys

def graph_loader(countries_list):
	with open(countries_list) as f:
		data = json.load(f)
		return data

'''
Finds the shortest path given a graph of countries
A start node and an end node (CAN)

'''
def shortest_path(graph, start, end = 'CAN', path=[]):
	path = path + [start]
	if start == end:
		return path
	if start not in graph.keys():
		return None
	shortest = None
	for node in graph[start]:
		if node not in path:
			new_path = shortest_path(graph, node, end, path)
			if new_path:
				if not shortest or len(new_path) < len(shortest):
					shortest = new_path
	return shortest


if __name__ == "__main__":  
	if len(sys.argv) != 2:
		print('Usage: python3 {0} country_code'.format(sys.argv[0]), file=sys.stderr)
		exit()
	countries = graph_loader('countries.json')
	route = shortest_path(countries, start = sys.argv[1])

	print(route)