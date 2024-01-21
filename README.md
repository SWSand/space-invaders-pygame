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


Below, you will find a Boiler Plate template that will open up a BASIC pygame window so that we can begin working. Everything in this code is the necessary foundation for all games using the pygame module. This will be our skeleton for our program.
Begin by creating a directory in which we will hold our game. Within this directory we will create our main.py which will hold our boiler plate. On top of containing our main.py we will be creating other files that will be holding our classes to keep everything seperated and organized. 

	# Example file showing a basic pygame "game loop"
 
	import pygame
	
	# pygame setup. This will initialize the module for you. Similar to initializing our class and calling an Init method
	pygame.init()
 
 	# declare a variable named screen and initialize it with our desired width and height
	screen = pygame.display.set_mode((1280, 720))

 	#Initiate a clock that keeps track of our framerate
	clock = pygame.time.Clock()
	running = True
	
	while running:
	    # poll for events
	    # pygame.QUIT event means the user clicked X to close your window
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

	pygame.quit()

Now that we have a window open we can begin working.

**CREATING OUR CHARACTER**

After creating your main.py file with our template, create a seperate file and name it **hero.py**
