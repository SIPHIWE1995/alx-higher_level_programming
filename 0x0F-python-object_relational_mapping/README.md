0x0F. Python - Object-relational Mapping 😄
This project focuses on working with Object-Relational Mapping (ORM) using SQLAlchemy and MySQL. The project contains several Python scripts that interact with a MySQL database to perform various tasks related to states and cities.

Prerequisites
Python 3.8.5
MySQLdb version 2.0.x
SQLAlchemy version 1.4.x
Ubuntu 20.04 LTS
pycodestyle version 2.8.x
Setup
Clone the repository:
git clone https://github.com/Nicholas2023/alx-higher_level_programming.git
Navigate to the project directory:
cd alx-higher_level_programming/0x0F-python-object_relational_mapping
Install the required packages:
pip3 install SQLAlchemy
Task Descriptions
0-select_states.py
Lists all states from the database hbtn_0e_0_usa.

Usage:

./0-select_states.py <mysql_username> <mysql_password> <database_name>
1-filter_states.py
Lists states with names starting with 'N' from the database hbtn_0e_0_usa.

Usage:

./1-filter_states.py <mysql_username> <mysql_password> <database_name>
2-my_filter_states.py
Lists states based on user input from the database hbtn_0e_0_usa.

Usage:

./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
3-my_safe_filter_states.py
Lists states based on user input (safe from SQL injection) from the database hbtn_0e_0_usa.

Usage:

./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
4-cities_by_state.py
Lists all cities from the database hbtn_0e_4_usa.

Usage:

./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
5-filter_cities.py
Lists cities by state name from the database hbtn_0e_4_usa.

Usage:

./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
6-model_state.py
Defines the State class and creates a corresponding database table.

Usage:

./6-model_state.py <mysql_username> <mysql_password> <database_name>
7-model_state_fetch_all.py
Lists all State objects from the database.

Usage:

./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
8-model_state_fetch_first.py
Prints the first State object from the database.

Usage:

./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
9-model_state_filter_a.py
Lists State objects with names containing the letter 'a' from the database.

Usage:

./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>
10-model_state_my_get.py
Prints the State object with the given name from the database.

Usage:

./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>
11-model_state_insert.py
Adds a new State object to the database.

Usage:

./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>
12-model_state_update_id_2.py
Changes the name of a State object with id 2 in the database.

Usage:

./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>
13-model_state_delete_a.py
Deletes State objects with names containing the letter 'a' from the database.

Usage:

./13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>
model_city.py & 14-model_city_fetch_by_state.py
Defines the City class, creates the cities table, and fetches cities by state.

Usage:

./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>
Author
Siphiwe Nomademeshane
