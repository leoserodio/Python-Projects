########################################
#   Draft and Clash
#   (Classes.py)
#   By: Leo Serodio
########################################
#   
########################################
#
#   Citations for this file: 
#   1)  Incorporated cmu_graphics syntax from 
#       https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
#   2)  Pictures taken from google images and links as specified
#
#   3)  Chatgpt used through specific functions in classes(described simultaneously with the code), and chatgpt used for some comments
#
########################################

class easyOpponent: 
    def __init__(self, x, y, width, height): # chatgpt: jump_chance and direction_change_timer
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocityX = random.uniform(-3, 3)  # Random initial velocity
        self.velocityY = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.is_jumping = False
        self.jump_chance = 0.0075  # chatgpt recommended this line, it contains the chance to jump randomly(easy opponent so this leaves room for very easy kicks)
        self.direction_change_timer = random.randint(30, 100)  # Random delay before direction change, initially I had fixed intervals, but chatgpt offered to use random

    def easyMove(self, app):
        # Apply gravity
        self.velocityY += self.gravity
        self.y += self.velocityY

        # Keep opponent on the ground 
        if self.y >= app.height - 120 - self.height:
            self.y = app.height - 120 - self.height
            self.velocityY = 0
            self.is_jumping = False
        
        # Handle horizontal movement
        if self.direction_change_timer == 0: # chatgpt edited the random velocity (line below)
            self.velocityX = random.uniform(-1, 1)  # Random velocity
            self.direction_change_timer = random.randint(10, 25)  # Reset timer
        else:
            self.direction_change_timer -= 1
        
        self.x += self.velocityX
        self.x = max(150, min(self.x, app.width - 150 - self.width))  # This was my idea, but I had a small syntax error that was corrected by chatgpt(not really chatgpt though)

        # Random jump, chatgpt suggested this functionality
        if not self.is_jumping and random.random() < self.jump_chance: # this line was corrected by chatgpt (similar to the above line)
            self.velocityY = self.jump_strength
            self.is_jumping = True

    def draw(self):
        forward_image = 'cmu://872511/35460974/Screenshot_2024-12-03_183618-removebg-preview.png' # Image from 442oons 
        reverse_image = 'cmu://872511/35507361/Screenshot_2024-12-03_183618-removebg-previewREVERSERAMOS.png'
        drawRect(self.x, self.y, self.width, self.height, fill=None)
        if self.velocityX <= 0:
            drawImage(forward_image, self.x, self.y, width=self.width, height=self.height)
        elif self.velocityX > 0:
            drawImage(reverse_image, self.x, self.y, width=self.width, height=self.height)


class hardOpponent: # Although I wrote this function using minimal chatgpt - only using it to debug minimal lines -, the logic was taken from a previously written class(above) that used chatgpt to debug and polish
    # I had chatgpt write comments for me on this class (when I initially wrote it, the comments were subpar)
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocityX = random.uniform(-10, 10)  # Random initial velocity, chatgpt recommended this line
        self.velocityY = 0
        self.gravity = 0.15
        self.jump_strength = -7
        self.is_jumping = False
        self.jump_chance = 0.0045  # Increased chance to jump randomly
        self.direction_change_timer = random.randint(30, 100)  # Random delay before direction change

    def hardMove(self, target_x, canvas_width, app): # 
        # Determine if the ball is on the left or right side of the canvas
        if target_x < canvas_width // 2:  # Ball on the left side
            target_position = target_x  # go towards the ball
        else:  # Ball on the right side
            target_position = target_x + 30  # Move right of the ball
    
        # Adjust horizontal movement
        # These lines were debugged by chatgpt (if, elif, else lines)
        if self.x < target_position:
            self.velocityX = 1
        elif self.x > target_position:
            self.velocityX = -1
        else:
            self.velocityX = 0  # Stop when aligned with target_position
        
        # Apply gravity to the vertical movement (random jump behavior)
        self.velocityY += self.gravity
        self.y += self.velocityY
    
        # Keep opponent on the ground
        if self.y >= app.height - 120 - self.height:
            self.y = app.height - 120 - self.height
            self.velocityY = 0
            self.is_jumping = False
        
        # Random jump logic
        if not self.is_jumping and random.random() < self.jump_chance:
            self.velocityY = self.jump_strength
            self.is_jumping = True
        
        # Update horizontal position
        self.x += self.velocityX
        self.x = max(150, min(self.x, app.width - 150 - self.width))  # Keep within canvas boundaries

    def draw(self):
        # Drawing the opponent using its position and dimensions
        drawRect(self.x, self.y, self.width, self.height, fill=None)
        forward_image = 'cmu://872511/35460974/Screenshot_2024-12-03_183618-removebg-preview.png' # Image from 442oons 
        reverse_image = 'cmu://872511/35507361/Screenshot_2024-12-03_183618-removebg-previewREVERSERAMOS.png'
        if self.velocityX <= 0:
            drawImage(forward_image, self.x, self.y, width=self.width, height=self.height)
        elif self.velocityX > 0:
            drawImage(reverse_image, self.x, self.y, width=self.width, height=self.height)
    


class extremeOpponent: # This class was edited by chatgpt, specifically "extremeMove", as the logic was not working when I implemented it myself at first
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocityX = random.uniform(-3, 3)  # Random initial velocity, *named velocityX and velocityY to not confuse with xv and yv of SoccerBall class
        self.velocityY = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.is_jumping = False
        self.jump_chance = 0.05  # Increased chance to jump randomly
        self.direction_change_timer = random.randint(30, 100)  # Random delay before direction change

    def extremeMove(self, target_x, app): # chatgpt helped me implement this functionality
        # Move horizontally towards the ball's x-coordinate
        if self.x < target_x and self.x < 850:
            self.velocityX = 2  # Move right
        elif self.x > target_x or self.x >= 850:
            self.velocityX = -2  # Move left if beyond 850 or ball is to the left
        else:
            self.velocityX = 0  # Stay in place if aligned
        # My AI for hard opponent was faulty, so chatgpt edited the 4 lines below (I had a small logic error). 
        self.x += self.velocityX # Update position
        self.velocityY += self.gravity
        self.y += self.velocityY
    
        # Keep the opponent on the ground
        if self.y >= app.height - 120 - self.height:
            self.y = app.height - 120 - self.height
            self.velocityY = 0
            self.is_jumping = False
    
        # Random jumps
        if not self.is_jumping and random.random() < self.jump_chance: # Although I wrote this line, the jump_chance was something chatgpt suggested(as stated above)
            self.velocityY = self.jump_strength
            self.is_jumping = True
    
        # Keep the opponent within canvas boundaries
        self.x = max(150, min(self.x, app.width - 150 - self.width))
    

    def draw(self):
        forward_image = 'cmu://872511/35460974/Screenshot_2024-12-03_183618-removebg-preview.png' # Image from 442oons 
        reverse_image = 'cmu://872511/35507361/Screenshot_2024-12-03_183618-removebg-previewREVERSERAMOS.png'
        drawRect(self.x, self.y, self.width, self.height, fill=None)
        if self.velocityX <= 0:
            drawImage(forward_image, self.x, self.y, width=self.width, height=self.height)
        elif self.velocityX > 0:
            drawImage(reverse_image, self.x, self.y, width=self.width, height=self.height)
    


# This function checks collisions between the ball and the opponent:
def checkCollision(ball, extremeOpponent): # here it is "extreme opponent" but it works for any opponent. In addition, chatgpt was used to debug, although it did not specifically write any code.
    # Although chatgpt did debug at times(stated below), most of the code was taken from the TA-Led Mini-lectures on object collisions and physics
    # Ensure ball maintains horizontal motion
    if abs(ball.xv) < 20:  # Minimum horizontal speed
        ball.xv += random.choice([-20, 20]) # chatgpt debugged this line(create physical randomness)

    # Check if the ball intersects with the opponent (rectangle)
    if (extremeOpponent.x <= ball.cx + ball.r and ball.cx - ball.r <= extremeOpponent.x + extremeOpponent.width and
        extremeOpponent.y <= ball.cy + ball.r and ball.cy - ball.r <= extremeOpponent.y + extremeOpponent.height):
        
        # Following the logic from the TA-Led Mini_lectures:
        # Handle horizontal collision (left or right side)
        if ball.cx - ball.r < extremeOpponent.x:
            ball.cx = extremeOpponent.x - ball.r  # Place the ball just outside the rectangle
            ball.xv = -ball.xv * 0.75  # Reverse horiz velocity
        elif ball.cx + ball.r > extremeOpponent.x + extremeOpponent.width:
            ball.cx = extremeOpponent.x + extremeOpponent.width + ball.r  # Place the ball just outside the rectangle
            ball.xv = -ball.xv * 0.75  # Reverse horiz velocity

        # Handle vertical collision (top or bottom side)
        if ball.cy - ball.r < extremeOpponent.y:
            ball.cy = extremeOpponent.y - ball.r  # Place the ball just outside the rectangle
            ball.yv = -ball.yv * 0.75  # Reverse vert velocity
        elif ball.cy + ball.r > extremeOpponent.y + extremeOpponent.height:
            ball.cy = extremeOpponent.y + extremeOpponent.height + ball.r  # Place the ball just outside the rectangle
            ball.yv = -ball.yv * 0.75  # Reverse horiz velocity





# All images from 442oons
playerBodies = {
    "Cristiano Ronaldo": 'cmu://872511/35564219/Screenshot_2024-12-03_182200-removebg-previewRONNIEREVERSE.png',
    "Lionel Messi": 'cmu://872511/35458677/Screenshot_2024-12-03_163317-removebg-preview.png',
    "Neymar": 'cmu://872511/35460891/Screenshot_2024-12-03_183016-removebg-preview.png', 
    "Kylian Mbappé": 'cmu://872511/35506177/Screenshot_2024-12-03_170739-removebg-previewREVERSEMBAPPE.png',
    "Mohamed Salah": 'cmu://872511/35506235/Screenshot_2024-12-03_172221-removebg-previewREVERSESALAH.png',
    "Lewandowski": 'cmu://872511/35460118/Screenshot_2024-12-03_172811-removebg-preview.png',
    "Kevin De Bruyne": 'cmu://872511/35460303/Screenshot_2024-12-03_173923-removebg-preview.png',
    "Virgil van Dijk": 'cmu://872511/35460419/Screenshot_2024-12-03_174439-removebg-preview.png'
}
# All images from 442oons
playerReverse = {
    "Cristiano Ronaldo": 'cmu://872511/35564219/Screenshot_2024-12-03_182200-removebg-previewRONNIEREVERSE.png',  
    "Lionel Messi": 'cmu://872511/35506069/Screenshot_2024-12-03_163317-removebg-previewREVERSEMESSI.png',
    "Neymar": 'cmu://872511/35506140/Screenshot_2024-12-03_183016-removebg-previewREVERSENEYMAR.png', 
    "Kylian Mbappé": 'cmu://872511/35459487/Screenshot_2024-12-03_170739-removebg-preview.png',
    "Mohamed Salah": 'cmu://872511/35459999/Screenshot_2024-12-03_172221-removebg-preview.png',
    "Lewandowski": 'cmu://872511/35506319/Screenshot_2024-12-03_172811-removebg-previewREVERSELEWA.png',
    "Kevin De Bruyne": 'cmu://872511/35506424/Screenshot_2024-12-03_173923-removebg-previewREVERSEBRUYNE.png',
    "Virgil van Dijk": 'cmu://872511/35506451/Screenshot_2024-12-03_174439-removebg-previewREVERSEDIJK.png'
} 

# All images from 442oons
playerKicks = {
    "Cristiano Ronaldo": 'cmu://872511/35461010/Screenshot_2024-12-03_164735-removebg-preview-removebg-preview.png', 
    "Lionel Messi": 'cmu://872511/35459270/Screenshot_2024-12-03_165438-removebg-preview+(1).png',
    "Neymar": 'cmu://872511/35460898/Screenshot_2024-12-03_182852-removebg-preview.png',
    "Kylian Mbappé": 'cmu://872511/35459509/Screenshot_2024-12-03_170813-removebg-preview.png',
    "Mohamed Salah": 'cmu://872511/35460015/Screenshot_2024-12-03_172253-removebg-preview.png',
    "Lewandowski": 'cmu://872511/35460128/Screenshot_2024-12-03_172858-removebg-preview.png',
    "Kevin De Bruyne": 'cmu://872511/35460310/Screenshot_2024-12-03_173812-removebg-preview.png',
    "Virgil van Dijk": 'cmu://872511/35460411/Screenshot_2024-12-03_174508-removebg-preview+(1).png' 
}
# all images from 442oons
playerKicksReverse = {
    "Cristiano Ronaldo": 'cmu://872511/35508866/Screenshot_2024-12-03_164735-removebg-preview-removebg-previewREVERSERONALDOKICK.png', 
    "Lionel Messi": 'cmu://872511/35508883/Screenshot_2024-12-03_165438-removebg-preview+(1)REVERSEMESSIKICK.png',
    "Neymar": 'cmu://872511/35508906/Screenshot_2024-12-03_182852-removebg-previewREVERSENEYMARKICK.png',
    "Kylian Mbappé": 'cmu://872511/35508450/Screenshot_2024-12-03_170813-removebg-previewREVERSEMBAPPEKICKREAL.png',
    "Mohamed Salah": 'cmu://872511/35508917/Screenshot_2024-12-03_172253-removebg-previewREVERSESALAHKICK.png',
    "Lewandowski": 'cmu://872511/35508962/Screenshot_2024-12-03_172858-removebg-previewREVERSELEWAKICK.png',
    "Kevin De Bruyne": 'cmu://872511/35508973/Screenshot_2024-12-03_173812-removebg-previewREVERSEBRUYNEKICK.png',
    "Virgil van Dijk": 'cmu://872511/35508984/Screenshot_2024-12-03_174508-removebg-preview+(1)REVERSEDIJKKICK.png'
}




class Player: # This class was all written by me except the collideWithBall, which had significant chatgpt debugging (I still wrote it initially)
    def __init__(self, name, country, speed, cx, cy):
        self.kicked = False  # Initialize the kicked bool
        self.kickStartTime = 0
        self.name = name
        self.cx = cx  # Player's x position
        self.cy = cy  # Player's y position
        self.country = country
        self.speed = speed  # Speed of player movement
        self.vx = 0  # Horizontal velocity
        self.vy = 0  # Vertical velocity
        self.isJumping = False  # To check if the player is in mid-jump
        self.falling = False
    
    def boundPlayer(self, app): # Bound the player to the field
        if self.cx <= 150:
            self.vx = 1 # starting speed
        if self.cx >= app.width:
            self.vx = -50
    def moveUp(self, ball):
        if not self.isJumping:
            if abs(self.cy - ball.cy) <= 400 and abs(self.cx - ball.cx) <= ball.r: # check if the ball would be in the jump space
                return # chatgpt added this line but pretty much just return if player can't jump
           
        if not self.isJumping:  # Check if the player is not already jumping
            self.isJumping = True
            self.vy = -15  # Set initial jump speed (negative for upward movement)
            self.cy = 400  # Set the initial jump height to 400

    def moveLeft(self):
        if self.cx >= 150:
            self.vx = -self.speed  # Move to the left

    def moveRight(self, app):
        if self.cx <= app.width - 150:
            self.vx = self.speed  # Move to the right

    def stopMoving(self):
        self.vx = 0  # Stop horizontal movement when key is released

    def applyGravity(self, g, dt, ground_y, app): # Also from TA-Led mini lecture (adapted by me)
        ground_y = app.height - 100
        # Apply gravity if player is above the ground
        if self.cy < ground_y - 40:  # Player has not reached the ground yet
            self.vy += g * dt  # Apply gravity to vertical velocity
        else:
            self.cy = ground_y - 40  # Keep player on the ground
            self.vy = 0  # Stop falling once the player hits the ground
            self.isJumping = False  # The player is not jumping anymore
    
    def updatePosition(self, dt): # From TA-Led mini lecture
        self.cx += self.vx * dt  # Update horizontal position
        self.cy += self.vy * dt  # Update vertical position based on velocity

    def collideWithBall(self, ball): # Updated Collide with ball function (Helped by chatgpt)
        # Here we use a circular hitbox for the top fifth of the player model (the head)
        ball_rad = ball.r + 7.5
        head_radius = 25  # Adjust this radius as needed
        head_center_x = self.cx 
        if not self.isJumping:
            head_center_y = self.cy - 80
        elif self.isJumping:
            head_center_y = self.cy - 60
        # For this line above, I added the rest, as when the player was jumping, the collisions was buggy
            
        # Here we calculate the distance from the ball to the player head
        dist_to_head = distance(ball.cx, ball.cy, head_center_x, head_center_y) # use our distance formula
            
        # Now we start the collision logic
        if dist_to_head < (ball_rad + head_radius):
            overlap = (ball_rad + head_radius) - dist_to_head # this line was edited by chatgpt
                
            # Calculate the collision normal (direction of bounce), chatgpt told me to call it "normal" as it is more professional (good variable naming)
            collision_normal_x = (ball.cx - head_center_x) / (dist_to_head + 1e-6) # Same as before
            collision_normal_y = (ball.cy - head_center_y) / (dist_to_head + 1e-6)
                
            # Now we adjust the ball's position to resolve the overlap
            # Adjust the ball's position to resolve the overlap with a stronger resolution, this was edited by chatgpt, the ball was initially sinking through my player model
            ball.cx += collision_normal_x * (overlap + 0.8) # chatgpt added the "1e-6"
            ball.cy += collision_normal_y * (overlap + 0.8)
        
                
            # Reflect the ball's velocity using the collision normal, used chatgpt for these lines (got me unstuck).
            dot_product = ball.xv * collision_normal_x + ball.yv * collision_normal_y # this line was my idea but chatgpt helped me implement
            # Reflect the ball's velocity
            ball.xv -= 2 * dot_product * collision_normal_x # Reflect horizontal velocity
            ball.yv -= 2 * dot_product * collision_normal_y # Reflect vertical velocity
        
        # Now we use a rectangular hitbox for the rest of the player (4/5)
        body_top = head_center_y + head_radius  # We already have the head radius and center, so if we add them, we get to the point right outside the bottom of the head
        if not self.isJumping:
            body_bottom = self.cy
        elif self.isJumping:
            body_bottom = self.cy - 30
        body_left = self.cx - 22  # Left edge (adjust as needed for visual purposes)
        body_right = self.cx + 22  # Right edge 
            
        # Same logic as before (when only had rectangular hitbox Pre-TP2)
        # This just checks if the ball is intersecting the hitbox we created
        closest_x = max(body_left, min(ball.cx, body_right)) # I was initially using min, chatgpt set to max(small logic error)
        closest_y = max(body_top, min(ball.cy, body_bottom))
            
        dist_to_body = distance(ball.cx, ball.cy, closest_x, closest_y) # Use the distance formula (dist from ball to closest point on the hitbox)
        if dist_to_body < ball_rad:
            overlap = ball_rad - dist_to_body # Find the overlap, similar logic with the head
            collision_normal_x = (ball.cx - closest_x) / (dist_to_body + 1e-6) # These lines are the same as before (TP2), finding the collision normal(math)
            collision_normal_y = (ball.cy - closest_y) / (dist_to_body + 1e-6)
                
            # Now we change the ball's position
            ball.cx += collision_normal_x * overlap
            ball.cy += collision_normal_y * overlap
            
            # Same as head so technically chatgpt was used(just copy and pasted from head collision)
            dot_product = ball.xv * collision_normal_x + ball.yv * collision_normal_y
            ball.xv -= 2 * dot_product * collision_normal_x
            ball.yv -= 2 * dot_product * collision_normal_y
        
        
    def kick(self, ball):
        if not self.kicked:  # Only allow kicking if not already in kick state
            self.kicked = True
            self.kickStartTime = time.time()  # Start the timer for this player's kick
            self.cx += 5  # Move the player forward a few pixels

            # Shoot the ball diagonally upward
            if abs(self.cx - ball.cx) <= 110 and abs(self.cy - ball.cy) <= 50:
                if self.vx >= 0:
                    ball.xv += 375  # Ball goes diagonally right and upward
                    ball.yv -= 550
                elif self.vx < 0:
                    ball.xv -= 375  # Ball goes diagonally left and upward
                    ball.yv -= 550

    def resetKick(self):
        if self.kicked and time.time() - self.kickStartTime > 0.35:
            self.kicked = False  # Reset kick state after 0.35 seconds
                        
            
            
    def draw(self, app):
        # Messi image is different than all the other, make his width larger
        kick = playerKicks[self.name] # Kicking image
        kickReverse = playerKicksReverse[self.name] # Kicking image reversed
        body = playerBodies[self.name] # Body image
        reverse = playerReverse[self.name] # Reverse image for when the player is running backwards
        
        if self.kicked == True:
            if self.vx >= 0:
                drawImage(kick, self.cx - 30, self.cy - 100, width=110, height=125)
            elif self.vx < 0:
                drawImage(kickReverse, self.cx - 30, self.cy - 100, width=110, height=125)
        
        else:
            if self.vx >= 0:
                if self.name == "Lionel Messi":
                     drawImage(body, self.cx - 30, self.cy - 100, width=80, height=125)
                else:
                    drawImage(body, self.cx - 30, self.cy - 100, width=60, height=125)
            elif self.vx < 0:
                if self.name == "Lionel Messi":
                    drawImage(reverse, self.cx - 30, self.cy - 100, width=80, height=125)
                else:
                    drawImage(reverse, self.cx - 30, self.cy - 100, width=60, height=125)
        
        

# Gravity Class (From TA-led Mini-Lecture)
class Gravity:
    def falling(y, v, g, dt):
        v += g * dt
        y += v * dt
        return y, v
    
    def moveXDir(x, v, dt):
        x += v * dt
        return x

# Adapted from TA-Led mini lecture on gravity and collisions
class Woodwork:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4): # the 4 corner tuples were my idea but I was unsure how to implement, so chatgpt implemented it for me
        self.corners = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    def coordQuadruple(self):
        return tuple(self.corners) # chatgpt wrote this line(syntax)
    def draw(self):   
        drawPolygon(*[coord for point in self.corners for coord in point], fill=None) # adapted from TA-Led Lecture and chatgpt

# Ball class(adapted from mini lecture)
class SoccerBall:
    def __init__(self, cx, cy, r, xv, yv):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.xv = xv
        self.yv = yv
    
        
def distance(x1, y1, x2, y2): # Simple distance formula
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


# Add the dropdown menu class, similar to the button class
class DropdownMenu: # Chatgpt helped me with this class
    def __init__(self, x, y, width, height, options):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.options = options
        self.selected = None  # Currently selected option
        self.expanded = False  # Menu state (collapsed/expanded) chatgpt wrote this line
        self.isHovered = False  # The hover feature similar to the Button class
        self.hoveredOption = None  # Chatgpt wrote this line

    def draw(self):
        # Set fill color based on hover/click state
        fillColor = 'lightblue' if self.isHovered else 'lightgray' # chatgpt edited my syntax to look like this (cleaner)
        if self.expanded:
            fillColor = 'lightgreen'  

        # Draw the main menu box
        drawRect(self.x, self.y, self.width, self.height, fill=fillColor, border='black')
        if self.selected is not None:
            drawLabel(self.selected, self.x + self.width // 2, self.y + self.height // 2, size=12, font = "orbitron", bold = True)

        # If expanded, then draw all the options(Player options), these next 5 lines were heavily edited by chatgpt in terms of syntax and fixed logic errors
        if self.expanded:
            for i, option in enumerate(self.options): # chatgpt did the enumerate logic
                optionFill = 'lightblue' if self.hoveredOption == i else 'white'
                drawRect(self.x, self.y + self.height * (i + 1), self.width, self.height, fill=optionFill, border='black', borderWidth=0.75)  # 0.5 looks the best
                drawLabel(option, self.x + self.width // 2, self.y + self.height * (i + 1.5), size=12, font = "orbitron", bold = True) # this line was written by chatgpt completely, I was stuck here

    def check_click(self, mouseX, mouseY): # similar function to Button class
        if (self.x <= mouseX <= self.x + self.width and 
            self.y <= mouseY <= self.y + self.height):
            self.expanded = not self.expanded
            return True

        # If expanded, check if an option is clicked, again chatgpt helped with this logic
        if self.expanded:
            for i, option in enumerate(self.options): # chatgpt did the enumerate logic
                option_y = self.y + self.height * (i + 1)
                if (self.x <= mouseX <= self.x + self.width and 
                    option_y <= mouseY <= option_y + self.height):
                    self.selected = option
                    self.expanded = False  # Collapse the menu
                    return True
        return False

    def check_hover(self, mouseX, mouseY): # Similar function to Button class
        self.isHovered = (self.x <= mouseX <= self.x + self.width and 
                          self.y <= mouseY <= self.y + self.height)
        
        self.hoveredOption = None
        if self.expanded:
            for i in range(len(self.options)):
                option_y = self.y + self.height * (i + 1) # This line was debugged by chatgpt (I had a small logic error)
                if (self.x <= mouseX <= self.x + self.width and 
                    option_y <= mouseY <= option_y + self.height):
                    self.hoveredOption = i

    def close(self):
        self.expanded = False # put the expanded back to False
        
        
class Button: # Button class for the buttons in my app, taken as inspiration from video (https://www.youtube.com/watch?v=GMBqjxcKogA) on tips for GUI's
    def __init__(self, x, y, width, height, text, base_color, hover_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.base_color = base_color
        self.hover_color = hover_color
        self.current_color = base_color
    
    def draw(self):
        # Draw the button rectangle
        drawRect(self.x, self.y, self.width, self.height, fill=self.current_color, border="black", borderWidth=2)
        # Draw the button text
        drawLabel(self.text, self.x + self.width / 2, self.y + self.height / 2, size=20, bold=True, fill="black", font = "orbitron")

    def check_hover(self, mouseX, mouseY): # Although this was my idea, chatgpt helped me implement the logic by debugging
        if self.x <= mouseX <= self.x + self.width and self.y <= mouseY <= self.y + self.height:
            self.current_color = self.hover_color # chatgpt told me to use this to make the button more 'appealing', so when the user hovers over, the color changes (simulated real games)
            return True
        else:
            self.current_color = self.base_color
            return False

    def check_click(self, mouseX, mouseY):
        return self.x <= mouseX <= self.x + self.width and self.y <= mouseY <= self.y + self.height
        
#
# END OF CLASSES
#
