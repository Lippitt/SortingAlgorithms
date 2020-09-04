# Bubble Sort Algorithm
# B Lippitt
# 04/09/2020

# init pygame window
import pygame as pg
pg.init()
window = pg.display.set_mode((500,350))
pg.display.set_caption('Bubble Sort Algorithm Visualised')


# declare variables, elements in array are list of numbers to be sorted
arr = [200, 50, 130, 90, 250, 61, 110,
       88, 33, 80, 70, 159, 180, 20]
n = len(arr)
x = 40
y = 20
width = 20
height = arr
run = True

# function to draw bars to the window
def display(height):
    for i in range(n):
        pg.draw.rect(window, (0,0,255), (x+30*i,y,width,height[i]))

# create infinite loop
while run:
    # create flag to begin sorting, with a time delay to make it easier for user to visualise
    exe = False
    pg.time.delay(500)

    # iterate through possible events
    for event in pg.event.get():
        # if event is to quit, break out of loop
        if event.type == pg.QUIT:
            run = False

    # if the space bar is pressed, set fag to true
    if pg.K_SPACE:
        exe = True

    # if flag is false, update the bars on the screen
    if exe == False:
        window.fill((133,201,85))
        display(height)
        pg.display.update()

    # else, run the sorting algorithm
    else:
        for i in range(n-1):
            for j in range(n-i-1):
                if height[j]>height[j+1]:
                    height[j],height[j+1] = height[j+1],height[j]
                    
                window.fill((133,201,85))
                display(height)
                pg.time.delay(300)
                pg.display.update()

# exit main window
pg.quit()
