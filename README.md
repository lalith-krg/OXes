# OXes

OXes is an implementation of the classic Tic-Tac-Toe game played by 2 players. This uses socket programming in the server-client model.

To run this, first open the folder and in a new terminal and run

```
python server.py <port number>
```

Enter a valid port number. P.S. Avoid smaller port numbers.

While the server terminal is ready, open another terminal and run

```
python client.py <same port number>
```

Enter the same port number to connect to the server. Once done, the two windows should open up.

To play against the computer, just use the port number 0

```
python server.py 0
```