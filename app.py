import sys
import flask
import json

from path_solver import graph_loader, shortest_path

app = flask.Flask(__name__)

@app.route('/')
def hello():
	return 'You pick a country code and it will return a \
	list of countries a driver must travel through.\
	 \n Here is a list of valid destinations: CAN, USA, MEX, GTM, BLZ, SLV, HND, NIC, CRI, PAN'

@app.route('/<country_code>')
def get_travel_list(country_code):
	countries = graph_loader('countries.json')
	route = shortest_path(countries, start = "USA", end = country_code)

	print(route)
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




