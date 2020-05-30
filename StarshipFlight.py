##### This program is a game that tests your skills of piloting a spaceship
# The game is about being in a spaceship, but evildoers are trying to shoot you down
# with huge lasers that will immediately destroy your ship on impact.
# To start the game you have to press the start button on the left screen in the cockpit,
# Which will put you out of the first-person view to a top-down view for you to
# fly the spaceship using the arrow-keys or awsd-keys to move around.
# Flying isn't as easy, as the lasers will progressively become faster, and the forming
# stars in the backgrounds immense gravity pulls you towards them, which means that
# everytime you release the key you will be slightly pulled to the right or left.
# In the UI there is a small top menu that shows the controls, objective and score.
# When you will eventually get hit by a laser, a game over screen will show up and tell
# you how many seconds you survived, which gives an insentive to improve.



# Menu components
stars = Group(align='center')
stars.count = 0
### Label(s) created
score = Label(0,378,50,fill='white')
scoreL = Label('SCORE:',335,50,fill='white')

# Game Over Screen
gameOver = Group(Rect(200,200,220,300,align='center',border='grey'),Label("That's it",200,200,fill='white',size=20),Label("You survived for:",200,230,fill='white',size=20),Label('seconds',200,280,fill='white',size=20),Label('Great Job!',200,315,fill='white',size=20))
gameOver.visible = False

# Lasers
laser = Group(
    Rect(-400, -10, 425, 10, fill=gradient('red','red','red', 'white','red','red','red', start='bottom')),
    Rect(100, -10, 400, 10, fill=gradient('red','red','red', 'white','red','red','red', start='bottom'))
    )
laser.dy = 3
laser.maxDy = 12

# Functions for the laser movement
def nextlaser():
    laser.bottom=0
    laser.centerX = randrange(50,351)
    
def newGame():
    gameOver.visible = False
    nextlaser()
    laser.dy = 3
    app.paused = False

def movelaser():
    laser.top += laser.dy
    if (laser.top >= 400):
        if (laser.dy < laser.maxDy):
            laser.dy += 1
        nextlaser()

# Background
app.background='black'
def drawBack():
    ### Nested loop used
    for x in range(20,381,30):
        for y in range(0,391,30):
            # Calculates the radius and color
            ### Local Variable
            distanceX = abs(200 - x)
            distanceY = abs(200 - y)
            radius = 0

            # Gets the radius based on where the circle is on the canvas.
            if (distanceX < distanceY):
                radius = distanceY / 10
            else:
                radius = distanceX / 10
            color = radius * 10 + 55
            
            ### Gradient created
            Circle(x, y, radius, fill=gradient(rgb(randrange(100,255), randrange(100,255), color), 'black'),opacity=30)


# Top menu
### Function with 2 parameters
def drawMenu(red, green, blue):
    ### Label(s) created
    Label('LOOK OUT!!!',200,20,fill=rgb(red,green,blue),size=40)
    Label('Survive for as long as possible', 200,50,fill=rgb(red,green,blue))
    Label('Use arrow-keys', 50,50,fill=rgb(red,green,blue))
    Label('or AWSD-keys', 50,63,fill=rgb(red,green,blue))

# Player
playerPhoto = 'https://media.discordapp.net/attachments/554657016434524160/715444755080937553/unnamedefwef.png'
player = Image(playerPhoto, 200, 200)


### onKeyPress used
def onKeyPress(key):
    if (key == 'up' or key =='w'):
        player.centerY -= 15
    elif (key == 'down'or key =='s'):
        player.centerY += 15
    elif (key == 'left'or key =='a'):
        player.centerX -= 15
    elif (key == 'right'or key =='d'):
        player.centerX += 15

### onKeyRelease used
def onKeyRelease(key):
    # This will make moving a little harder
    player.centerY+=5
    ### randrange used
    player.centerX+=randrange(-1,1)

### onMouseMove
def onMouseMove(mouseX,mouseY):
    # Controls the cursor in the menu
    cursor.centerX = mouseX+5
    cursor.centerY = mouseY+5

### onMousePress
def onMousePress(mouseX,mouseY):
    if(button.hits(mouseX, mouseY)):
        button.visible=False
        stars.visible=False
        cursor.visible=False
        cockpit.visible=False
        black.visible=False
        if (gameOver.visible == True):
            newGame()

def onStep():
    ### Complex Conditional using a nested conditional
    if(cockpit.visible==False):
        if(gameOver.visible==False):
            movelaser()
            
        if(player.hitsShape(laser)):
            laser.visible=False
            gameOver.visible=True
            gameOver.toFront()
            Label(rounded(score.value/30), 200,255,fill='white',size=20)
            Image(gamePhoto,115,60)
            app.stop()
            print('Game Over, you survived for ' + str(rounded(score.value/30)) + ' seconds')
    
    # Resistance and drag
    player.centerY+=0.0981
    
    # Stars
    if (stars.count >= 250):
        stars.clear()
        stars.count = 0
        stars.width = 1
        stars.height = 1

    x = randrange(0,400)
    y = randrange(0,400)
    stars.add(Circle(x,y,1,fill='white'))

    stars.height *= 1.01
    stars.width *= 1.01
    stars.count += 1
    
    # Score in menu changes for how long you survive
    score.value +=1

    
    # Setting menu to the front
    laser.toFront()
    stars.toFront()
    cockpit.toFront()
    button.toFront()
    cursor.toFront()
    
    

### Calling functions
drawBack()
drawMenu(randrange(100,255),randrange(100,255),randrange(100,255))


# Things that had to be ontop
cursorPhoto = 'https://media.discordapp.net/attachments/554658343776682016/643525276516745256/actualcursorMini.png'
cockpitPhoto = 'https://media.discordapp.net/attachments/554657016434524160/715434675103072326/cockpit_roof_raptor.dis.png'
gamePhoto = 'https://media.discordapp.net/attachments/554657016434524160/715741613195788319/unnamed_1dis.png'
black = Rect(0,0,400,400)
cockpit = Image(cockpitPhoto,0,0)
cursor = Image(cursorPhoto,200,200)
### Group created
button = Group(Rect(58,320,88,20,fill=rgb(15,15,15),align='center'), Label('Start',58,320,fill='green',size=30))
