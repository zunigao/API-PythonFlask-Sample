# Orlando Zuniga API for C.H. Robinson
# 11-28-2020 
# app.py

import sys
import flask
import json

from path_solver import graph_loader, shortest_path

app = flask.Flask(__name__)

'''
Endpoint returns an html file with a list of country codes the user can enter or click on.
'''
@app.route('/')
def index():
	return flask.render_template('index.html')


'''
This method loads the countries as a dictionary in python. If the country code is not in the dictionary then
a 404 error is sent to the user.
Makes a call to path_solver.py to calculate the shortest path from the USA to the country code. The function will
return an empty list if there are no paths to the destination.
Returns the destination and a list of countries a driver must travel through in JSON format.
'''
@app.route('/<country_code>')
def get_travel_list(country_code):
	countries = graph_loader('countries.json')
	#Error Handling will return a 404 error and message when the country code is not valid.
	if country_code not in countries.keys():
		error_message = "\"{0}\" not found. The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.\
			  \n Please select a valid endpoint from the following list: {1}".format(country_code, list(countries))
		print()
		flask.abort(404, error_message)
	route = shortest_path(countries, start = "USA", end = country_code)

	print(route)
	#Returns the destination and list of countries in a JSON format.
	return json.dumps({"destination": country_code, 
		"list" : route})


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: {0} host port'.format(sys.argv[0]))
		print('  Example: python3 {0} 127.0.0.1 5000'.format(sys.argv[0]))
		exit()

	host = sys.argv[1]
	port = int(sys.argv[2])
	app.run(host=host, port=port, debug=True)




