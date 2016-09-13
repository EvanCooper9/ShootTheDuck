# Shoot The Duck.
A [Duck Hunt](https://en.wikipedia.org/wiki/Duck_Hunt) inspired python/pygame game

## How to play :
The game opens to the main menu. To start playing, the user must click the mouse.
When the game starts, the player has 3 lives, and 3 shots. These are displayed at the top right corner of the screen, where the lives are represented by hearts and the shots are represented by the black bullets.

## Game Screen :
* Score - Displayed at the top middle
* Shots - Displayed at the top right
* Lives - Displayed at the top right, under the shots

When a duck flies in the screen, the player must try and shoot the duck, by clicking on it. For every duck, the player has 3 shots. If the player successfully shoots the duck, the duck dies by falling to the bottom of the screen, and the appropriate score is added (see below). If the player uses all his/her shots, and did not hit the duck, the screen turns red and the duck flies away. The player then loses a life.

Once a duck flies away, or is killed, the player’s bullets are reloaded, and a new duck spawns and flies around the screen.

For every 3 ducks that the player shoots, the next ducks will start to fly faster.

The game ends when the player loses all their lives. If applicable, the player’s final score updates the high score. The game over screen displays the current high score for the game.

## Scoring :
* + 100 : Successfully shooting the duck on the first shot 
* +  75 : Successfully shooting the duck on the second shot
* +  50 : Successfully shooting the duck on the third shot
