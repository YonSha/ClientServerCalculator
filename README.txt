------------------=============================================------------------
This is a simple server-client architecture.
The server expect a mathematical equation such as "5+5" , 6*6+5 etc.
The server returns the answer.
Both server& client working on different threads, so they can run simultaneously.


Client.py
Responsible for the user input.

Server.py
Responsible for the calculation & the output.

ConnectionHandler.py
responsible for the connection between the server & the client

main.py
Runs both the client & the server.


logger
Responsible for logging the application.

tools
generic tools.

Example:
 -->: 5*5
 Received from server: Answer: 25

------------------=============================================------------------