# AirBnB Clone - The Console

## Table Of Content
- [Description](#description)
- [Usage](#usage)
- [Testing](#testing)
- [Authors](#authors)

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
  The FileStorage system utilizes JSON (JavaScript Object Notation) as the serialization format for storing data persistently. Specifically, the data is stored in a file named `file.json`, which serves as the primary storage mechanism for the application, the code can be found in [file_storage.py](https://github.com/x33zp/AirBnB_clone/blob/main/models/engine/file_storage.py).

  **Functionality**
  - Data Serialization and Deserialization: Objects within the AirBnB Clone project are serialized into JSON format before being written to the file.json file. This serialization process converts Python objects into a human-readable and lightweight format that can be easily stored, manipulated and retrieved followinf this flow: `<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>`.

  - File Organization: The file.json file organizes data using JSON object notation, with each class or data type represented as a JSON object. Individual instances of classes are stored as nested objects within their respective class entries.

  - CRUD Operations: The FileStorage system supports CRUD operations for managing data stored in the file.json file. It allows for the creation, retrieval, modification, and deletion of data objects by reading from and writing to the JSON file.


## Usage <a name="usage">
- **Cloning the repository**
  ```
  $ git clone https://github.com/x33zp/AirBnB_clone.git
  ```

- **Running the console** \
  The console can be run both interactively and non-interactively.
  ```
  $ ./console.py
  ```

  | Command | Description |
  | ----------- | ----------- |
  | `help` | Displays a list of available commands |
  | `help <command>` | Provides information about the command specified as an argument. |
  | `quit` | Exits/quits the console. |
  | `create <classname>` | Creates a new instance of the specified class and returns the ID |
  | `all` | Displays the string representation all instances of all classes. |
  | `all <classname>` or <br>  `<classname>.all()` | Displays the string representation of all instances of the specified class |
  | `<classname>.count()` | Displays the total number of instances of the specified class. |
  | `show <classname> <id>` or <br> `<classname>.show("<id>")` | Displays the string representation of a specific instance based on the class name and ID provided. |
  | `update <classname> <id> <attribute name> "<attribute value>"` or <br> `<class name>.update("<id>", "<attribute name>", "<attribute value>")` or <br> `<class name>.update("<id>", <dictionary representation>)` | Updates attributes of a specific instance based on the class name and ID provided.  |
  | `destroy <classname> <id>` or <br> `<class name>.destroy("<id>")` | Deletes a specific instance based on the class name and ID provided |

  To run non-interactively you need to pipe a valid console command into the execution of the `console.py` file.
  ```
  $ echo "help" | ./console.py
  (hbnb)
  Documented commands (type help <topic>):
  ========================================
  EOF  all  create  destroy  help  quit  show  update

  (hbnb)
  $
  ```

  A prompt for input is displayed in interactive mode, then you can proceed to input a valid command.
  \
  **using the `create` command.**
  ```
  $ ./console
  (hbnb) create BaseModel
  6ed092f8-dd5f-418c-a83b-136d5f7fd293
  (hbnb) quit
  ```
  \
  **Using the `all`, `all <classname>` and `<classname>.all()`commands.**
  ```
  (hbnb) create User
  c69cd071-b08e-45da-912e-87812525c5a4
  (hbnb) all
  ["[BaseModel] (6ed092f8-dd5f-418c-a83b-136d5f7fd293) {'id': '6ed092f8-dd5f-418c-a83b-136d5f7fd293', 'created_at': datetime.datetime(2024, 3, 31, 16, 29, 43, 120752), 'updated_at': datetime.datetime(2024, 3, 31, 16, 29, 43, 120821)}", "[User] (c69cd071-b08e-45da-912e-87812525c5a4) {'id': 'c69cd071-b08e-45da-912e-87812525c5a4', 'created_at': datetime.datetime(2024, 3, 31, 16, 39, 48, 231360), 'updated_at': datetime.datetime(2024, 3, 31, 16, 39, 48, 231451)}"]
  (hbnb) all User
  ["[User] (c69cd071-b08e-45da-912e-87812525c5a4) {'id': 'c69cd071-b08e-45da-912e-87812525c5a4', 'created_at': datetime.datetime(2024, 3, 31, 16, 39, 48, 231360), 'updated_at': datetime.datetime(2024, 3, 31, 16, 39, 48, 231451)}"]
  (hbnb) BaseModel.all()
  ["[BaseModel] (6ed092f8-dd5f-418c-a83b-136d5f7fd293) {'id': '6ed092f8-dd5f-418c-a83b-136d5f7fd293', 'created_at': datetime.datetime(2024, 3, 31, 16, 29, 43, 120752), 'updated_at': datetime.datetime(2024, 3, 31, 16, 29, 43, 120821)}"]
  ```
  \
  **Using the `<classname>.count()` command.**
  ```
  (hbnb) create User
  412731ac-a032-411a-aab8-bc81871e2ce9
  (hbnb) User.count()
  2
  (hbnb) BaseModel.count()
  1
  ```
  \
  **Using the `show <classname> <id>` and `<classname>.show("<id>")` commands.**
  ```
  (hbnb) show BaseModel 6ed092f8-dd5f-418c-a83b-136d5f7fd293
  [BaseModel] (6ed092f8-dd5f-418c-a83b-136d5f7fd293) {'id': '6ed092f8-dd5f-418c-a83b-136d5f7fd293', 'created_at': datetime.datetime(2024, 3, 31, 16, 29, 43, 120752), 'updated_at': datetime.datetime(2024, 3, 31, 16, 29, 43, 120821)}
  (hbnb) User.show("412731ac-a032-411a-aab8-bc81871e2ce9")
  [User] (412731ac-a032-411a-aab8-bc81871e2ce9) {'id': '412731ac-a032-411a-aab8-bc81871e2ce9', 'created_at': datetime.datetime(2024, 3, 31, 16, 43, 54, 277038), 'updated_at': datetime.datetime(2024, 3, 31, 16, 43, 54, 277111)}
  ```
  \
  **Using the `update <classname> <id> <attribute name> "<attribute value>"`, `<class name>.update("<id>", "<attribute name>", "<attribute value>")` and `<class name>.update("<id>", <dictionary representation>)` commands.**
  ```
  (hbnb) update BaseModel 6ed092f8-dd5f-418c-a83b-136d5f7fd293 name "1st_BaseModel"
  (hbnb) show BaseModel 6ed092f8-dd5f-418c-a83b-136d5f7fd293
  [BaseModel] (6ed092f8-dd5f-418c-a83b-136d5f7fd293) {'id': '6ed092f8-dd5f-418c-a83b-136d5f7fd293', 'created_at': datetime.datetime(2024, 3, 31, 16, 29, 43, 120752), 'updated_at': datetime.datetime(2024, 3, 31, 16, 54, 42, 661124), 'name': '1st_BaseModel'}
  (hbnb) User.update("c69cd071-b08e-45da-912e-87812525c5a4", "name", "user1")
  (hbnb) show User c69cd071-b08e-45da-912e-87812525c5a4
  [User] (c69cd071-b08e-45da-912e-87812525c5a4) {'id': 'c69cd071-b08e-45da-912e-87812525c5a4', 'created_at': datetime.datetime(2024, 3, 31, 16, 39, 48, 231360), 'updated_at': datetime.datetime(2024, 3, 31, 16, 57, 59, 514057), 'name': 'user1'}
  (hbnb) User.update("412731ac-a032-411a-aab8-bc81871e2ce9", {"name": "user2", "number": 2})
  [User] (412731ac-a032-411a-aab8-bc81871e2ce9) {'id': '412731ac-a032-411a-aab8-bc81871e2ce9', 'created_at': datetime.datetime(2024, 3, 31, 16, 43, 54, 277038), 'updated_at': datetime.datetime(2024, 3, 31, 17, 7, 31, 22184), 'name': 'user2', 'number': 2}
  ```
  \
  **Using the `destroy <classname> <id>` and `<class name>.destroy("<id>")` commands.**
  ```
  (hbnb) User.count()
  2
  (hbnb) destroy User c69cd071-b08e-45da-912e-87812525c5a4
  (hbnb) User.count()
  1
  (hbnb) User.destroy("412731ac-a032-411a-aab8-bc81871e2ce9")
  (hbnb) User.count()
  0
  ```
  \
  **Exiting the console.**
  ```
  (hbnb) quit
  $
  ```

## Testing <a name="testing">
Unittest for the project are defined in the [tests](https://github.com/x33zp/AirBnB_clone/tree/main/tests) folder. To run the entire test suite simultaneously, execute the following command:
```
$ python3 unittest -m discover tests
```
Alternatively, you can specify a single test file to run at a time:
```
$ python3 unittest -m tests/filename.py
```

## Authors <a name="authors">
- [Zubby Peculiar](https://github.com/x33zp)