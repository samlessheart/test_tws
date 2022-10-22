This is an assignment project for taxiwars (problem description is at the end)

this project only consists of Rest Framework

Following API Endpoints are available 

1. List of Users (GET, POST)
http://127.0.0.1:8000/api/users/

2. detail view of a user (GET, PUT, DELETE) (Authentication required for PUT, DELETE)
http://127.0.0.1:8000/api/users/1/

3. Create a Game Board (GET)(Authentication required)
http://127.0.0.1:8000/api/createboard/

4. List of all GameBoard Created (GET)(Authentication required)
http://127.0.0.1:8000/api/gamelist/

5. a Detail of a Game Board (GET)(Authentication required)
http://127.0.0.1:8000/api/getBoard/1/

6. to update a Game String (PUT)(Authentication required)
http://127.0.0.1:8000/api/updateBoard/1/

---------------------------------------------------------------------------------------------

Assignment Problem Description

Implement REST APIs for a palindrome game.

The following APIs need to be implemented using Python Django and Postman or any similar tool can be used for testing.

Please use your preferred DB and design API names

User APIs

User creation, deletion and update.

These APIs will be used for user management.

User Login.

Once a user login, then the user can invoke the Game and List functionality.

Game APIs

Start/Create

This will initialize empty string

This should return game-ID

getBoard

This will return the value string from the server.

e.g. after create-game , the state of the string will be "".

and after the user invokes updateBoard , the string will have some value.

updateBoard

Using this API, the user will append one character between 'a' to 'z' to string.

Server should update the string and add one more random number.

Once the length of the string is 6, it should return whether the string is palindrome or not.

List of Games API

This API should list all game IDs created in the system.


