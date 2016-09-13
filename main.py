################################
# Evan Cooper
# Assignment 8
################################

# Imports
from __future__ import division
import sys
import os
import math
import pygame
import random
import time

# After upgrading to Mac OSX 10.10, the pygame font module becomes uninstalled.
# It cannot be installed at this point.
# This program was created on a Mac computer, 
# and needed to be tested on the same computer.
# Therefore, instead of using fonts, 
# this program uses images of text that get blitted to the screen.
# The code is longer than it should be, 
# since each image had to be loaded in (especially numbers), 
# instead of using one line for loading a font.

# Useful functions
def delta(a1, a2) :
	# Return the absolute value of the difference of two numbers
	return max(a1, a2) - min(a1, a2)

def High_Score(score, low_score_txt, high_score_txt):
	# Function modified from 
	# programarcadegames.com/python_examples/show_file.php?file=high_score.py
	try :
		score_file = open('HighScore.txt', 'r')
		high_score = int(score_file.read())
		score_file.close()
	except IOError :
		# This should never happen
		print 'There is no high score'
	
	if high_score < score :
		txt = high_score_txt
		try :
			score_file = open('HighScore.txt', 'w')
			score_file.write(str(score))
			score_file.close()
		except IOError :
			# This should never happen
			print 'Couldn"t save the score'
	else : 
		txt = low_score_txt
	return txt

def load_image(filename) :
	return pygame.image.load(os.path.join('images', filename))

def load_sound(filename) :
	return pygame.mixer.Sound(os.path.join('sounds', filename))

def check_shots_and_lives(self):
	if self.duck.missed == 0 :
		self.shots = self.shots_list[2]
	if self.duck.missed == 1 :
		self.shots = self.shots_list[1]
	if self.duck.missed == 2 :
		self.shots = self.shots_list[0]
	if self.duck.missed > 2 :
		self.shots = self.clear_img

	if self.duck.lives == 3 :
		self.life = self.lives_list[2]
	if self.duck.lives == 2 :
		self.life = self.lives_list[1]
	if self.duck.lives == 1 :
		self.life = self.lives_list[0]
	if self.duck.lives == 0 :
		self.life = self.clear_img
		self.shots = self.clear_img
		self.state == Game.GAMEOVER

# Create a duck object
class Duck(object) :
	def __init__(self, position, target_x, target_y, width, height) :
		# Load duck images
		self.duck_right = pygame.image.load('images/Duck.png')
		self.duck_left = pygame.transform.flip(self.duck_right, True, False)
		self.duck_img = self.duck_right
		self.duck_rect = self.duck_img.get_rect()
		
		# Set duck parameters
		self.duck_rect.x = position[0]
		self.duck_rect.y = position[1] # 500
		self.target_x = target_x
		self.target_y = target_y
		self.direction_x = 0
		self.direction_y = 0
		self.speed = 0.1

		# Set amounts for each duck object
		self.lives = 3
		self.missed = 0
		self.timer = 0
	
	def move_duck(self, screen_width) :
		# Modify duck orientation based on duck's target
		if self.target_x - self.duck_rect.x < 0 :
			self.duck_img = self.duck_left
		else :
			self.duck_img = self.duck_right

		# Distance from duck to target
		self.dist = math.sqrt(((self.duck_rect.x - self.target_x)**2) + \
					((self.duck_rect.y - self.target_y)**2))
		
		# Difference of duck's x or y value to target's x or y value
		# And angle of a vector towards the target
		delta_x = delta(self.target_x, self.duck_rect.x)
		delta_y = delta(self.target_y, self.duck_rect.y)
		theta = math.atan2(delta_x, delta_y)

		# Create a vector of length 10 from the duck to the target
		if self.target_x < self.duck_rect.x :
			v_x = -10*math.sin(theta)
		else :
			v_x = 10*math.sin(theta)

		if self.target_y < self.duck_rect.y :
			v_y = -10*math.cos(theta)
		else :
			v_y = 10*math.cos(theta)
		
		self.direction_x = .9*self.direction_x + v_x
		self.direction_y = .9*self.direction_y + v_y

		if self.dist >= 50 :
			# If duck isn't close to the target, move it one step closer
			self.duck_rect.x += self.direction_x*self.speed
			self.duck_rect.y += self.direction_y*self.speed

		else :	
			# Select new target
			self.target_x = random.randrange(0, screen_width - \
											self.duck_rect.width)
			self.target_y = random.randrange(0, 800 - self.duck_rect.height)

	def draw_duck(self, surface1, surface2) :
		surface2.blit(surface1, self.duck_rect)

	def reset_duck(self) :
		self.duck_rect.y = 600
		self.target_y = 400

	def kill_duck(self) :
		self.duck_img = pygame.transform.flip(self.duck_img, False, True)
		self.target_x = self.duck_rect.x
		self.target_y = 620
		self.duck_rect.y += 15

	def fly_away(self) :
		self.target_x = self.duck_rect.x
		self.target_y = -100

		self.duck_rect.y -= 15

	def wait_duck(self) :
		self.timer += 1
	
# Main game
class Game(object) :
	# Game stages
	(MAINMENU, PLAYING, DUCK_DYING, DUCK_FLYING_AWAY, GAMEOVER, WAITING)\
	  = range(6)
	
	def __init__(self) :
		# Initialize sound
		pygame.mixer.init()
		pygame.mixer.pre_init(44100, -16, 2, 2048)

		# Initialize pygame module
		pygame.init()
		
		# Set up game window
		self.width = 1100
		self.height = 800
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.toggle_fullscreen()
		pygame.display.set_caption('Shoot The Duck.')

		# Game objects (only 1 is needed)
		self.duck = Duck((random.randrange(100,self.width - 100), 550), \
					random.randrange(50, self.width - 50), \
					random.randrange(50, 500), self.width, self.height)
		
		# Game parameters
		self.mute_key_count = 0
		self.a = 1
		self.b = 1
		self.state = Game.MAINMENU
		self.shots = 3
		self.lives = 3
		self.score = 0
		self.hit_ducks = 0

		# Load data here
		self.shot_sound = load_sound('shot.wav')
		self.reload_sound = load_sound('reload.wav')
		self.duck_hit_sound = load_sound('duck_shot.wav')

		self.theme_song = load_sound('theme.wav')
		self.theme_song.play(-1)
		self.theme_song.set_volume(0.3)

		self.foreground = load_image('foreground.png')
		self.foreground = pygame.transform.scale(self.foreground, \
						(self.width, self.height))

		self.background = load_image('background.png')
		self.background = self.background.convert()
		self.background = pygame.transform.scale(self.background, \
						(self.width, self.height))

		self.lives_list = []
		for i in range(1,4) :
			self.image_l = load_image('lives' + str(i) + '.png')
			self.image_l = pygame.transform.scale(self.image_l, (i*40, 40))
			self.lives_list.append(self.image_l)

		self.shots_list = []
		for i in range(1,4) :
			self.image_s = load_image(str(i) + 'shots.png')
			self.image_s = pygame.transform.scale(self.image_s, (i*40, 40))
			self.shots_list.append(self.image_s)

		self.clear_img = load_image('missed_duck1.png')

		# Here is where the font module would make the code shorter.
		# The code would simply have one line that loads the desired font.
		# That font would later on be used to create numbers and certain texts
		self.menu_txt = load_image('mainmenu.png')
		self.gameovr_txt = load_image('gameover.png')
		self.gameover_high_score = load_image('gameoverhighscore.png')

		self.nums = []
		for i in range(0,10) :
			self.image_n = load_image('numbers/' + str(i) + '.png')
			self.image_n = pygame.transform.scale(self.image_n, (27, 42))
			self.nums.append(self.image_n)

		self.FPS = 12
		self.REFRESH = pygame.USEREVENT + 1
		pygame.time.set_timer(self.REFRESH, 1000//self.FPS)

		self.frame = 1

		# Wait for events
		self.run()

	def restart(self) :
		# Resets the game parameters after restarting the game
		self.a = 1
		self.b = 1
		self.shots = 3
		self.duck.lives = 3
		self.score = 0
		self.hit_ducks = 0
		self.duck.speed = 0.1
		self.theme_song.play(-1)
		self.theme_song.set_volume(0.3)

	def run(self) :
		"""Loop forever processing event"""
		running = True
		while running :
			event = pygame.event.wait()

			# Quitting the game 
			if event.type == pygame.QUIT :
				running = False

			# Pausing the Game
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
				while 1 < 2 :
					event = pygame.event.wait()
					pygame.mixer.pause()
					if event.type == pygame.KEYDOWN \
					  and event.key == pygame.K_SPACE :
						pygame.mixer.unpause()
						break

			# Muting the game
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_m :
				self.mute_key_count += 1
				if self.mute_key_count == 1 :
					self.shot_sound.set_volume(0.0)
					self.duck_hit_sound.set_volume(0.0)
					self.reload_sound.set_volume(0.0)
					pygame.mixer.pause()
				if self.mute_key_count == 2 :
					self.shot_sound.set_volume(1.0)
					self.duck_hit_sound.set_volume(1.0)
					self.reload_sound.set_volume(1.0)
					pygame.mixer.unpause()
					self.mute_key_count = 0

			# If player is in main menu
			elif event.type == self.REFRESH and self.state == Game.MAINMENU :
				self.draw()

			# If player clicks to play
			elif event.type == pygame.MOUSEBUTTONDOWN \
			  and self.state == Game.MAINMENU :
				self.state = Game.PLAYING
				pass

			# If player hasn't clicked
			elif event.type == self.REFRESH and self.state == Game.PLAYING :
				self.duck.move_duck(self.width)
				check_shots_and_lives(self)
				self.draw()


			# If player clicks
			elif event.type == pygame.MOUSEBUTTONDOWN \
			  and self.state == Game.PLAYING :
				self.shot_sound.play()
				mouse_pos = pygame.mouse.get_pos()
				if self.duck.duck_rect.collidepoint(mouse_pos) :
					self.duck_hit_sound.play()
					
					scoring_dict = {0:100, 1:75, 2:50}
					self.score += scoring_dict[self.duck.missed]
					
					self.duck.missed += 1
					self.hit_ducks += 1
					
					# Speed up duck
					ints = range(1,101)
					threes = threes = [i*3 for i in ints]
					if self.hit_ducks in threes :
						self.duck.speed += 0.15

					self.state = Game.DUCK_DYING
					
				else :
					self.duck.missed += 1
					if self.duck.missed > 2 :
						self.state = Game.DUCK_FLYING_AWAY
						self.duck.missed = 0
						self.clear_img = load_image('missed_duck.png')
							
			# If player uses all shots
			elif event.type == self.REFRESH and self.state == Game.DUCK_FLYING_AWAY :
				self.shots = self.clear_img
				self.duck.fly_away()
				if self.duck.duck_rect.y < -110 :
					self.duck.lives -= 1
					check_shots_and_lives(self)
					self.reload_sound.play()
					if self.duck.lives == 0 :
						self.state = Game.GAMEOVER
					else :
						self.state = Game.WAITING
				self.draw()

			elif event.type == self.REFRESH and self.state == Game.WAITING :
				self.duck.wait_duck()
				if self.duck.timer > 3*self.FPS :
					self.duck.timer = 0
					self.duck.reset_duck()
					self.state = Game.PLAYING
				self.draw()

			
			# If player hits duck
			elif event.type == self.REFRESH and self.state == Game.DUCK_DYING :
				check_shots_and_lives(self)
				self.duck.kill_duck()
				if self.duck.duck_rect.y > 620 :
					self.state = Game.PLAYING
					self.duck.missed = 0
					self.duck.duck_rect.x = random.randrange(100, \
											(self.width - 100))
					self.duck.duck_rect.y = 500
					self.duck.reset_duck()
					self.reload_sound.play()
				self.draw()

			# If player loses all lives
			elif event.type == self.REFRESH and self.state == Game.GAMEOVER :
				self.life = self.clear_img
				self.duck.duck_rect.y = 1000
				self.theme_song.fadeout(3000)
				self.draw()

			elif event.type == pygame.MOUSEBUTTONDOWN \
			  and self.state == Game.GAMEOVER :
				self.restart()
				self.state = Game.MAINMENU
				
			else :
				pass # An event type we don't handle

	def draw(self) :
		"""Update the display"""
		# Everything we draw now is to a buffer that is not displayed
		self.screen.fill((255,255,255))

		background = self.background
		rect_bg = background.get_rect()
		self.screen.blit(background, rect_bg)

		# Here is where the font module would make the code shorter as well
		# This block is used to display the scores
		if self.state != Game.MAINMENU :
			score = self.score
			score1 = [int(i) for i in str(score)]
			
			score_file = open('HighScore.txt', 'r')
			high_score = int(score_file.read())
			high_score1 = [int(i) for i in str(high_score)]
			if self.state == Game.GAMEOVER and high_score >= self.score :
				scores = [score1, high_score1]
			else : 
				scores = [score1]
			self.b = 1
			for d in scores : 
				if self.b == 1 :
					# When blitting the current score the at top of the screen
					pos_y = 20
					pos_x = self.width//2
				if self.b == 2 :
					# When blitting the high score in the game over screen
					pos_y = (self.height//16)*7
					pos_x = (self.width//8)*7
				
				self.x_pos = 30*(len(d) - 1)
				for i in d :
					a = self.nums[i]
					
					rect_score = a.get_rect()
					rect_score = rect_score.move(pos_x - self.x_pos, pos_y)
					self.screen.blit(a, rect_score)
					self.x_pos -= 30
					if self.x_pos < 0 :
						self.x_pos = 30*(len(d) - 1)
				self.b = 2

		if self.state != Game.MAINMENU :
			self.screen.blit(self.duck.duck_img, self.duck.duck_rect)

			shots = self.shots
			rect_shots = shots.get_rect()
			rect_shots = rect_shots.move(self.width - \
										(rect_shots.width + 20), 10)
			self.screen.blit(shots, rect_shots)

			lives = self.life
			rect_lives = lives.get_rect()
			rect_lives = rect_lives.move(self.width - \
										(rect_lives.width + 20), 60)
			self.screen.blit(lives, rect_lives)			
		
		foreground = self.foreground
		rect_fg = foreground.get_rect()
		self.screen.blit(foreground, rect_fg)
		
		if self.state == Game.MAINMENU :
			rect_menu = self.menu_txt.get_rect()
			rect_menu = rect_menu.move((self.width - \
										rect_menu.width)//2 +120, 185)
			self.screen.blit(self.menu_txt, rect_menu)

		if self.state == Game.GAMEOVER :
			while self.a == 1 :
				self.end_txt = High_Score(self.score, self.gameovr_txt, \
											self.gameover_high_score)
				self.a += 1
			rect_txt = self.end_txt.get_rect()
			rect_txt = rect_txt.move((self.width - \
									rect_txt.width)//2 +120, 185)
			self.screen.blit(self.end_txt, rect_txt)
			
		self.frame += 1
		
		# Flip bufferes so that new display is now showing 
		pygame.display.flip()

Game().run()
pygame.quit()
sys.exit()