Shoot The Duck.
By Evan Cooper
Version 1.0

How to play :
The game opens to the main menu. To start playing, the user must click the mouse.
When the game starts, the player has 3 lives, and 3 shots. These are displayed at the top right corner of the screen, where the lives are represented by hearts and the shots are represented by the black bullets.

Game Screen :
Score - Displayed at the top middle
Shots - Displayed at the top right
Lives - Displayed at the top right, under the shots

When a duck flies in the screen, the player must try and shoot the duck, by clicking on it. For every duck, the player has 3 shots. If the player successfully shoots the duck, the duck dies by falling to the bottom of the screen, and the appropriate score is added (see below). If the player uses all his/her shots, and did not hit the duck, the screen turns red and the duck flies away. The player then loses a life.

Once a duck flies away, or is killed, the player’s bullets are reloaded, and a new duck spawns and flies around the screen.

For every 3 ducks that the player shoots, the next ducks will start to fly faster.

The game ends when the player loses all their lives. If applicable, the player’s final score updates the high score. The game over screen displays the current high score for the game.

Scoring :
+ 100 : Successfully shooting the duck on the first shot 
+ 75 : Successfully shooting the duck on the second shot
+ 50 : Successfully shooting the duck on the third shot

Satisfying the requirements :

Skill :
The game  requires fast reflexes in order to accurately shoot the duck while it it flying around the screen.

Lives :
The player has 3 lives per game. When they have used all their shots for the current duck, without hitting it, they lose a life. The game ends when the player has no more lives.

Score :
The score is displayed at the top middle of the screen
Please read the comments in the code. It explains why images had to be used instead of fonts for the entire game.

Difficulty Increase :
For every 3 ducks that the player shoots, the speed of the following ducks increases.

Input validation and error recovery :
There is not much room for input validation and error recovery, however, while a duck is flying away or dying, the user cannot attempt to shoot the duck again.

Sound Effects :
- There is a shooting sound effect for every time the player takes a shot
- There is a quacking sound for every time a player shoots a duck
- There is a reloading sound for every time that the player’s bullets are reloaded (Once a new duck spawns)
- The music fades out during the game over screen

Soundtrack :
The game has a song that plays through the entire playing process
Song downloaded for free from :
http://ericskiff.com/music/

Screens :
- There is a main menu screen
- There is a game over screen
- The game over screen features a high score, which is stored in ‘HighScore.txt’

Pauses :
The game features a 3 second pause between when a duck missed and flies out of the screen, and when the next duck flies from the grass.

Bonus : 
The game animations include smooth acceleration. Since the movement of the duck does not depend on the counting of pixels, and the movement uses vectors, the animation is more smooth. There is also inertia in the movement in the duck, because it does not switch paths immediately, it slowly deviates from it current path, towards the new path. I implemented a high score within the game. The high score is saved on a text file. If the current game’s score is higher than the high score, the file is overwritten with the new score. The game also features a pause and mute feature. To pause and un-pause the game, press the ‘space’ key. To mute and un-mute the game, press the ‘m’ key. The muting resets when the game is reset.