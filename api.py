import flask, datetime, json
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Data store
drivers = []
drivers_file = 'drivers.txt'

# Get all drivers
@app.route('/drivers', methods=['GET'])
def get_all_drivers():
	return jsonify(drivers)		

# Post new drivers -  no default routes
@app.route('/driver/create', methods=['GET', 'POST'])
def create_driver(): 
	id_val = 1

	if len(drivers) > 0:
		id_val = drivers[-1]['id'] + 1 

	new_driver = {
        'id': id_val, # generate a uuid for each rec
        'first name': request.args.get('firstname'),
        'last name': request.args.get('lastname'),
        'date_of_birth': request.args.get('date_of_birth'), # do not error check DOB
        'creation date': datetime.date.today().strftime('%Y-%m-%d')
	}
	
	drivers.append(new_driver)
	keep_drivers_file_updated()

	return jsonify(new_driver), 201

# Get drivers created after specififed date
@app.route('/drivers/byDate', methods=['GET'])
def get_drivers_by_date():

	drivers_after_date = []
	byDate = request.args.get('byDate')

	for driver in drivers:
		if (driver['creation date'] > byDate) :
			drivers_after_date.append(driver)

	return jsonify(drivers_after_date)

# Dump drivers list into text file (as json format)
def keep_drivers_file_updated():
	with open(drivers_file, 'w') as outfile:
		json.dump(drivers, outfile)


app.run()
