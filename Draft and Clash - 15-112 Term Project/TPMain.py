########################################
#   Draft and Clash
#   (TPMain.py)
#   By: Leo Serodio
########################################
#   
########################################
#
#   Citations for this file: 
#   1)  Incorporated cmu_graphics syntax from 
#       https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
#   2)  Pictures taken from the google images and links as specified, music cited as specified
#
#   3)  Chatgpt used as specified, and chatgpt used for some comments
#
########################################


def onAppStart(app):
    app.screen = "first"
    # Music and sounds:
    backgroundMus = "cmu://872511/35357121/Joy+Crookes+-+Feet+Don't+Fail+Me+Now+(Lyrics).mp3" # Taken from youtube, "Feet Don't Fail Me Now" by Joy Crookes
    app.backgroundMusic = Sound(backgroundMus)
    crowd = "cmu://872511/35499029/Stadium+Crowd+Sound+Effect.mp3" # Stadium Crowd Sound Effect on youtube, https://www.youtube.com/watch?v=_QCYcMOxWxI
    #goalSound = 'cmu://872511/35583673/Score+a+Goal+Sound+Effect.mp3' # taken from https://www.youtube.com/watch?v=9nt9FEbcI9k
    app.crowd = Sound(crowd)
    #app.goalSound = Sound(goalSound)
    app.isGoal = False
    app.progress = 0 # For loading bar
    app.stage = 1
    app.width=1200
    app.height=650
    app.buttons = { # Initially I was using lists, but chatgpt recommended for me to use a dictionary and it helped me a lot later in "onMousePress" and "redrawAll"
        "play": Button(app.width / 2 - 100, 200, 240, 52, "BEAT RAMOS", "lightGreen", "green"),
        "options": Button(app.width / 2 - 100, 255, 240, 52, "OPTIONS", "lightBlue", "blue"),
        "quit": Button(app.width / 2 - 100, 475, 240, 52, "QUIT", "lightCoral", "red"),
        "back": Button(app.width - 100, 0, 100, 40, "BACK", "lightGray", "gray"),
        "start": Button(app.width / 2 - 75, app.height / 2, 150, 60, "START", "lightblue", "blue"), # Actually, chatgpt did not suggest I use a start game button, but I decided to because I thought it would be better for readability and I like the "hover" feature
        "instructions": Button(app.width / 2 - 100, 310, 240, 52, "INSTRUCTIONS", "plum", "purple"),# hover color is slightly darker than base, used google to find common combinations for this
        "tutorial": Button(app.width / 2 - 100, 365, 240, 52, "TUTORIAL", "lightBlue", "blue"),
        "yes": Button(app.width / 2 + 175, app.height / 2 - 90, 65, 50, "Y", "lightblue", "blue"), # the minus volume button (adapted it to yes or no music)
        "no": Button(app.width / 2 + 270, app.height / 2 - 90, 65, 50, "N", "lightblue", "blue"), # the plus volume button
        "Easy": Button(app.width / 2 + 75, app.height / 2 + 10, 125, 50, "EASY", "lightblue", "blue"), # These are the difficulty buttons that will be used twice throughout the app
        "Hard": Button(app.width / 2 + 210, app.height / 2 + 10, 125, 50, "HARD", "lightblue", "blue"),
        "Extreme": Button(app.width / 2 + 345, app.height / 2 + 10, 125, 50, "EXTREME", "lightblue", "blue"),
        "quitOPT": Button(app.width / 2 - 100, 500, 200, 50, "QUIT", "lightCoral", "red"), # this is a different quit button for the options tab
        "home": Button(app.width / 2 - 125, 500, 250, 50, "MAIN MENU", "lightCoral", "red"), # This button is the return to home screen/main menu button
        "Easy2": Button(app.width / 2 - 210, app.height / 2 + 10, 130, 50, "EASY", "lightblue", "blue"), # These are the difficulty buttons that will be used twice throughout the app
        "Hard2": Button(app.width / 2 + -65, app.height / 2 + 10, 130, 50, "HARD", "lightblue", "blue"),
        "Extreme2": Button(app.width / 2 + 80, app.height / 2 + 10, 130, 50, "EXTREME", "lightblue", "blue"),
        "game": Button(app.width / 2 - 90, app.height - 100, 180, 50, "START GAME", "lightblue", "blue"),
        "pause": Button(760, 0, 275, 40, "CLICK HERE TO PAUSE", "lightGray", "gray"),
        "resume": Button(app.width - 120, 0, 120, 40, "RESUME", "lightGray", "gray"),
        # Now the tutorial buttons
        "next": Button(app.width - 130, app.height - 50, 130, 50, "NEXT", "lightblue", "blue"),
        "backstory": Button(app.width / 2 - 130, app.height - 50, 260, 50, "BACKSTORY", "lightblue", "blue"),
        "menu": Button(app.width - 160, app.height - 50, 160, 50, "MAIN MENU", "lightblue", "blue"),
        "anywhere": Button(0, 0, app.width, app.height, "", None, None), # button to start the game
        "multiplayer": Button(app.width / 2 - 100, 420, 240, 52, "MULTIPLAYER", 'white', "gray"),
        "clash": Button(app.width / 2 - 130, app.height - 50, 260, 50, "CLASH", "lightblue", "blue")
    }
    app.buttonLeft = 150
    app.buttonTop = 250
    app.buttonWidth = 150
    app.buttonHeight = 50
    app.startGame = False
    app.draftPlayers = []  # Initialize the draft players list as empty
    app.selectedPlayer = None # the player we will use
    app.gameStarted = False  # Flag to track if the game has started
    app.backgroundImage = 'cmu://872511/35272232/Screenshot+2024-11-24+173858.png'  # Messi Image taken from google
    app.phase = "welcome" # this is the phase variable, checking whether the phase is welcome, draft or selected
    app.difficulty = "Easy" # Easy by default. 
    # Original sound: Joy Crookes - Feet Don't Fail Me Now (Lyrics) - https://www.youtube.com/watch?v=vUJis1UBI5w
    
    
    
    #
    # ADD STUFF FOR THE ACTUAL GAME
    #
    
    
    # Now the game initializations:
    app.keyPressed = None
    app.kick = False
    app.gamePaused = False
    app.gameOver = False
    app.userCounter = 0
    app.oppCounter = 0
    
    app.woodworks = [
        # For the user goal
        Woodwork(80, 450, 100, 450, 235, 340, 160, 340),
        
        
        # Now for the Ramos goal
        Woodwork(app.width - 65, 450, app.width - 85, 450, 975, 340, 1020, 340),
     
    ]
    
    # For multiplayer
    
    # Add all the players to the dropdown menu choices
    app.allPlayers = ["Cristiano Ronaldo","Lionel Messi","Neymar","Kylian Mbappé","Mohamed Salah","Lewandowski","Kevin De Bruyne","Virgil van Dijk"]
    
    app.player1Menu = DropdownMenu(200, 360, 150, 30, app.allPlayers)
    app.player2Menu = DropdownMenu(935, 360, 150, 30, app.allPlayers)
    app.p1Counter = 0
    app.p2Counter = 0
    

    app.easyOpponent = easyOpponent(app.width - 350, app.height - 230, 60, 135)
    app.hardOpponent = hardOpponent(app.width - 350, app.height - 230, 60, 135)
    app.extremeOpponent = extremeOpponent(app.width - 350, app.height - 230, 60, 135)
    app.user = None # Draft hasn't started yet, we will initialize this to a player object on the mouse press where the user selects a player (Draft)
    app.stepsPerSecond = 10
    app.r = 15
    # Multiplayer initializations
    
    app.ball = SoccerBall(app.width // 2, app.r, 15, 0, 0)  # Initial y position at the top
    
    # Now add the stuff for the backstory:
    app.typingIndex = 0  # the typing index keeps track of how much text has been "typed"
    # This is the full backstory text
    app.fullText = "Hello, my name is Messi. I was told you are here for the true story behind the abandoned Puppet Theater. Well, my friend, you came to the right place. You see, long ago, Neymar and I used to do puppet shows here with other guys like Ronaldo, Van Dijk, you know, those guys. But one day, as we were doing a puppet show, a little boy sitting in a chair fell from his seat, uncovering a soccer field below. Except there weren't any goals, only haunted backstage areas which we call 'Puppet black Holes'. They say a beast in human form, 'Ramos', took the soul of this poor little boy, and if you beat him in a soccer match, you can save him. If not, you're doomed until the next one tries... As a puppet master, I was not allowed to play, but you, you my son, are the only one who can save him. Goodbye."
    app.maxCharsPerLine = 68  # max characters per lines (have to fit into the cartoon bubble)
    app.splitLines = splitTextIntoLines(app.fullText, app.maxCharsPerLine) # This function was both debugged by and also a few minimal lines were added by chatgpt (mostly syntax errors as I was unfamiliar on how to work with time.time())
    app.typedTextLines = [""] * len(app.splitLines)  # The lines that have been "typed" so far, this line was edited by chatgpt
    app.currentLine = 0
    app.typingSpeed = random.uniform(2.5, 3.5)  # The delat between words
    app.lastTypedTime = 0  # Time when the last letter was added



def restart(app): # restart the positions of the players
    if app.screen == "game":
        app.easyOpponent = easyOpponent(app.width - 200, app.height - 230, 60, 135)
        app.hardOpponent = hardOpponent(app.width - 200, app.height - 230, 60, 135)
        app.extremeOpponent = extremeOpponent(app.width - 200, app.height - 230, 60, 135) 
    app.gamePaused = False
    app.gameOver = False
    if app.screen == "game":
        app.user.cx = 280
    elif app.screen == "clash":
        app.p1.cx = 150
        app.p2.cx = app.width - 150
    
    app.ball = SoccerBall(app.width // 2, app.r, 15, 0, 0)  # Initial y position at the top

  
def onMouseMove(app, mouseX, mouseY): # Need this function for the hover functionality
    for button in app.buttons.values():
        button.check_hover(mouseX, mouseY)
    if app.screen == 'multiplayer': # Now the hover for the dropdown menu
        app.player1Menu.check_hover(mouseX, mouseY)
        app.player2Menu.check_hover(mouseX, mouseY)


def redrawAll(app): 
    if app.screen == "first":
        app.buttons["anywhere"].draw()
        drawFirst(app)
        
    
    if app.screen == "loading":
        drawLoading(app)
        
        
    if app.screen == "main":
        # Draw the background picture:
        mainPic = 'cmu://872511/35389505/Screenshot+2024-12-02+122244.png' # Same place as options screen background
        drawImage(mainPic, 0, 0, width=app.width, height=app.height)
        drawLabel("MAIN MENU", app.width / 2 + 10, 130, size=50, bold=True, fill="white", font = "orbitron")
        for button in ["play", "options", "quit", "instructions", "tutorial", "multiplayer"]: # All the buttons that appear in the home screen
            app.buttons[button].draw()
    # FIX THIS
    elif app.screen == "instructions": # We are now in the instructions screen, so we want to print out the intructions of the game (using labels)
        writeInstructions(app)
        app.buttons["back"].draw() # have to draw the back button
    
    
    
    # The tutorial screens now
    elif app.screen == "tutorial1":
        writeTutorial1(app)
        app.buttons["back"].draw()
        app.buttons["next"].draw()
    
    elif app.screen == "tutorial2":
        writeTutorial2(app)
        app.buttons["back"].draw()
        app.buttons["next"].draw()
    
    elif app.screen == "tutorial3":
        writeTutorial3(app)
        app.buttons["back"].draw()
        app.buttons["next"].draw()
        app.buttons["backstory"].draw()
    
    elif app.screen == "backstory":
        writeBackstory(app)
        app.buttons["back"].draw()
        
            
        
    elif app.screen == "play":
        welcomePic = 'cmu://872511/35389505/Screenshot+2024-12-02+122244.png' # Off of google images
        drawImage(welcomePic, 0, 0, width=app.width, height=app.height)
        app.buttons["back"].draw()
        if app.phase == "welcome":
            drawWelcome(app)
            app.buttons["start"].draw() # Instead of the line above, draw button using the Button class so the hover functionality works
            
        elif app.phase == "draft":
            displayDraftChoices(app)
        
        elif app.phase == "selected":
            displaySelectedPlayer(app)
            app.buttons["game"].draw()
    # Now we want the back button to show when we go into options
    elif app.screen == "options":
        writeOptions(app)
        drawOptionLines(app)
        app.buttons["back"].draw()
        app.buttons["yes"].draw() # Draw the volume buttons
        app.buttons["no"].draw()
        app.buttons["Easy"].draw() # Draw the difficulty buttons
        app.buttons["Hard"].draw()
        app.buttons["Extreme"].draw()
        app.buttons["quitOPT"].draw()
    elif app.screen == "quit": # If a quit button was pressed, pan to an "end game" screen.
        drawEnd(app)
        app.buttons["home"].draw() # draw the "main menu" button
    
    elif app.screen == "game": # Now we draw the field
        drawGame(app)
        if app.difficulty == "Easy":
            app.easyOpponent.draw()
        elif app.difficulty == "Hard":
            app.hardOpponent.draw()
        elif app.difficulty == "Extreme":
            app.extremeOpponent.draw()
        
        
    
    if app.screen != "quit" and app.screen != "first" and app.screen != "loading": # Difficulty in top-left for all instances except when the user quits
        drawLabel(f"Difficulty: {app.difficulty.upper()}", 70, 15, font = "orbitron", bold = True) # Always have the difficulty in the top left of the app
    if app.screen == "game" and app.stepsPerSecond != 0: # So there's no pause button when the game is already paused
        app.buttons["pause"].draw()
    
    if app.screen == "pause":
        drawPauseMenu(app)
        
    
    # Add the ending screens
    if app.screen == "badEnding":
        drawBadEnding(app)
        app.buttons["menu"].draw()
    if app.screen == "goodEnding":
        drawGoodEnding(app)
        app.buttons["menu"].draw()
        
    if app.screen == "multiplayer":
        drawMultiplayer(app)
        app.buttons["clash"].draw()
        drawDropdown(app)
        app.buttons["back"].draw()
        
      
    if app.screen == "clash":
        drawClash(app)
        drawClashScore(app)
    
    if app.screen == "p1Won":
        mainPic = 'cmu://872511/35389505/Screenshot+2024-12-02+122244.png' # Same place as options screen background
        drawImage(mainPic, 0, 0, width=app.width, height=app.height)
        drawLabel("Player 1 won!!!", app.width / 2, 300, size = 40, font = "orbitron", bold = True)
        app.buttons["menu"].draw()
        
    if app.screen == "p2Won":
        mainPic = 'cmu://872511/35389505/Screenshot+2024-12-02+122244.png' # Same place as options screen background
        drawImage(mainPic, 0, 0, width=app.width, height=app.height)
        drawLabel("Player 2 won!!!", app.width / 2, 300, size = 40, font = "orbitron", bold = True)
        app.buttons["menu"].draw()
       

def onMousePress(app, mouseX, mouseY): # chatgpt helped me debug this to fix the logic of the home screen (added 3 last lines and fixed a small logic errors), also helped me implement onMousePress after the addition of 'phase'.
    # However all of the rest of the function is my own work(like 99 percent)
    # Anytime the difficulty is changed, update it in the top left corner
    if app.screen == "first":
        if app.buttons["anywhere"].check_click(mouseX, mouseY):
            app.screen = "loading"
   
    if app.buttons["Easy"].check_click(mouseX, mouseY) and app.screen == "options": 
            app.difficulty = 'Easy'
    if app.buttons["Easy2"].check_click(mouseX, mouseY) and app.phase == "selected":
            app.difficulty = 'Easy'
    
    if app.buttons["Hard"].check_click(mouseX, mouseY) and app.screen == "options": 
            app.difficulty = 'Hard'
    if app.buttons["Hard2"].check_click(mouseX, mouseY) and app.phase == "selected":
            app.difficulty = 'Hard'
    
    if app.buttons["Extreme"].check_click(mouseX, mouseY) and app.screen == "options":
            app.difficulty = 'Extreme'
    if app.buttons["Extreme2"].check_click(mouseX, mouseY) and app.phase == "selected":
            app.difficulty = 'Extreme'
            
    if app.screen == "main":
        if app.buttons["play"].check_click(mouseX, mouseY):
            play_screen(app)
        elif app.buttons["options"].check_click(mouseX, mouseY):
            options_screen(app)
        elif app.buttons["quit"].check_click(mouseX, mouseY):
            app.phase = "welcome" # So user can re-draft after quitting
            app.userCounter = 0
            app.oppCounter = 0
            quit_game(app)
        elif app.buttons["instructions"].check_click(mouseX, mouseY):
            instructions_screen(app)
        elif app.buttons["tutorial"].check_click(mouseX, mouseY):
            tutorial1_screen(app)
        elif app.buttons["multiplayer"].check_click(mouseX, mouseY):
            multiplayer_screen(app)
        
    
    # Now if we want to go to options (adjust the music etc.) and back.    
    elif app.screen == "options":
        if app.buttons["yes"].check_click(mouseX, mouseY):
            app.backgroundMusic.play(loop=True) # taken from the notes, play the loop
        if app.buttons["no"].check_click(mouseX, mouseY):
            app.backgroundMusic.pause()
        if app.buttons["back"].check_click(mouseX, mouseY): 
            app.screen = "main"
        elif app.buttons["quitOPT"].check_click(mouseX, mouseY): # Other quit button
            app.userCounter = 0
            app.oppCounter = 0
            quit_game(app)
    
    
    # Now these are the instructions, where I just quickly describe the game for the user => we can also go back to the menu with the 'back' button
    elif app.screen == "instructions":
        if app.buttons["back"].check_click(mouseX, mouseY): 
            app.screen = "main"
            
    elif app.screen == "play":
        if app.buttons["back"].check_click(mouseX, mouseY): # Have a Back button to Main Menu
            app.screen = "main"
        
        if app.phase == "welcome" and app.buttons["start"].check_click(mouseX, mouseY):
            app.phase = "draft"
            startDraft(app)
        elif app.phase == "draft": 
            for i, button in enumerate(app.draftButtons): # this line was edited by chatgpt
                if button.check_click(mouseX, mouseY):
                    app.selectedPlayer = app.draftPlayers[i] # assign the selected player
                    createSelectedPlayer(app) # This line creates the physical object (app.user) which is the player object containing the selected player's stats
                    app.phase = "selected"  # Move to the selected phase
                    break # this break line was added by chatgpt for debugging purposes
    elif app.screen == "quit":
        if app.buttons["home"].check_click(mouseX, mouseY):
            app.screen = "main" # If the user presses the main menu button, the game goes back to the main menu
    
    # The tutorial logic
    elif app.screen == "tutorial1":
        if app.buttons["back"].check_click(mouseX, mouseY):
            app.screen = "main" # return to main menu
        if app.buttons["next"].check_click(mouseX, mouseY):
            tutorial2_screen(app)
    
    elif app.screen == "tutorial2":
        if app.buttons["back"].check_click(mouseX, mouseY):
            app.screen = "tutorial1" # return to last slide
        if app.buttons["next"].check_click(mouseX, mouseY):
            tutorial3_screen(app)
    
    elif app.screen == "tutorial3":
        if app.buttons["back"].check_click(mouseX, mouseY):
            app.screen = "tutorial2" # return to last slide
        if app.buttons["next"].check_click(mouseX, mouseY):
            instructions_screen(app)
        if app.buttons["backstory"].check_click(mouseX, mouseY):
            backstory_screen(app)
    
    elif app.screen == "backstory":
        if app.buttons["back"].check_click(mouseX, mouseY):
            app.screen = "tutorial3" # return to last slide
            
    
    if app.phase == "selected": # Transition to game
        if app.buttons["game"].check_click(mouseX, mouseY):
            game_screen(app) # now the screen is set to "game"
            app.stepsPerSecond = 120
    if app.screen == "backstory":
        app.stepsPerSecond = 120 # I felt 30 was quite slow, so I set it to 120
    
    
    if app.screen == "game":
        app.backgroundMusic.pause() # Pause the background music during the game automatically
        app.crowd.play(loop=True)
        if app.buttons["pause"].check_click(mouseX, mouseY):
            app.stepsPerSecond = 0
            pause_menu(app)
            
             # This function will move to a new screen, and we will set the app.stepsPerSecond to 0 (pausing the game), and have a button 
             
    if app.screen == "pause":
        app.crowd.pause()
        if app.buttons["resume"].check_click(mouseX, mouseY):
            game_screen(app) # Now we resume the game
            app.crowd.play(loop=True)
            app.stepsPerSecond = 120
        if app.buttons["quit"].check_click(mouseX, mouseY):
            restart(app)
            app.userCounter = 0
            app.oppCounter = 0
            app.phase = "welcome"
            app.screen = "quit"
        if app.buttons["menu"].check_click(mouseX, mouseY):
            restart(app)
            app.userCounter = 0
            app.oppCounter = 0
            app.phase = "welcome"
            app.screen = "main"
            
    # Ending screen logic
    if app.screen == "goodEnding":
        app.crowd.pause()
        if app.buttons["menu"].check_click(mouseX, mouseY):
            app.phase = "welcome" # Reset the draft
            app.screen = "main" # Back to the main menu
    # Same for other ending
    if app.screen == "badEnding":
        app.crowd.pause()
        if app.buttons["menu"].check_click(mouseX, mouseY):
            app.phase = "welcome" 
            app.screen = "main" 
    
    if app.screen == "multiplayer":
        if app.buttons["back"].check_click(mouseX, mouseY):
            main_menu(app)
        # Check the dropdown(from class)
        # Chatgpt helped me with this logic as I was initially initializing the players in onAppStart, which would mean the app.p1 and app.p2 would be None and therefore crash
        clicked1 = app.player1Menu.check_click(mouseX, mouseY)
        clicked2 = app.player2Menu.check_click(mouseX, mouseY)
        player1_name = app.player1Menu.selected
        player2_name = app.player2Menu.selected
        if player1_name:
            app.p1 = Player(player1_name, "Country1", 90, 150, app.height - 150)  # Example initialization with default position
        if player2_name:
            app.p2 = Player(player2_name, "Country2", 90, app.width - 150, app.height - 150)
            app.p2.vx = -1 # so the player starts facing towards the middle
        
        # If neither of them were clicked, close any open menus(so both if both were open)
        if not clicked1 and not clicked2:
            app.player1Menu.close()
            app.player2Menu.close()
        if app.buttons["clash"].check_click(mouseX, mouseY) and player1_name and player2_name and app.phase != "selected": # check if the players were selected
            app.screen = "clash"
        
    
    if app.screen == "clash":
        app.backgroundMusic.pause() # Pause the background music during the game automatically
        app.crowd.play(loop=True)
        clash_screen(app)
        app.stepsPerSecond = 120
        
    
    if app.screen == "p2Won" or app.screen == "p1Won":
        app.crowd.pause()
        app.p1Counter = 0
        app.p2Counter = 0
        if app.buttons["menu"].check_click(mouseX, mouseY):
            main_menu(app)

def onStep(app): # This onStep method was adapted by me from watching the TA-Led mini lecture on physics and object collisions
    
    # Logic for multiplayer mode
    if app.phase != "selected":
        if app.screen == "clash":
            # Kick logic for multiplayer
            if app.p1.kicked:
                app.p1.resetKick()
            if app.p2.kicked:
                app.p2.resetKick()
            app.p1.boundPlayer(app) # make sure both players stay in the field
            app.p2.boundPlayer(app) 
             

            
            app.p1.applyGravity(400, 0.02, app.height, app)  # Apply gravity (pass app.height as ground_y) self.gravity = 0.15 self.jump_strength = -6
            app.p1.updatePosition(0.0235)  # Update player position
            
            # do the same for player 2(p2)
            app.p2.applyGravity(400, 0.02, app.height, app)  # Apply gravity (pass app.height as ground_y) self.gravity = 0.15 self.jump_strength = -6
            app.p2.updatePosition(0.0235)  # Update player position
            
        
            # Check for collision with the players and the ball(can use same ball as "beat Ramos" story mode)
            app.p1.collideWithBall(app.ball)
            app.p2.collideWithBall(app.ball)
        
            # Update ball position using gravity and horizontal velocity
            gravity_strength = 0.0085 # set this as gravity strength for multiplayer
            app.ball.cy, app.ball.yv = Gravity.falling(app.ball.cy, app.ball.yv, 400, gravity_strength)
            app.ball.cx = Gravity.moveXDir(app.ball.cx, app.ball.xv, 0.0235)
            
            # Simulating small friction
            if app.height - app.ball.r - 1 <= app.ball.cy <= app.height - app.ball.r + 1:
                app.ball.xv *= 0.99  
            
            # Goal logic here:
            checkGoalMultiplayer(app) # call the function
            
            
            # Screen boundaries for ball, adjust as needed for multiplayer
            # Ground collision
            if app.ball.cy >= app.height - 130 - app.ball.r:  # Adjusted for the ground height
                app.ball.cy = app.height - 130 - app.ball.r  # Place ball at new ground position
                app.ball.yv = -app.ball.yv * 0.75  # Apply bounce with some energy loss
                if abs(app.ball.xv) < 20:  # Add horizontal bias when velocity is low, these two lines were added by chatgpt(adds some realism)
                    app.ball.xv += random.choice([-5, 5])
            
            # Ceiling collision
            if app.ball.cy <= app.ball.r:  # Ball hits the ceiling
                app.ball.cy = app.ball.r
                app.ball.yv = -app.ball.yv * 0.75  # Bounce off ceiling
            
            # Right wall collision
            if app.ball.cx >= 1120 and app.ball.cy <= 360:  # Ball hits the right wall
                app.ball.cx = 1120
                app.ball.xv = -app.ball.xv * 0.75  # Bounce off right wall
            
            # Left wall collision
            if app.ball.cx <= 75 and app.ball.cy <= 360:  # Ball hits the left wall
                app.ball.cx = 75
                app.ball.xv = -app.ball.xv * 0.75  # Bounce off left wall
            
      
    # Loading screen logic
    if app.screen == "loading":
        loadingOnStep(app)
       
       
       
    # Update player position with gravity
    if app.screen == "backstory":
        current_time = time.time()
        if app.currentLine < len(app.splitLines):
            current_text = app.splitLines[app.currentLine]
            if app.typingIndex < len(current_text):
                # Calculate delay based on typing speed
                delay = 1 / (app.typingSpeed * 20)  # This is around 20 characters per word, chatgpt helped me do this math
                # Initially, the delay was 5, but 20 looked better visually
                if current_time - app.lastTypedTime >= delay:
                    app.typedTextLines[app.currentLine] += current_text[app.typingIndex]
                    app.typingIndex += 1  # Move to the next character
                    app.lastTypedTime = current_time
                    # Update typing speed randomly
                    app.typingSpeed = random.uniform(0.5, 2.5)
            else:
                # Move to the next line if current line is fully typed
                app.currentLine += 1
                app.typingIndex = 0
    
    elif app.screen == "game":
        if app.user != None:
            
            app.user.boundPlayer(app) # make sure the user stays in the field 
            
            
            # Deal with the kick feature, use time so the user is only 0.35 seconds within the kick animation
            if app.user.kicked:
                app.user.resetKick() 
            if app.difficulty == "Easy":
                app.easyOpponent.easyMove(app)
            if app.difficulty == "Hard":
                app.hardOpponent.hardMove(app.ball.cx, app.width, app)
            if app.difficulty == "Extreme":
                app.extremeOpponent.extremeMove(app.ball.cx, app)
            
            app.user.applyGravity(400, 0.02, app.height, app)  # Apply gravity (pass app.height as ground_y) self.gravity = 0.15 self.jump_strength = -6
            app.user.updatePosition(0.0235)  # Update player position
            
            # Check for collision with the opponent
            if app.difficulty == "Easy":
                checkCollision(app.ball, app.easyOpponent)
            if app.difficulty == "Hard":
                checkCollision(app.ball, app.hardOpponent)
            if app.difficulty == "Extreme":
                checkCollision(app.ball, app.extremeOpponent)
        
            # Check for collision with the player
            app.user.collideWithBall(app.ball)
        
            # Update ball position using gravity and horizontal velocity
            gravity_strength = 0.0085 # set this as gravity strength for singelplayer(beat Ramos)
            app.ball.cy, app.ball.yv = Gravity.falling(app.ball.cy, app.ball.yv, 400, gravity_strength)
            app.ball.cx = Gravity.moveXDir(app.ball.cx, app.ball.xv, 0.0235)
            
            # Simulating friction
            if app.height - app.ball.r - 1 <= app.ball.cy <= app.height - app.ball.r + 1:
                app.ball.xv *= 0.99  
            
            
            # Goal logic here:
            checkGoal(app) # call the function
            
            
            # Screen boundaries for ball
            # Ground collision
            if app.ball.cy >= app.height - 120 - app.ball.r:  # Adjusted for new ground height
                app.ball.cy = app.height - 120 - app.ball.r  # Place ball at new ground position
                app.ball.yv = -app.ball.yv * 0.75  # Apply bounce with some energy loss
                if abs(app.ball.xv) < 20:  # Add horizontal bias when velocity is low, these two lines were added by chatgpt
                    app.ball.xv += random.choice([-30, 30])
            
            
            # These collision numbers were edited by chatgpt
            # Ceiling collision
            if app.ball.cy <= app.ball.r:  # Ball hits the ceiling
                app.ball.cy = app.ball.r
                app.ball.yv = -app.ball.yv * 0.75  # Bounce off ceiling
            
            # Right wall collision (bounces off when above the goal)
            if app.ball.cx >= 1010:  # Ball hits the right wall above the goal
                app.ball.cx = 1010
                app.ball.xv = -app.ball.xv * 0.75  # Bounce off the right wall
            
            # Left wall and right wall collisions (bounces off when above the goal)
            if app.ball.cx <= 220:  # Ball is above the goal
                app.ball.cx = 220
                app.ball.xv = -app.ball.xv * 0.75  # Bounce off the right wall
            
            # Collision near the lower part of the walls, slightly above the ground
            
            for w in app.woodworks: # these lines were adapted from the TA-Led mini lecture and edited by chatgpt
                for i in range(4):  # Loop through each edge of the woodwork
                    x1, y1 = w.corners[i]
                    x2, y2 = w.corners[(i + 1) % 4]  # Wrap around to connect the last point to the first
            
                    # Find the closest point on the edge to the ball
                    line_length_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
                    if line_length_squared == 0:  # If the edge is a single point
                        closest_x, closest_y = x1, y1
                    else:
                        # Project the ball's center onto the edge, clamping t between 0 and 1
                        t = max(0, min(1, ((app.ball.cx - x1) * (x2 - x1) + (app.ball.cy - y1) * (y2 - y1)) / line_length_squared))
                        closest_x = x1 + t * (x2 - x1)
                        closest_y = y1 + t * (y2 - y1)
            
                    # Check if the ball is colliding with this edge
                    if distance(app.ball.cx, app.ball.cy, closest_x, closest_y) < app.ball.r:
                        # Restart the game on collision
                        restart(app) # restart the game if the ball is touching the "untouchable" woodworks
                        return  # Exit the function entirely to avoid further processing, this line added by chatgpt

# Player movement
def onKeyPress(app, key): 
    # Game reacts to key presses(Story Mode)
    if app.screen == "game":
        if key == "w":
            app.user.moveUp(app.ball)  
        elif key == "a":
            if app.user.cx >= 150:
                app.user.moveLeft()  
        elif key == "d":
            if app.user.cx <= app.width - 200:
                app.user.moveRight(app)  # moves the player depending on user input
        elif key == "s":
            app.user.stopMoving()
        elif key == "e":
            app.user.kick(app.ball)
        elif key == "p":
            app.stepsPerSecond = 0
            pause_menu(app)
    
    # Multiplayer Mode
    elif app.screen == "clash": 
        if key == "w":
            app.p1.moveUp(app.ball)  
        elif key == "a":
            if app.p1.cx >= 150:
                app.p1.moveLeft()  
        elif key == "d":
            if app.p1.cx <= app.width - 200:
                app.p1.moveRight(app)  # moves the player depending on user input
        elif key == "s":
            app.p1.stopMoving()
        elif key == "e":  # Player 1 kick
            app.p1.kick(app.ball)
        elif key == "p":
            app.stepsPerSecond = 0
            
        # now for p2:
        if key == "up":
            app.p2.moveUp(app.ball)  
        elif key == "left":
            if app.p2.cx >= 150:
                app.p2.moveLeft()  
        elif key == "right":
            if app.p2.cx <= app.width - 200:
                app.p2.moveRight(app)  # moves the player depending on user input
        elif key == "down":
            app.p2.stopMoving()
        elif key == "/":  # Player 2 kick
            app.p2.kick(app.ball)
        elif key == "p":
            app.stepsPerSecond = 0
        
        
            
def main():
    runApp()

main()

#
# END OF TPMAIN
#