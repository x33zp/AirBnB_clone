# AirBnB Clone - The Console

## Table Of Content
- [Description](#description)
- [Usage](#usage)
- [Description](#description)
- [Description](#description)
- [Description](#description)

## Description <a name="description">
The project aims to replicate some of the core functionalities of the popular accommodation rental platform AirBnB utilizing Object-Oriented Programming (OOP) principles and following Test-Driven Development (TDD) methodologies. It includes a command-line interface (CLI) and backend functionalities for managing and interacting with rental properties.

### The Console
The console is a command line interface that allows users to interact with the JSON file-based data storage system for the AirBnB clone project. It uses the Python module 'cmd' to create the interface and provides a custom prompt of '(hbnb)'. The console implements the ability to quit the program using 'quit' or 'EOF' and provides a 'help' command to display information on available commands.

### Models
The models folder contains files of all classes uses in the project.
| Classes | Description | Attributes | file
| ----------- | ----------- | ----------- | ----------- |
| `BaseModel` | Base class which defines all common attributes/methods for other classes. | `id`, `created_at`, `updated_at` | | [base_model.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/base_model.py) |
| `User` | For managing user information | `email`, `password`, `first_name`, `last_name` | [user.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/user.py) |
| `State` | For managing location information | `name` | [state.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/state.py) |
| `City` | For managing location information | `state_id`, `name` | [city.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/city.py) |
| `Place` |  For managing accomodation information | `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, `amenity_ids` | [place.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/place.py) |
| `Amenity` | For managing Amenity informatin | `name` | [amenity.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/amenity.py) |
| `Review` | For managing review information | `place_id`, `user_id`, `text` | [review.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/review.py) |

### Storage


## Usage <a name="usage">
- **Cloning the repository**
`git clone https://github.com/x33zp/AirBnB_clone.git`

- **Running the console**
`./console.py`

| Command | Description |
| ----------- | ----------- |
| `(hbnb) help` | Quits the console |
| `(hbnb) quit` | Quits the console |
| `(hbnb) create` | Quits the console |
| `(hbnb) all` | Quits the console |
| `(hbnb) show` | Quits the console |
| `(hbnb) update` | Quits the console |
| `(hbnb) destroy` | Quits the console |