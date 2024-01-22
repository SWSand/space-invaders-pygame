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

     	pygame.Surface((x,y)) : creates a surface that isnt our screen for us to add our hero or enemies on to

      	surface.fill("color") : fills in our surface to make it visible. default color is black

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
 	pygame.mouse.get_pos() : returns tuple relative to the 0,0 location
  	pygame.key.get_pressed() : grabs a dictionary of the status of all keys

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

First thing we will do is create a Surface that we can work on. Keep in mind that the Display screen is not the same as our working Surface. to create a surface you require the "pygame.Surface command. we will begin by declaring a data member which will hold and initiate our Surface and we will give it the OuterSpace.png file

 	# declare your surface in the init method
	self.space_surface = pygame.Surface((800,800))



	# WITHIN, the Run method inside of our game loop we can to use screen.blit to add the surface to our display, afterwards we can add other items on top of this surface
 
 	self.screen.blit(self.space_surface, (0,0))
        self.space_surface.blit(pygame.image.load("OuterSpace.png"),(0,0))


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

	#DONT FORGET TO IMPORT OUR SHIP CLASS!!!

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption('OOP')
        self.clock = pygame.time.Clock()

 	#We create our space surface
        self.space_surface = pygame.Surface((800,800))

        # Create our hero ship
        self._hero = SpaceShip("DurrrSpaceShip.png", 360, 700)

    def run(self):
        while True:

            #This initiates our game loop. Every time it runs it will go through all these checks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screen.blit(self.space_surface, (0,0))
            self.space_surface.blit(pygame.image.load("OuterSpace.png"),(0,0))

            
            self._hero.draw(self.space_surface)


If done corretly, when our main.py runs it should open up a game window with our SpaceShip dead center and a cool looking space background!!

Now all this is cool and all but our ship doesnt do anything just yet, so lets add some functionality. We would like for our spaceship to be able to move left and right to allow it to aim around around screen. To do this we need to be able to capture certain input like either using the arrow keys on our keyboard of the w,a,s,d.

First thing first we can to create a method that is unique only to our SpaceShip that will allow it to move. This method will take in a Str argument which could be "a","d","w","s" and change our x and y coordinates. Think of it as a setter method:

    def move(self, direction):
        if direction == "a":
            if self._x >= 20:
                self._x -= 5
        elif direction == "d":
            if self._x <= 700:
                self._x += 5
        elif direction == "w":
            if self._y >=  300:
                self._y -= 5
        elif direction == "s":
            if self._y <= 700:
                self._y += 5

Once our SpaceShip has a method to move we can begin capturing the necessary Events for it within our Game Loop;

	# The key.get_pressed() method returns a dictionary of status of all keys
	# which we can access to see if theyre pressed or not. Depending on their status
	# we want to move left or move right
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.hero.move("a")
            if keys[pygame.K_d]:
                self.hero.move("d")
            if keys[pygame.K_w]:
                self.hero.move("w")
            if keys[pygame.K_s]:
                self.hero.move("s")
 		
