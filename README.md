# AirBnB Clone - The Console

## Table Of Content
- [Description](#description)
- [Usage](#usage)
- [Description](#description)
- [Description](#description)
- [Description](#description)

## Description <a name="description">
The project aims to replicate some of the core functionalities of the popular accommodation rental platform AirBnB utilizing Object-Oriented Programming (OOP) principles and following Test-Driven Development (TDD) methodologies. It includes a command-line interface (CLI) and backend functionalities for managing and interacting with rental properties.

- ### The Console
  The console is a command line interface that allows users to interact with the JSON file-based data storage system for the AirBnB clone project. It uses the Python module 'cmd' to create the interface and provides a custom prompt of '(hbnb)'. The console implements the ability to quit the program using 'quit' or 'EOF' and provides a 'help' command to display information on available commands.

- ### Models
  The models folder contains files of all classes uses in the project.
  | Classes | Description | Attributes | file
  | ----------- | ----------- | ----------- | ----------- |
  | `BaseModel` | Base class which defines all common attributes/methods for other classes. | `id`, `created_at`, `updated_at` | [base_model.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/base_model.py) |
  | `User` | For managing user information | `email`, `password`, `first_name`, `last_name` | [user.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/user.py) |
  | `State` | For managing location information | `name` | [state.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/state.py) |
  | `City` | For managing location information | `state_id`, `name` | [city.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/city.py) |
  | `Place` |  For managing accomodation information | `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, `amenity_ids` | [place.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/place.py) |
  | `Amenity` | For managing Amenity informatin | `name` | [amenity.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/amenity.py) |
  | `Review` | For managing review information | `place_id`, `user_id`, `text` | [review.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/review.py) |

- ### Storage
  The FileStorage system utilizes JSON (JavaScript Object Notation) as the serialization format for storing data persistently. Specifically, the data is stored in a file named `file.json`, which serves as the primary storage mechanism for the application.

  **Functionality**
  - Data Serialization: Objects within the AirBnB Clone project are serialized into JSON format before being written to the file.json file. This serialization process converts Python objects into a human-readable and lightweight format that can be easily stored and manipulated.

  - File Organization: The file.json file organizes data using JSON object notation, with each class or data type represented as a JSON object. Individual instances of classes are stored as nested objects within their respective class entries.

  - CRUD Operations: The FileStorage system supports CRUD operations for managing data stored in the file.json file. It allows for the creation, retrieval, modification, and deletion of data objects by reading from and writing to the JSON file.


## Usage <a name="usage">
- **Cloning the repository**
  ```
  git clone https://github.com/x33zp/AirBnB_clone.git
  ```

- **Running the console**
  ```
  ./console.py
  ```

  | Command | Description |
  | ----------- | ----------- |
  | `(hbnb) help ` | Displays a list of available commands |
  |  `(hbnb) help <command>` | Provides information about the command specified as an argument. |
  | `(hbnb) quit` | Exits/quits the console. |
  | `(hbnb) create <classname>` | Creates a new instance of the specified class and returns the ID |
  | `(hbnb) all` | Displays the string representation all instances of all classes. |
  | `(hbnb) all <classname>` or <br>  `<classname>.all()` | Displays the string representation of all instances of the specified class |
  | `(hbnb) <classname>.count()` | Displays the total number of instances of the specified class. |
  | `(hbnb) show <classname> <id>` or <br> `<classname>.show("<id>")` | Displays the string representation of a specific instance based on the class name and ID provided. |
  | `(hbnb) update <classname> <id> <attribute name> "<attribute value>"` or <br> `<class name>.update(<id>, <attribute name>, <attribute value>)` or <br> `<class name>.update(<id>, <dictionary representation>)` | Updates attributes of a specific instance based on the class name and ID provided.  |
  | `(hbnb) destroy <classname> <id>` | Deletes a specific instance based on the class name and ID provided |