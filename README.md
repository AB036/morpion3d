# MEGA MORPION 3D - Groupe Python 2
POOA ISIA 2018

A [3D tic-tac-toe](https://en.wikipedia.org/wiki/3D_tic-tac-toe) written in Python as part of the 2018 object oriented programming course at Centralesupélec.

The game is multi-player only: you need to run two game instances to be able to play (a "server" and a "client"). The client needs to manually enter the IP address of the server to connect. If the server and the client are on the same computer, leave the default join address as it is already set to 127.0.0.1 (localhost).

# Members
- Armand Bouvier
- Sylvestre Prabakaran
- Gabriel Moneyron

# Requirements
This software project has been written in Python 3, so you need it to run the game.

The game needs pygame to run. See <https://www.pygame.org/wiki/GettingStarted> for installation. Most likely, you can just do `pip install pygame`.

**requirements.txt** lists all the python modules needed for this project. Running `pip install -r requirements.txt` will install them automatically.

The game uses the port 12800 with TCP. So try to open it if it seems you can't connect to another game.

# Instructions
Clone the repository and launch main.py to start the game.

Commands are written on screen

# Features
- A 3D tic-tac-toe game engine
- Game sizes can go from 3x3x3 to 9x9x9!
- A basic 3D engine with points, polygons and even meshes
- An interface using Pygame
- Games over network
- A low config mode if the <sub><sup>badly optimized 3D engine written in Python</sup></sub> does not run well on your computer

# Screenshots

![Pretty graphics mode](https://raw.githubusercontent.com/Benhalor/morpion3d/master/Screenshot%20from%202018-11-10%2014-55-33.png)

![High performances mode](https://raw.githubusercontent.com/Benhalor/morpion3d/master/Screenshot%20from%202018-11-10%2014-56-07.png)


