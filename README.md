# Chess AI
Artificial Intelligence Chess developed with the minimax adversarial search algorithm. It returns the best possible move it has been able to find at the given depth within a specified time interval, at each iteration the algorithm takes into account a series of Heuristics that tell it whether a particular move is good or bad based on the future outcome it might cause.

By default it analyzes the best move at a depth of 2 and with a time limit of 10 seconds, this means that it will evaluate all possible moves taking into account the outcome of 2 boards in the future. 

##### test the demo [HERE]( "HERE")
<br><br>
## Technologies 

- Python
    - chess
    - numpy
    - pygame
    - sys
    - ast
    - copy
    - os
  
 <br><br>
 ## Project images
 
[![To-Do-List-Home.png](chess.png)](https://postimg.cc/5HF53TPw)
 

<br><br>
## What do you need to run this project ?

- Python - v3.7 onwards

<br><br>
## Installation

- Download the project or clone it
   - download [CLICK AQUI](https://github.com/Fraineralex/ChessAI/archive/refs/heads/master.zip)
   - clone [CLICK AQUI](https://github.com/Fraineralex/ChessAI.git)

- You need to open a console and go to the path where the project is located.
```js
 //C:\Users\Frainer Alexander\Downloads\ChessAI>  - take this path whit example
```

- Now install all dependencies
```cmd
    - chess
    - numpy
    - pygame
    - sys
    - ast
    - copy
    - os
```

- When all packages are installed, you can run the project using the this command 
```cmd
npm start
```

- Now you need to copy and past this path in your brouser 
```cmd
127.0.0.1:5000 
```
Or
```cmd
localhost:5000 
```
<br><br>
## Developer
- Frainer Alexander -> [Github](https://github.com/Fraineralex) 

<br><br>
## Acknowledgment

I am grateful to Nelmix Inc for assigning me this technical test which I certainly enjoyed and it has helped me show my skills and knowledge in this wonderful profession.


- Entry point: main.py
- Press 't' to change theme (green, brown, blue, gray)
- Press 'r' to restart the game
