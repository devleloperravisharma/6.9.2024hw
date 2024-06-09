import pgzrun

WIDTH = 300

HEIGHT = 300

r1 = 255

g1 = 228

b1 = 225

r2 = 240

g2 = 248

b2 = 255

r3 = 230

g3 = 230

b3 = 250

rgb = (r2,g2,b2)

rgb1 = (r1, g1, b1) 

rgb2 = (r3, g3, b3)
"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

def draw():

    screen.fill(color = "pink" )
    width = WIDTH
    height = HEIGHT-100

    radius = 175


    r = 241
    g = 222
    b = 221

    for i in range(30):
        d = Rect((0,0), (width, height))
        d.center = (150,150)

        width -= 10

        height += 10

        r -= 5
        g += 5

        screen.draw.rect(d, (rgb))

    screen.draw.line((0,0), (-1,-1), (rgb))

    screen.draw.circle((150,150), (radius), (rgb2))

    screen.draw.filled_circle((150,150), (radius-75), (rgb2))

    screen.draw.filled_rect(d, (rgb2))

    
pgzrun.go()
