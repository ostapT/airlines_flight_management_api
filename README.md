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
3. Set virtual enviroment:
```shell
python -m venv venv
source venv/bin/activate (on MacOS/Linux)
venv\Scripts\activate (on Windows)
```
4. Install the dependencies:
```shell
pip install -r requirements.txt
```
5. Create .env file using .env.sample as a template. Provide your info for variables inside it, for e.g. DJANGO_SECRET_KEY=your secret key
6. Run the migrations to create the database:
```shell
python manage.py makemigrations
python manage.py migrate
```
7. Start the server:
```shell
python manage.py runserver
```
8. The API will be available at http://localhost:8000/api/

## Usage
The API provides the following functionalities:

- GET /api/planes/: Get a list of all airplanes.
- POST /api/planes/: Create a new airplane.
- GET /api/planes/{id}/: Get details of a specific airplane by its identifier.
- PUT /api/planes/{id}/: Update the information of an airplane by its identifier.
- DELETE /api/planes/{id}/: Delete an airplane by its identifier.

## Documentation
The API has documentation built using Swagger. To view the documentation, start the server and open the link http://localhost:8000/api/doc/swagger/

## Scalability and Principles

To ensure scalability of this project, several key principles were followed.

Firstly, the principle of Separation of Concerns was applied. This is evident in the use of two different serializers - PlaneSerializer and PlaneDetailSerializer. PlaneSerializer is used for creating and updating plane objects, while PlaneDetailSerializer adds additional fields related to fuel consumption and maximum flight duration calculations. This allows for extending the functionality of endpoints without the need to modify the underlying data model.

Secondly, the use of tests is crucial for ensuring the safety and stability of the program. In my project, a set of tests was written to verify the functionality of core features, such as fuel consumption and maximum flight duration calculations. This helps identify and fix errors at early stages of development and maintain a reliable program.

Furthermore, considering the scalability of the project, potential changes in the database structure were taken into account. When modifying the table structure, the functionality of endpoints remains intact, thanks to the use of serializers and proper separation of logic.
