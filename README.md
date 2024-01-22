# pygame
Extra: Object-Oriented Programming utilizing the Python Pygame module

**Lesson: EXTRA class in object-oriented programming cont.**

In this extra-curricular lecture we will be dicussing classes and objects while utilizing Pythons module Pygame to further improve our understanding and confidence when working with OOP.
Object Oriented programming provides us flexibility in our code allowing us to create reusable code that can be altered without affecting the rest of our program. Using concepts like inheritance and polymorphism we are able to easily create subclasses and overwrite methods
in our children without directly affecting our parent classes. Imagine having the blueprint to a car that allows you to easily recreate different Car types without having to restart from scratch every single time and still have the flexibility to change any features from its parent. That is the power of Classes and objects


**Installing Pygame:**

Pygame is a module that requires Python and Pip. Lucky for you we already installed these during the installfest.


To install pygame use either method 1 or method 2 depending on your system:

Method 1 --> UBUNTU:

	sudo apt-get install python3-pygame

Method 2 --> MAC:

	python3 -m pip install -U pygame --user

After pygame has been installed run the following command on your terminal to test it out. If a window is displayed with a vehicle with a turret and aliens then you're all set ! :

	python3 -m pygame.examples.aliens

**GETTING STARTED**

Now that Pygame is installed we can start putting some code on the screen:

Just like every module up to this point. There are pre-built methods that come with it. When it comes to pygame all these methods can be found on their website under the documentation tab

	https://www.pygame.org/docs/

Unfortunately, this isn't a Pygame lesson. It is an **Object Oriented Programming and Classes** lecture so we won't dwell too much on Pygames library of methods. All the legwork has been done for you and all you need to do is use the boiler plates provided for you. A small description has been added to familiarize you with the module we will be using. Pygame will simply be a tool for us to better visualize classes and objects


Pygame method **CHEATSHEET**


 	# GAME WINDOW

	pygame.init() : Initializes the pygame modules in the code

  	pyame.display.set_mode((size_x, size_y)) : this creates the window and sets its size. Assign this to a variable that will hold your "screen"

   	#IMAGES

   	pygame.image.load("my_image.jpg") : Loads an image. You can assign this to an image variable

	screen.blit(my_image, (my_image_x, my_image_y)) : Adds the image on to your game screen at the location given

	my_image.get_rect().size[1] : when called on an image variable and assigned to a variable ex: image_heigh,  will return the height of an image

	pygame.transform.flip(my_image, False, True) : used on an image, will flip it on its x axis

	object_one.colliderect(object_two) : detects if one object/rect collides with another

 	#EVENTS

  	events = pygame.event.get() : grabs an event and assigns it to a variable

   	#WRTING TO SCREEN
	# Write size 36 turquoise text to the screen
	colour = (0, 255, 255)
	font = pygame.font.Font(None, 36)
	location = (300, 10)
	screen.blit(font.render(“Flippy Bird”, True,
	colour), location)


	#-----------------------------------------------------
 	# CHECKS TO SEE IF THE EVENT IS A PRESSED OR RELEASED KEY
   	if event[0].type == pygame.KEYDOWN:
    		print("A key was pressed!")
      	elif events[0].type == pygame.KEYUP:
       		print("A key was released!")

  	#-------------------------------------------------
   	# CHECKS TO SEE WHICH KEY WAS PRESSED
	if events[0].key == pygame.K_UP:
		print("The up arrow key was pressed!")
	elif events[0].key == pygame.K_DOWN:
		print("The down arrow key was pressed!")
	elif events[0].key == pygame.K_q:
		print("The letter q was pressed!")
  	
	#-----------------------------------------------
 	#PYGAME EVENTS 
	pygame.QUIT
	pygame.ACTIVEEVENT
	pygame.KEYDOWN
	pygame.KEYUP
	pygame.MOUSEMOTION
	pygame.MOUSEBUTTONUP
	pygame.MOUSEBUTTONDOWN

 	#------------------------------------------------
  	# CLOSE THE WINDOW

   
	# Import the system module
	import sys
	# Close the window and exit
	pygame.display.quit()
	sys.exit()

 	#-------------------------------------------------
  	#COMMON KEY CODES IN PYGAME
	pygame.K_SPACE : spacebar
	pygame.K_a/w/s/d : a/w/s/d
	pygame.K_UP/DOWN/LEFT/RIGHT : up arrow/down arrow/left arrow/right arrow
   	


Below, you will find a Boiler Plate template that will open up a BASIC pygame window so that we can begin working. Everything in this code is the necessary foundation for all games using the pygame module. This will be our skeleton for our program.
Begin by creating a directory in which we will hold our game. Within this directory we will create our main.py which will hold our boiler plate. On top of containing our main.py we will be creating other files that will be holding our classes to keep everything seperated and organized. 

	# Example file showing a basic pygame "game loop"
 
	import pygame
	import sys
	
	class Game:

	    def __init__(self):
	        pygame.init()
	        self.screen = pygame.display.set_mode((800,800))
	        pygame.display.set_caption('OOP')
	        self.clock = pygame.time.Clock()

	    def run(self):
	        while True:
	            
	     	    #Every time it loops, it will check if we decided to exit the game or not
	            for event in pygame.event.get():
	                if event.type == pygame.QUIT:
	                    pygame.quit()
	                    sys.exit()

			# <---- WITHIN THIS SPACE WE CAN ADD CODE FOR OUR GAME TO CONDUCT ---->

       
		     
		    #This method is a form of a refresh, and updates our screen
	            pygame.display.update()
	            self.clock.tick(60)

	my_game = Game()
	my_game.run()

Now that we have a window open we can begin working.

**CREATING OUR CHARACTER**

After creating your main.py file with our template, create a seperate file and name it **hero.py**

We will now isolate our Hero code by creating our class in its individual file. For our Hero to properly work we want to ensure he is able to take as arguments an image, and its x and y coordinates. 

	import pygame

	class SpaceShip:

	    def __init__(self, image, x, y):
	        self.image = pygame.image.load(image)
	        self.x = x
	        self.y = y


After we create our SpaceShip we need to code the functionality to allow it to appear in our screen. We can either do this in our game loop or we can just give our class the method for it. In our example we will create the method within our class

	    def draw(self, screen):
	        screen.blit(self.image, (self.x, self.y))


Now that our blueprint ( or CLASS ) for our SpaceShip / Hero has been created we can draw it on our screen: Remember, the way our pixels work on our screen is from top left to bottom right. Therefore if we were to assign our x and y axis as 0,0 our image will appear at the top left corner of our screen. As we increase our x axis it will shift to our right, and going negative will shift it to the left outside of our screen. For the Y axis as we increase the Y axis it will move down our screen and as we go into the negatives it will move up away from our screen. Below is the Code Snippet for what our Spaceship class should look like.

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption('OOP')
        self.clock = pygame.time.Clock()

        # Create our hero ship
        self._hero = SpaceShip("DurrrSpaceShip.png", 350, 350)

    def run(self):
        while True:
            #This initiates our game loop. Every time it runs it will go through all these checks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #we call the .draw method creating in our hero class and pass it the screen data member to draw it in our screen
            self._hero.draw(self.screen)

        

            pygame.display.update()
            self.clock.tick(60)



 		
