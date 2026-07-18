import pgzrun

WIDTH=(750)
HEIGHT=(750)
TITLE=("SHAPES")

w=200
h=200
x=WIDTH//2
y=HEIGHT//2
def draw():
    for i in range (100,400,20) :
        rect=Rect((x,y),(i,i))
        rect.center=(x,y)
        screen.draw.rect((rect),("green"))

pgzrun.go()