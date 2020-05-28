import math
##### We will be making a program that is a kind of ball drop where you randomly receive a
# gift, by droping a ball randomly and then it will randomly go through a bouncy grid
# and eventually land in one of 5 possible gift location, either receiving a blue or red gift.
# We wanted the game to always play out randomly, which is why that everytime you start a
# new game, the background is different randomly generated, and the position and speed of the
# ball is also always different from game to game.
# To play you simply press the start button on the start menu, when first starting the game,
# then a ball will randomly appear, with a random speed and direction, and then you can sit
# in anticipation of what gift you are going to get.
# While you wait you can see how far away the ball is from the gifts in the upper left
# corner, as well as seeing the angle of the ball to the top, displaying in degrees, and
# as an arrow in a clock.
# Then if you don't want to play anymore you can press the cross in the top right corner.
# Have fun, we hope you will get the gift you want :).


app.paused = True


# Photos
name = 'https://media.discordapp.net/attachments/554657016434524160/702259701198487652/lol100.png'

#Backgrounds
### Rangrange used
red = randrange(0, 256)
Rect(0,0,400,400, fill=rgb(red, 255-red, 255))
Rect(110,90,240,280,fill='white')

# The ball
### Arc created
arc1 = Arc(200,50,20,20,0,90,fill='red')
arc2 = Arc(200,50,20,20,0,90,fill='red',rotateAngle=180)
ballout = Circle(200,50,10,fill='yellow')
ball = Group(ballout, arc1, arc2)

### RandRange used
ball.centerX = randrange(135, 318)
ball.centerY = 110
ball.ballRadius = ballout.radius

# Ball movement
ball.dy = 0.1
ball.dx = -3.0 + 6.0 * random()

# Distance Label
distanceL = Label(0,200,36,fill='white',size=20)
distV = Label('Distance to target:', 100, 36, fill='white', size=20)

# Grid
grid = Group()

# Border of the game
border = Group(Rect(110,90,240,280,fill=None,border='black'))

# Makes the grid and adds it to the group
### Nested for-loop using (low, high, step)
for x in range(135,346,37):
    for y in range(140,330,45):
        grid.add(Circle(x,y,5))
        
# Puts the ball infront of the grid
ball.toFront()

# Angle compass
compass = Circle(200, 200, 165, fill=gradient('white', 'lightGrey', start='left'), border='black', borderWidth=4)
compass.width = 90
compass.height = 90
compass.centerX = 55
compass.centerY = 130

# The ticks in the compass
for i in range(20):
            centerX, centerY = getPointInDir(55,130,20*i, 45)
            Line(centerX, centerY, 55, 130)

# Cover of the ticks
compass_cover = Group(Arc(200, 200, 225, 225, 45, 270, fill=gradient('lightGrey', 'white', start='left')), Arc(200, 200, 225, 225, 315, 90, fill=gradient('gainsboro', 'silver', start='right-top')))
compass_cover.width = 71
compass_cover.height = 71
compass_cover.centerX = 55
compass_cover.centerY = 130

# Angle label
aLabel = Label("Angle of ball:", 55, 190,fill='white')
angLabel = Label(0, 55, 202,fill='white')

# Arrow in the
### Arrow
arr = Line(55,130,55,98,fill='crimson',arrowEnd=True,lineWidth=2)

# Cross for closing game
close = Label('x',365,32,fill='white',size=50)

# Makes the lines on the bottom and makes the gifts
def drawGifts():
    # Makes the seperating lines
    for i in range(155,350,50):
        border.add(Line(i,370,i,333))
    
    # Creates the gift differently using the mod operator
    for i in range(5):
        ### Mod(%) operator used
        if(i%2 == 0):
            Rect(i*50+130,350,30,30,fill='crimson',align='center')
            Circle(i*50+130,350,9,fill='yellow')
        else:
            RegularPolygon(i*50+130,350,17,7,fill='blue',align='center')
            ### Arc created
            Arc(i*50+129,348.6,20,20,0,180,fill='pink',rotateAngle=45)
            

# Collision Physics Function        
def doCollision(b, g):
    #Distance between centers
    d = distance(g.centerX, g.centerY, b.centerX, b.centerY)
    
    #Unit normal along line connecting centers
    nx = (g.centerX - b.centerX)/d
    ny = (g.centerY - b.centerY)/d 
    
    #Conserve 95% momentum
    p = (nx*b.dx+ny*b.dy) * 1.9
    
    b.dx -= p*nx
    b.dy -= p*ny
    
    #Displace ball away from g to account for possible overlap
    overlap = d - b.ballRadius - g.radius
    b.centerX -= (overlap * (b.centerX - g.centerX)/d)
    b.centerY -= (overlap * (b.centerY - g.centerY)/d)

def onStep():
    # gravity:
    ball.dy += 0.1
    
    #Makes it so the ball is affected by the grid
    for gball in grid.children:
        if gball.hitsShape(ball):
            doCollision(ball, gball)
            break
        
    
    # Makes the ball move
    ball.centerY += ball.dy
    ball.centerX += ball.dx
    
    # Bounces the ball of the border
    if ball.right > border.right:
        ball.dx *= -1
        ball.right = border.right
    elif ball.left < border.left:
        ball.dx *= -1
        ball.left = border.left
    
    if ball.top < border.top:
        ball.top = border.top
        ball.dy *= -1
    elif ball.bottom > border.bottom:
        ball.bottom = border.bottom
        ball.dy *= -1
    
    # Checks distance and shows it
    ### Distance Function used
    ### Local variable
    dist = distance(ball.centerX, ball.centerY, 200, 370)
    distanceL.value = int(dist)
    
    # Moves the arrow showing angle to top
    angle = angleTo(ball.centerX, ball.centerY, 230 , 90)
    newX2, newY2 = getPointInDir(55,130,angle,35)
    arr.x2 = newX2
    arr.y2 = newY2
    
    # Shows the angle
    angLabel.value = int(angle)
    
    # Toggles end of game menu
    if(ball.bottom>=370):
        app.stop()
        menu.visible = True
        menu.toFront()
        if(155>ball.centerX>110 or 255>ball.centerX>205 or 400>ball.centerX>305):
            Label('Congrats you got the red gift',200,320,fill='white',size=20)
        else:
            Label('Congrats you got the blue gift',200,320,fill='white',size=20)


def onMousePress(mouseX, mouseY):
    # Toggles the menu
    if(menuB.hits(mouseX,mouseY)):
        menu.visible=False
        menuB.visible=False
        app.paused=False
    
    # Closes the game
    if(close.hits(mouseX,mouseY)):
        app.stop()
        Rect(0,0,400,400)
        print('Press play to play again')

# Calling of functions
drawGifts()

# Start menu
menu = Group(Rect(0,0,400,400,opacity=40), Rect(50,60,300,300,fill='lightBlue'), Label('Ball Drop', 200,90,fill='white',size=50), Image(name,135,131))
menuB = Group(Rect(125,275,150,40,fill=rgb(red, 255-red, 255)), Label('Start',200,294,fill='white',size=45))
