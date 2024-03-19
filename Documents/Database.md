## Type of Database
For this project, we are connecting our Flask application to a MySQL Database. During earlier phases of the first version, we were using a SQLite Database. Though this was easier to work with, we decided to use a MySQL Database due to its larger-scalability. If we had time to push this project to an actual website on the Internet, rather than solely to the CyberNet network, it would be easier to use MySQL. MySQL is better equipted for more data from high-traffic sites.

## Creating the Database
To make the MySQL Database, we first needed to create the actual database. After logging into MySQL, run the following command:
```
CREATE DATABASE orca_users;
```
After creating the database, run the following command:
```
USE orca_users;
```
This command allows you to focus on using this specific database.

## Configuring the Database

From here, we need to make the tables that house the data. We elected to use two tables for our program. The creation for each is below:
```
CREATE TABLE users ( user_id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(30) NOT NULL, password VARCHAR(300) NOT NULL );
```
user_id : assign each user an INT value as their primary key and automatically increment it with each new user

username : a STRING that can be no longer than 30 characters and cannot be left NULL

password : a STRING that can be no longer than 300 characters and cannot be left NULL

```
CREATE TABLE scores ( user_id INT, Game1 INT, Game2 INT, Game3 INT, FOREIGN KEY (user_id) REFERENCES users(user_id) );
```
user_id : assign each user an INT value as their primary key

Game1, Game2, Game3 : assigns an INT value to each game to house their high scores

FOREIGN KEY (user_id) : ensures that no scores are left without a user; every user must have a score


Now that the tables were created, they were ready to hold data assuming that the Flask Application was correct.
