# Airlines Flight Management API
This is a RESTful API for managing airplanes in the "ZipAirlines" airline company. The API allows for input of information about 10 different airplanes, calculates the fuel consumption per minute, and determines the maximum flight duration.

## Requirements
- Python 3.x
- Django
- Django Rest Framework
## Installation
1. Clone the repository:
```shell
git clone https://github.com/ostapT/airlines_flight_management_api.git
```
2. Navigate to the project directory:
```shell
cd airlines_flight_management_api
```
3. Install the dependencies:
```shell
pip install -r requirements.txt
```
4. Run the migrations to create the database:
```shell
python manage.py makemigrations
python manage.py migrate
```
5. Start the server:
```shell
python manage.py runserver
```
6. The API will be available at http://localhost:8000/api/

## Usage
The API provides the following functionalities:

- GET /api/planes/: Get a list of all airplanes.
- POST /api/planes/: Create a new airplane.
- GET /api/planes/{id}/: Get details of a specific airplane by its identifier.
- PUT /api/planes/{id}/: Update the information of an airplane by its identifier.
- DELETE /api/planes/{id}/: Delete an airplane by its identifier.

## Documentation
The API has documentation built using Swagger. To view the documentation, start the server and open the link http://localhost:8000/api/doc/swagger/
