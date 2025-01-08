########################################
#   Draft and Clash
#   (GUIFunctions.py)
#   By: Leo Serodio
########################################
#   
########################################
#
#   Citations for this file: 
#   1)  Incorporated cmu_graphics syntax from 
#       https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
#   2)  Pictures taken from the google images and links as specified
#
#   3)  Chatgpt used as specified, and chatgpt used for some comments
#
########################################


# These functions adapted from the video I watched (https://www.youtube.com/watch?v=GMBqjxcKogA), essentially just set the screen to whatever I want to display which is then used in redrawAll to form the "screen"
def writeInstructions(app):# I just made a quick intructions method to make redrawAll a little cleaner
    welcomePic = 'cmu://872511/35389505/Screenshot+2024-12-02+122244.png' # picture taken from google images, 'soccer background cartoon'
    drawImage(welcomePic, 0, 0, width=app.width, height=app.height)
    
    drawLabel('How to play Draft and Clash:', app.width / 2, 60, 
                      size=18, fill='white', font='orbitron', bold = True)
    drawLabel('Draft and Clash is a soccer insipired 1vs1 game featuring a player and an opponent'
                                                            , app.width / 2, 90, 
                      size=15, fill='white', font='orbitron', bold = True)                  
    drawLabel('Step 1 - Draft your players: You will be given a choice of 3 players, and you must choose one.'
                                                            , app.width / 2, 115, 
                      size=15, fill='white', font='orbitron', bold = True)
    drawLabel('Step 2 - Choose your difficulty: The difficulty options are;'
                                                            , app.width / 2, 140, 
                      size=15, fill='white', font='orbitron', bold = True)
    drawLabel('Easy, Hard, or Extreme. Choose carefully...'
                                                            , app.width / 2, 165, 
                      size=15, fill='white', font='orbitron', bold = True)
    drawLabel('Step 3: WIN!!! Score 5 goals to beat your opponent!'
                                                            , app.width / 2, 190, 
                      size=15, fill='white', font='orbitron', bold = True)
                      
    
    
    # Draw white square for UI
    drawRect(65, 230, app.width - 130, 350, fill = 'white', border = 'black', borderWidth = 5)
    # Draw fake grass underneath player
    drawRect(70, 480, 1060, 95, fill = 'green')
    
    
    
    drawLine(270, 230, 270, 580, fill = 'black', lineWidth = 4)
    drawLine(480, 230, 480, 580, fill = 'black', lineWidth = 4)
    drawLine(700, 230, 700, 580, fill = 'black', lineWidth = 4)
    drawLine(920, 230, 920, 580, fill = 'black', lineWidth = 4)
    
    jumpImg = 'cmu://872511/35463532/Screenshot_2024-12-03_230451-removebg-preview+(1).png' # taken from google images
    leftImg = 'cmu://872511/35463500/Screenshot_2024-11-27_223709-removebg-preview.png' # taken from google images
    rightImg = 'cmu://872511/35463496/Screenshot_2024-11-27_223728-removebg-preview.png' # taken from google images
    kickImg = 'cmu://872511/35463486/Screenshot_2024-12-03_225940-removebg-preview.png'
    stopImg = 'cmu://872511/35463555/Screenshot_2024-12-03_230905-removebg-preview.png'
    
    drawImage(jumpImg, 140, 250, width=40, height=40)
    drawImage(leftImg, 350, 250, width=40, height=40) # 25 is half of 50, which is the width of the image, which centers it
    drawImage(rightImg, app.width / 2 - 30 , 250, width=40, height=40)
    drawImage(kickImg, app.width / 2 + 190, 250, width=40, height=40)
    drawImage(stopImg, app.width / 2 + 410, 250, width=40, height=40)
    drawLabel('Press "W" to jump.', app.width / 2 - 430, 310, size=14, fill='black', font='orbitron', bold = True)
    drawLabel('Press "A" to move left.', app.width / 2 - 220, 310, size=14, fill='black', font='orbitron', bold = True)
    drawLabel('Press "D" to move right.', app.width / 2 - 5, 310, size=14, fill='black', font='orbitron', bold = True)
    drawLabel('Press "E" to kick.', app.width / 2 + 215, 310, size=14, fill='black', font='orbitron', bold = True)
    drawLabel('Press "S" to stop.', app.width / 2 + 430, 310, size=14, fill='black', font='orbitron', bold = True)
    
    
    body = playerBodies["Lewandowski"] # Body image of Lewa
    kick = playerKicks["Lewandowski"] # Kicking image of Lewa
    drawImage(body, 140, 330, width=50, height=125)
    drawImage(body, 560, 360, width=50, height=125)
    drawImage(body, 350, 360, width=50, height=125)
    drawImage(body, 1010, 360, width=50, height=125)
    drawImage(kick, 760, 360, width=100, height=125)
    
    drawLine(220, 410, 220, 340, arrowEnd=True) # Up
    drawLine(410, 340, 340, 340, arrowEnd=True) # Left
    drawLine(550, 340, 620, 340, arrowEnd=True) # Right
    
# All GUI stuff here
def writeOptions(app):
        welcomePic = 'cmu://872511/35389505/Screenshot+2024-12-02+122244.png' # picture taken from google images, 'soccer background cartoon'
        drawImage(welcomePic, 0, 0, width=app.width, height=app.height)
        drawLabel("OPTIONS:", app.width / 2, 100, size=30, bold=True, fill=rgb(165,0,0), align="center", font = "orbitron")
        drawLabel("MUSIC ON/OFF:", app.width / 2 - 175, app.height / 2 - 70, size=40, bold=True, fill=rgb(165,0,0), font = "orbitron")
        drawLabel("SET DIFFICULTY:", app.width / 2 - 170, app.height / 2 + 30, size=40, bold=True, fill=rgb(165,0,0), font = "orbitron")

def drawOptionLines(app): # This function 'decorates' the options tab by adding some lines to make the tab look more organized
    drawLine(0, app.height / 2 - 120, app.width, app.height / 2 - 120, fill=rgb(215, 215, 215), # offwhite color
         lineWidth=5)
    drawLine(0, app.height / 2 - 20, app.width, app.height / 2 - 20, fill=rgb(215, 215, 215),
         lineWidth=5)
    drawLine(0, app.height / 2 + 80, app.width, app.height / 2 + 80, fill=rgb(215, 215, 215),
         lineWidth=5)
        
def drawWelcome(app):
    drawLabel('Welcome to Draft and Clash!', app.width / 2, 65, size=40, bold=True, 
                      fill='white', font='orbitron')
    drawLabel('Click the "start" button below to begin your adventure.', app.width / 2, 110, 
                      size=18, fill='white', font='orbitron', bold = True)
    drawLabel('Make sure you have read the instructions!!!', app.width / 2, 140, 
                      size=18, fill='white', font='orbitron', bold = True)
    drawImage(app.backgroundImage, app.width / 2 - 75, app.height / 2  - 150, width=150, height=150)
    
    # Draw the lines around the Messi picture for aesthetics:
    drawLine(app.width / 2 - 75, app.height / 2 - 150, app.width / 2 + 75, app.height / 2 - 150, fill='blue', lineWidth=2)  # Top
    drawLine(app.width / 2 + 75, app.height / 2 - 150, app.width / 2 + 75, app.height / 2, fill='red', lineWidth=2)  # Right
    drawLine(app.width / 2 + 75, app.height / 2, app.width / 2 - 75, app.height / 2, fill='blue', lineWidth=2) # Bottom
    drawLine(app.width / 2 - 75, app.height / 2, app.width / 2 - 75, app.height / 2 - 150, fill='red', lineWidth=2) # Left
    # Now the lines around the start button
    drawLine(app.width / 2 - 75, app.height / 2 + 60, app.width / 2 + 75, app.height / 2 + 60, fill='red', lineWidth=2)  # Bottom
    drawLine(app.width / 2 - 75, app.height / 2, app.width / 2 - 75, app.height / 2 + 60, fill='blue', lineWidth=2)  # Left
    drawLine(app.width / 2 + 75, app.height / 2, app.width / 2 + 75, app.height / 2 + 60, fill='blue', lineWidth=2)  # Right
    
def drawEnd(app): # Ending screen
    mainPic = 'cmu://872511/35389505/Screenshot+2024-12-02+122244.png' # Same place as options screen background
    drawImage(mainPic, 0, 0, width=app.width, height=app.height)
    drawLabel("Thanks for playing!", app.width / 2, 250, size = 45, fill = 'white', bold = True, font = "orbitron")
    drawLabel("Click below to return to the main menu.", app.width / 2, 350, size = 30, fill = 'white', bold = True, font = "orbitron")
    
 
 


# Soccer stats and players

# Players dictionary, initially had a list but chatgpt recommended a dictionary instead
playersDict = {
    "Lionel Messi": {"country": "Argentina", "speed": 90},
    "Cristiano Ronaldo": {"country": "Portugal", "speed": 90},
    "Neymar": {"country": "Brazil", "speed": 90},
    "Kylian Mbappé": {"country": "France", "speed": 90},
    "Mohamed Salah": {"country": "Egypt", "speed": 90},
    "Lewandowski": {"country": "Poland", "speed": 90},
    "Kevin De Bruyne": {"country": "Belgium", "speed": 90},
    "Virgil van Dijk": {"country": "Netherlands", "speed": 90}
}


# Function to create players with their given stats
# Although chatgpt had the idea of the dictionary, I implemented this based off of the logic of the dictionary
def createPlayers(playersDict):
    players = []
    for name, stats in playersDict.items():
        country = stats['country']
        speed = stats['speed']
        cx, cy = 0, 0 # Initialize the cx and the cy, they don't matter in the draft phase
        players.append(Player(name, country, speed, cx, cy))
    return players

def drawStadium(app): # Got the images from google
    #image_path = 'cmu://872511/35358785/Screenshot+2024-11-30+174646.png'
    image_path = 'cmu://872511/35359655/Screenshot+2024-11-30+231239.png' # Puppet theatre picture off of google
    #image_path = 'cmu://872511/35359385/Screenshot+2024-11-30+214544.png'
   
    
    drawImage(image_path, 220, 0, width=app.width - 430, height=app.height // 2)
    #drawImage(image_path, 0, 0, width=app.width, height=app.height // 2)# without the width = and the height =, it wasn't working -> chatgpt fixed it for me

def drawBound(app): # draw the bricks which are the boundary of the game
    image_path1 = 'cmu://872511/35359409/Screenshot+2024-11-30+215348.png'
    image_path2 = 'cmu://872511/35359427/Screenshot+2024-11-30+220110.png'
    drawImage(image_path1, app.width - 220, 0, width=250, height=app.height - 245)
    drawImage(image_path2, 0, 0, width=220, height=app.height - 220)
 
def drawScore(app):
    scoreboard = 'cmu://872511/35564272/Screenshot_2024-11-30_232148-removebg-preview+(1).png' # image off of google images 'head soccer scoreboard'
    # Now draw the scoreboard
    drawRect(445, 0, 310, 155, fill = 'black', border = 'black', borderWidth = 5) # background to the scoreboard
    drawImage(scoreboard, app.width / 2 - 150, 0, width=300, height=150)
    
    
    # Draw the rectangles over the scoreboard
    drawRect(475, 75, 40, 50, fill = rgb(50,50,50)) # Used rgb color picker for these rgb values
    drawRect(580, 75, 40, 60, fill = rgb(100,2,2))
    drawRect(685, 75, 40, 50, fill = rgb(50,50,50))
    #Draw the current scores
    drawLabel(f"{app.userCounter}", 495, 100, size=25, fill='white', font = "orbitron", bold = True)
    drawLabel(f"{app.oppCounter}", 700, 100, size=25, fill='white', font = "orbitron", bold = True)
    
    # Now the time
    #drawLabel(f"{app.oppCounter}", 666, 355, size=12, fill='white', font = "orbitron", bold = True)
    
def drawField(app): # Got the image from google
  
    image_path = 'cmu://872511/35358773/Screenshot+2024-11-30+173915.png'
    drawRect(0, app.height * 2 // 3, app.width, app.height // 3, fill = 'green')
    drawImage(image_path, 0, app.height * 2 // 3, width=app.width, height=app.height // 3)

def drawBrick(app): # Draw the rest of the game, got the image from google "Brick Wall"
    
    image_path = 'cmu://872511/35358801/Screenshot+2024-11-30+175318.png'
    drawImage(image_path, 250, app.height // 2, width=app.width - 500, height=app.height // 5)


def drawGame(app):
    stadium_image = 'cmu://872511/35429989/Screenshot+2024-12-03+104556.png' # AI generated image off of copilot
    drawImage(stadium_image, 0, 0, width=app.width, height=app.height)
    drawScore(app)
    drawCircle(app.ball.cx, app.ball.cy, app.ball.r, fill=None)
    
    # Draw the soccer ball
    ball_image = 'cmu://872511/35359981/SBall.png' # "soccer ball cartoon" off of google images
    image_width = 45  
    image_height = 45  
    image_x = app.ball.cx - image_width / 2
    image_y = app.ball.cy - image_height / 2
    drawImage( ball_image, image_x, image_y, width=image_width, height=image_height)
    sign = 'cmu://872511/35590291/Screenshot+2024-12-06+122811.png' # "Out of order sign" from google images
    goal1_net = 'cmu://872511/35566820/NETLEFT.png' # 'Cartoon goal net' off of google images
    goal2_net = 'cmu://872511/35566821/NETRIGHT.png' # 'Cartoon goal net' off of google images
    goal1_image = 'cmu://872511/35560547/Screenshot_2024-12-05_162008-removebg-preview.png' # 'Cartoon Goal' off of google images
    goal2_image = 'cmu://872511/35560617/Screenshot_2024-12-05_162008-removebg-preview2.png' # Just flipped the image
    drawImage(goal1_net, 180, 350, width=52, height=195)
    drawImage(goal2_net, 980, 350, width=53, height=195)
    drawImage(goal1_image, 180, 350, width=60, height=195)
    drawImage(goal2_image, 980, 350, width=60, height=195)
    drawImage(sign, 120, 440, width=30, height=30)
    drawImage(sign, 1080, 440, width=30, height=30)
    
    if app.user != None:
        app.user.draw(app)
    # Lines from TA-led mini lecture on object collisions and gravity
    for post in app.woodworks:
        post.draw()
   
    
    
        
def drawMultiplayer(app): # This function will draw the multiplayer screen with the instructions for multiplayer
    background = 'cmu://872511/35565128/Screenshot+2024-12-05+214630.png' # 'Cartoon Soccer field birds-eye view' off of google images
    drawImage(background, 0, 0, width=app.width, height=app.height)
    drawRect(60, 41, 1080, 385, fill = 'white', border = 'black', borderWidth = 5)
    drawLabel("Welcome to the Multiplayer game mode!", app.width / 2, 75, size = 22, bold = True, font = "orbitron")
    drawLabel("Although you may have played the 'Beat Ramos' Mode, this mode is slightly different", app.width / 2, 125, size = 22, bold = True, font = "orbitron")
    drawLabel("You will face off against another user with a few new rules...", app.width / 2, 175, size = 22, bold = True, font = "orbitron")
    drawLabel("The stadium is now different (Multiplayer Stadium) and Player 2 has new controls", app.width / 2, 225, size = 22, bold = True, font = "orbitron")
    drawLabel("The controls for Player 1 remain the same, but now for Player 2:", app.width / 2, 275, size = 22, bold = True, font = "orbitron")
    drawLabel("'Up' is jump, 'left' is left, 'right' is right, 'down' is stop, and '/' is kick", app.width / 2, 325, size = 22, bold = True, font = "orbitron")
    
def drawClash(app): # Draw the multiplayer game
    background = 'cmu://872511/35564810/Screenshot+2024-12-05+211520.png'
    drawImage(background, 0, 0, width=app.width,height=450)
    goal1_net = 'cmu://872511/35566820/NETLEFT.png' # 'Cartoon goal net' off of google images
    goal2_net = 'cmu://872511/35566821/NETRIGHT.png' # 'Cartoon goal net' off of google images
    goal1_image = 'cmu://872511/35560547/Screenshot_2024-12-05_162008-removebg-preview.png' # 'Cartoon Goal' off of google images
    goal2_image = 'cmu://872511/35560617/Screenshot_2024-12-05_162008-removebg-preview2.png' # Just flipped the image
    
    multiplayer_field = 'cmu://872511/35538141/Screenshot+2024-12-05+113359.png'
    drawImage(multiplayer_field, 0, app.height - 250, width=app.width, height=250)
    # Draw ball
    ball_image = 'cmu://872511/35359981/SBall.png' # "soccer ball cartoon" off of google images
    image_width = 45  
    image_height = 45  
    image_x = app.ball.cx - image_width / 2
    image_y = app.ball.cy - image_height / 2
    drawImage( ball_image, image_x, image_y, width=image_width, height=image_height)
    # Draw Players
    
    app.p1.draw(app)
    app.p2.draw(app)
    # Draw Goals
    drawImage(goal1_net, 0, 343, width=52, height=195)
    drawImage(goal2_net,app.width - 57, 345, width=53, height=195)
    drawImage(goal1_image, 0, 345, width=60, height=195)
    drawImage(goal2_image, app.width - 60, 345, width=60, height=195)
    
def drawClashScore(app): # Draw the multiplayer scoreboard
    drawRect(app.width / 2 - 220, 0, 440, 140, fill = 'white', border = 'black', borderWidth = 3)
    drawLabel(f"{app.p1.name}", 490, 30, size = 20, font = "orbitron", bold = True)
    drawLabel(f"{app.p1Counter}", 490, 105, size = 30, font = "orbitron", bold = True)
    drawLabel(f"{app.p2.name}", 708, 30, size = 20, font = "orbitron", bold = True)
    drawLabel(f"{app.p2Counter}", 708, 105, size = 30, font = "orbitron", bold = True)
    drawLine(600, 0, 600, 140, lineWidth = 3)
    drawLine(app.width / 2 - 220, 65, app.width / 2 + 220, 65, lineWidth = 3)
    
    

# Snake case for these functions make them stand out which made it easier for me to work with them (also in the GUI video linked above they used snake case) 
def first_screen(app):
    app.screen = "first"

def loading_screen(app):
    app.screen = "loading"
    
        
def play_screen(app): 
    app.screen = "play"
    

def options_screen(app):
    app.screen = "options"

def instructions_screen(app):
    app.screen = "instructions"

def game_screen(app):
    app.screen = "game"

    
def multiplayer_screen(app):
    app.screen = "multiplayer"

def clash_screen(app):
    app.screen = "clash"

def quit_game(app):
    app.screen = "quit"

def main_menu(app):
    app.screen = "main"
    

def pause_menu(app): # If the user pauses the game
    app.screen = "pause"

# Two different screens depending on if you beat Ramos
def bad_ending(app):
    app.screen = "badEnding"
    
def good_ending(app):
    app.screen = "goodEnding"
    

# Now for the tutorial/Story Mode

def tutorial1_screen(app):
    app.screen = "tutorial1"

def tutorial2_screen(app):
    app.screen = "tutorial2"

def tutorial3_screen(app):
    app.screen = "tutorial3"

def backstory_screen(app):
    app.screen = "backstory"
    
def drawFirst(app):
    home_image = 'cmu://872511/35511957/DRAFTCLASHHOME.jpg' # image generated by chatgpt
    drawRect(0,0, app.width, app.height, fill = rgb(108,166,219)) # Used https://imagecolorpicker.com/ for rgb color
    drawImage(home_image, 230, 0, width=app.width - 460, height=app.height)
    drawLabel("Click anywhere to begin!", 590, 570, size = 25, bold = True, font = "orbitron", fill = 'black')
    
def drawLoading(app): # Do the logic for the loading screen here
    # First, draw the background image
    mainPic = 'cmu://872511/35389505/Screenshot+2024-12-02+122244.png' # Same place as options screen background
    drawImage(mainPic, 0, 0, width=app.width, height=app.height)
    # write stuff based off of the stage:
    if app.stage == 1:
        drawLabel( "Fetching Puppets...", app.width / 2, 330, size = 14, font = "orbitron", bold = True, fill = 'white')
    elif app.stage == 2:
        drawLabel("Watering Fields...", app.width / 2, 330, size = 14, font = "orbitron", bold = True, fill = 'white')
    elif app.stage == 3:
        drawLabel( "Kicking Off...", app.width / 2, 330, size = 14, font = "orbitron", bold = True, fill = 'white') # Took "kicking off" from Fifa mobile
    
    drawRect(app.width / 2 - 150, 350, 306, 30, fill='gray', border='black', borderWidth = 3)
    drawRect(app.width / 2 - 147, 353, max(app.progress * 3, 1), 24, fill='green') # chatgpt helped me with this line, but forgot to add the 1(if progress is 0)
    drawLabel(f'{int(app.progress)}%', app.width / 2, 365, size=20, bold=True, font = "Orbitron") # show the percentage and maintain the orbitron font
    
    # Now for the Pictures above:
    Lewa_kick = playerKicks["Lewandowski"]
    Mbappe_body = playerReverse["Kylian Mbappé"]
    drawImage(Lewa_kick, 150, 325, width=225, height=275)
    drawImage(Mbappe_body, 900, 325, width=110, height=275)
    
    # Now draw a ball at the top
    ball_image = 'cmu://872511/35359981/SBall.png'
    drawImage(ball_image, 550, 100, width=90, height=90)
    
def writeTutorial1(app):
    # First add the 'PSG Stadium image' off of google images(Parc des Princes)
    stad_image = 'cmu://872511/35403465/Screenshot+2024-12-02+145627.png'
    drawImage(stad_image, 0, 0, width=app.width, height=app.height)
    
    # 'Neymar full body Image' off of google images
    tut1_image = 'cmu://872511/35390010/Screenshot_2024-12-02_122758-removebg-preview.png' # got image off of google images
    drawImage(tut1_image, 150, 150, width=200, height=500)
    # 'Cartoon speaking cloud' off of google images
    cloud_image = 'cmu://872511/35402358/Screenshot_2024-12-02_143850-removebg-preview.png'
    drawImage(cloud_image, 300, 0, width=800, height=250)
    
    
    drawLabel("Welcome to the tutorial!", app.width / 2 + 95, 
    60, size = 13, bold = True, font = "orbitron")
    drawLabel("My name is Neymar, I'm a professional soccer player for PSG.", app.width / 2 + 95, 
    80, size = 13, bold = True, font = "orbitron")
    drawLabel("I'm here to show you aroud the Clash and Draft arena.", app.width / 2 + 95, 
    100, size = 13, bold = True, font = "orbitron")
    drawLabel("When you're ready, click 'next' and we'll embark on our journey!", app.width / 2 + 95, 
    120, size = 13, bold = True, font = "orbitron")

def writeTutorial2(app):
    
    # First add the 'PSG Stadium image' off of google images(Parc des Princes)
    stad_image = 'cmu://872511/35403465/Screenshot+2024-12-02+145627.png'
    drawImage(stad_image, 0, 0, width=app.width, height=app.height)
    
    phone_image = 'cmu://872511/35404531/Screenshot_2024-12-02_151421-removebg-preview.png' # 'Iphone sideways image' on google images
    drawImage(phone_image, app.width / 3 + 65, app.height / 3 + 40, width=app.width / 2 + 75, height=app.height/2 )
    puppet_image = 'cmu://872511/35359655/Screenshot+2024-11-30+231239.png' # Puppet theatre picture off of google
    drawImage(puppet_image, app.width / 3 + 145, app.height / 3 + 60, width=app.width / 2 - 150, height=app.height/2 - 40)
    
    # 'Neymar full body Image' off of google images
    ney_image = 'cmu://872511/35390010/Screenshot_2024-12-02_122758-removebg-preview.png' # got image off of google images
    drawImage(ney_image, 150, 150, width=200, height=500)
     # 'Cartoon speaking cloud' off of google images
    cloud_image = 'cmu://872511/35402358/Screenshot_2024-12-02_143850-removebg-preview.png'
    drawImage(cloud_image, 290, 5, width=775, height=250)
    
    drawLabel("Firsty, let me show you your field!", app.width / 2 + 75, 
    50, size = 13, bold = True, font = "orbitron")
    drawLabel("Now you may be wondering... This ain't no Parc de Princes...", app.width / 2 + 75, 
    70, size = 13, bold = True, font = "orbitron")
    drawLabel("Yes, that's true, this is an abandoned puppet show arena.", app.width / 2 + 75, 
    90, size = 13, bold = True, font = "orbitron")
    drawLabel("And you were brought here to play the last game... The game to end all games.", app.width / 2 + 75, 
    110, size = 13, bold = True, font = "orbitron")
    drawLabel("Don't get nervous though, I'll teach you how to play!", app.width / 2 + 75, 
    130, size = 13, bold = True, font = "orbitron")
    drawLabel("First, though, lets go to the locker room to get you sorted...", app.width / 2 + 75, 
    150, size = 13, bold = True, font = "orbitron")
    
    drawLabel("Neymar's Iphone", 760, 225, size = 20, bold = True, font = "orbitron", fill = "white")

def writeTutorial3(app):
    office_image = 'cmu://872511/35405396/Screenshot+2024-12-02+153428.png' # 'PSG locker room' image taken off of google images
    drawImage(office_image, 0, 0, width=app.width, height=app.height)
    # 'Neymar full body Image' off of google images
    ney_image = 'cmu://872511/35390010/Screenshot_2024-12-02_122758-removebg-preview.png' # got image off of google images
    drawImage(ney_image, 150, 150, width=200, height=500)
     # 'Cartoon speaking cloud' off of google images
    cloud_image = 'cmu://872511/35402358/Screenshot_2024-12-02_143850-removebg-preview.png'
    drawImage(cloud_image, 285, 0, width=775, height=250)
    
    drawLabel("Finally, we're here, welcome to the locker room!", app.width / 2 + 75, 
    50, size = 13, bold = True, font = "orbitron")
    drawLabel("Anyways, as I was saying, you were chosen to be here.", app.width / 2 + 75, 
    70, size = 13, bold = True, font = "orbitron")
    drawLabel("I can't really get into a lot of detail, but my friend old friend can...", app.width / 2 + 75, 
    90, size = 13, bold = True, font = "orbitron")
    drawLabel("Just click 'backstory' below to see the full story!", app.width / 2 + 75, 
    110, size = 13, bold = True, font = "orbitron")
    drawLabel("Click below to see the backstory", app.width / 2, 
    575, size = 13, bold = True, font = "orbitron", fill = "white")
    drawLabel("When you're ready, I'll direct you to the 'instructions' tab.", app.width / 2 + 75, 
    130, size = 13, bold = True, font = "orbitron")
    drawLabel("From there, you're on your own, good luck soldier!", app.width / 2 + 75, 
    150, size = 13, bold = True, font = "orbitron")
    
    # Now for the intructions:
    drawLabel("Click 'NEXT' to proceed to the instructions tab", app.width / 2, 
        555, size = 13, bold = True, font = "orbitron", fill = "white")
    
    
    


# This is a helper function for writing the Backstory
def splitTextIntoLines(text, max_chars_per_line): # This helper function splits a long text into multiple lines based on a maximum number of characters per line. 
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        # This is the check to see if the words on the line exceed the limit (if so, then move to a new line)
        if len(current_line) + len(word) + 1 > max_chars_per_line: 
            lines.append(current_line) 
            current_line = word
        else: 
            if current_line:
                current_line += " "
            current_line += word

    if current_line:
        lines.append(current_line)
    return lines # Return the lines
    
    
def writeBackstory(app):
    messi_image = 'cmu://872511/35410102/Screenshot+2024-12-02+193442.png' # taken from bzersko.pl, 'Messi in room alone' on google images
    drawImage(messi_image, 0, 0, width=app.width, height=app.height)
    
    speech_image = 'cmu://872511/35410974/Screenshot_2024-12-02_211129-removebg-preview.png' # taken from StickPNG, 'Speech bubble with arrow top right'
    drawRect(75, 200, 470, 390, fill = 'white', border = 'black', borderWidth = 4)
    drawRect(75, 120, 470, 80, fill = 'white', border = 'black', borderWidth = 4)
    drawLabel("Live translation from G.O.A.T Language:", 310, 160, size = 20, fill = 'black', font = "orbitron")

    
    for i, line in enumerate(app.typedTextLines): # enumerate was recommended by chatgpt, but I did the label (line below)
        drawLabel(line, 310, 225 + i * 30, size=11, fill="black", font = "orbitron", bold = True)

def drawGoodEnding(app):
    drawRect(0,0, app.width, app.height, fill = 'black')
    good_ending = 'cmu://872511/35463150/cartoon-style+image+with+a+somber+puppet+theatre,+a+soccer+player+carrying+a+human+little+boy,+in+a+night-time+scene+within+a+soccer+stadium+of+a+puppet+theatre+(1).png' # Copilot AI generated image
    drawImage(good_ending, 200, 0, width=app.width - 400, height=app.height)
    drawLabel("Congratulations, you have ended the curse!", 400, 25, fill = 'white', bold = True, font = "orbitron", size = 23)

def drawBadEnding(app):
    drawRect(0,0, app.width, app.height, fill = 'black')
    bad_ending = 'cmu://872511/35462481/a+menacing+monster+on+a+soccer+field+with+a+puppet+theatre+stadium+in+a+cartoon+style+(1).png' # Copilot AI generated image
    drawImage(bad_ending, 200, 0, width=app.width - 400, height=app.height)
    drawLabel("Sorry, son, Ramos beat you...", 400, 30, fill = 'white', bold = True, font = "orbitron", size = 23)
    
def drawPauseMenu(app):
    mainPic = 'cmu://872511/35389505/Screenshot+2024-12-02+122244.png' # Same place as options screen background
    drawImage(mainPic, 0, 0, width=app.width, height=app.height)
    app.buttons["quit"].draw()
    app.buttons["resume"].draw()
    app.buttons["menu"].draw()
    drawLabel("This is the Pause menu", app.width / 2, 280, size = 40, bold = True, fill = 'white', font = "orbitron")

def drawDropdown(app): # Draw the Dropdown Menu

    drawLabel('Select Players:', app.width / 2 - 10, 370, size=20, font = "orbitron", bold = True)
    app.player1Menu.draw()
    app.player2Menu.draw()
    drawLabel('Player 1:', 135, 375, size=15, font = "orbitron", bold = True)
    drawLabel('Player 2:', 865, 375, size=15, font = "orbitron", bold = True)
    


# Draft Mode functions, chatgpt used for debugging purposes and other purposes as cited:

def displayDraftChoices(app): # Make sure there is no MVC violation
    # Render the buttons for draft players
    for button in app.draftButtons:
        button.draw()

   
    buttonSpacing = 10
    buttonHeight = 30
    for i, player in enumerate(app.draftPlayers): 
        playerBoxTop = 150 + i * (buttonHeight + buttonSpacing)
        
        drawLabel(f"Country: {player.country}", app.width / 2 - 180, playerBoxTop + buttonHeight / 4, size=12, fill='white', font = "orbitron")
        drawLabel(f"Speed: {player.speed}", app.width / 2 - 150, playerBoxTop + buttonHeight / 1.4, size=12, fill='white', font = "orbitron")
        
    # Draw the rest of the screen here:
    drawLabel("Draft a player!", app.width / 2, 80, font = "orbitron", fill = 'white', size = 40)
    drawImage(playerKicks["Virgil van Dijk"], app.width / 2 - 100, 330, width=200, height=250)


def displaySelectedPlayer(app):
    # Map each player's name to their image (all taken from google images), chatgpt recommended the dictionary usage
    player_images = {
        "Virgil van Dijk": 'cmu://872511/35351732/VANDIJKTP-removebg-preview.png',
        "Kevin De Bruyne": 'cmu://872511/35351985/Screenshot_2024-11-24_181211-removebg-preview.png',
        "Lewandowski": 'cmu://872511/35351989/Screenshot_2024-11-24_181150-removebg-preview.png',
        "Mohamed Salah": 'cmu://872511/35351706/Screenshot_2024-11-24_181123-removebg-preview.png',
        "Neymar": 'cmu://872511/35352009/NEYMARNOBACK.png',
        "Kylian Mbappé": 'cmu://872511/35351994/Screenshot_2024-11-24_180926-removebg-preview.png',
        "Lionel Messi": 'cmu://872511/35351721/REMOVEMESSI.png',
        "Cristiano Ronaldo": 'cmu://872511/35351990/Screenshot_2024-11-24_180822-removebg-preview.png',
    }

    # Get the image corresponding to the selected player
    player_image = player_images.get(app.selectedPlayer.name)

    if player_image:
        # Display the selected player's image with fixed size (100x100)
        drawImage(player_image, app.width // 2 - 50, 110, width=100, height=100, border = 'black', borderWidth = 2)

    # Display the selected player's stats
    drawLabel(f'You selected {app.selectedPlayer.name}', app.width / 2, 250, size=20, fill='green', font = 'orbitron', bold = True)
    drawLabel(f"Country: {app.selectedPlayer.country}, Speed: {app.selectedPlayer.speed}",  
              app.width / 2, 275, size=16, fill='black', font = 'orbitron', bold = True)
    drawLabel('Choose your difficulty:', app.width / 2, 300, size=18, fill='blue', font = 'orbitron', bold = True)
    app.buttons["Easy2"].draw() # Draw the difficulty buttons
    app.buttons["Hard2"].draw()
    app.buttons["Extreme2"].draw()

# This function physically creates the player object
def createSelectedPlayer(app):
    app.user = Player( # Now we initialize the selectedPlayer using the player class so we can use this player in game
                    app.selectedPlayer.name, 
                    app.selectedPlayer.country, 
                    app.selectedPlayer.speed, 
                    cx=300, 
                    cy=app.height 
                    )
                    
def startDraft(app): # This function was heavily edited by chatgpt
    allPlayers = createPlayers(playersDict)
    
    # Choose 3 random players for the draft
    app.draftPlayers = random.sample(allPlayers, 3) # this sample functionality was given to me by chatgpt

    # Create buttons for the draft players
    app.draftButtons = []  # Ensure buttons are initialized here
    buttonSpacing = 10
    buttonHeight = 30
    buttonWidth = 210

    for i, player in enumerate(app.draftPlayers): # chatgpt helped me with these lines
        playerBoxTop = 150 + i * (buttonHeight + buttonSpacing)
        playerBoxLeft = (app.width - buttonWidth) / 2

        # Create a button for each player
        button = Button(
            playerBoxLeft,
            playerBoxTop,
            buttonWidth,
            buttonHeight,
            f"{player.name}",
            "skyblue",
            "lightblue",
        )
        app.draftButtons.append(button)

#
# GAME FUNCTIONALITY
#

def checkGoal(app): # This function sets the bounds for a goal
    # User's goal bounding coordinates
    user_goal_left = 190
    user_goal_right = 220
    user_goal_top = 360
    user_goal_bottom = 520

    # Opponent's goal bounding coordinates
    opp_goal_left = 1000
    opp_goal_right = 1030
    opp_goal_top = 360
    opp_goal_bottom = 520
    
    if (user_goal_left <= app.ball.cx <= user_goal_right and
            user_goal_top <= app.ball.cy <= user_goal_bottom):
        app.oppCounter += 1  # The opponent would score here
        app.isGoal = True
        
        sleep(0.35) # sleep adjusted amount of seconds
        restart(app)
        if app.oppCounter == 5:
            app.userCounter = 0
            app.oppCounter = 0
            app.screen = "badEnding"
        

    # Check if ball is in the opponent's goal
    elif (opp_goal_left <= app.ball.cx <= opp_goal_right and
              opp_goal_top <= app.ball.cy <= opp_goal_bottom):
        app.userCounter += 1  # User would score
        app.isGoal = True
        
        restart(app)
        if app.userCounter == 5:
            app.userCounter = 0
            app.oppCounter = 0
            app.screen = "goodEnding"
        

def checkGoalMultiplayer(app):
     # p1 goal bounding coordinates
    user_goal_left = 0
    user_goal_right = 30
    user_goal_top = 350
    user_goal_bottom = 510

    # p2 bounding coordinates
    opp_goal_left = 1170
    opp_goal_right = app.width # is 1200
    opp_goal_top = 350
    opp_goal_bottom = 510
    
    if (user_goal_left <= app.ball.cx <= user_goal_right and
            user_goal_top <= app.ball.cy <= user_goal_bottom):
        app.p2Counter += 1  # p2 would score here
        sleep(0.35)
        restart(app)
        if app.p2Counter == 5:
            app.screen = "p2Won"
            
        

    # Check if ball is in the opponent's goal
    elif (opp_goal_left <= app.ball.cx <= opp_goal_right and
              opp_goal_top <= app.ball.cy <= opp_goal_bottom):
        app.p1Counter += 1  # p1 would score
        sleep(0.35)
        restart(app)
        if app.p1Counter == 5:
            app.screen = "p1Won"
            
        
    
    
def loadingOnStep(app): # Chatgpt helped me with this function
    # Increment progress based on the stage
    if app.stage == 1:  # Fast loading for the first stage
        app.progress += 7
        if app.progress >= 33:
            app.stage = 2
    elif app.stage == 2:  # Slower loading for the second stage
        app.progress += 5
        if app.progress >= 60:
            app.stage = 3
    elif app.stage == 3:  # Make it slower for the final stage(Like the games I play)
        app.progress += 1
        if app.progress >= 99:
            stage = 4
    elif stage == 4:  # Final stage to reach 100%
        app.progress += 0.5
        if app.progress >= 100:
            app.progress = 100 # 100 is the largest percentage
    if app.progress == 100:
        app.stepsPerSecond = 0 # Put steps to 0 so it stops
        main_menu(app)
        
 
#
# END OF GUIFUNCTIONS
#
    
  
