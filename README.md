#exDriver API
Minimal example of RESTful API endpoints for a Driver database.

Endpoints at:

/driver/create?firstname=<first>&lastname=<last>&date_of_birth<YYYY-MM-DD>

- POST: Creates a new driver, assigns ID and creation date


/drivers

- GET: Gets Json formatted list of drivers


/drivers/byDate?date=<date>

- GET: Gets list of drivers created after specified date.

----------------------------------------------------------

Run:

Run python file (I'm using vers. 3.8.0) to run locally.
Use curl to test in terminal. Or manually test URLs in browser.


curl example (In broswer can remove backslashes):

curl http://127.0.0.1:5000/driver/create?firstname=john\&lastname=smith\&date_of_birth=1993-08-02

curl http://127.0.0.1:5000/drivers

----------------------------------------------------------

Files:

Drivers.txt file: Driver records are dumped into this file

api.raml: Some manually produced psuedo RAML. No response codes included.
