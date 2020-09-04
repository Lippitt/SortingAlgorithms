# Insertion Sort Algorithm
# B Lippitt
# 04/09/2020

# imports
import pygame
import random
import time

# init window
pygame.font.init()
startTime = time.time()
window = pygame.display.set_mode((900,650))
pygame.display.set_caption('Insertion Sort Visualiser')

# variable declaration
run = True
width = 900
length = 600
array = [0]*151
arr_clr = [(0,204,102)]*151
clr_ind = 0
clr = [(0,204,102),(255,0,0),(0,0,153),(255,102,0)]
fnt = pygame.font.SysFont('comicsans', 30)
fnt1 = pygame.font.SysFont('comicsans', 20)

# generate an array of 150 random numbers
def generate_arr():
    for i in range(1,151):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1,100)

# call said function so that we have an array to work with
generate_arr()

# sorting algorithm - explained on portfolio site
def insertion_sort(arr):
    # traverse through elements of array
    for i in range(len(array)):
        pygame.event.pump()
        refill()
        pivot = array[i]
        arr_clr[i] = clr[2]
        #move elements to the left of pivot, one position ahead of current position
        j = i-1
        while j>=0 and pivot < array[j]:
            arr_clr[j] = clr[2]
            array[j+1] = array[j]
            refill()
            arr_clr[j] = clr[3]
            j = j-1
        array[j+1] = pivot
        refill()
        arr_clr[i] = clr[0]

# function to update window
def refill():
    window.fill((255,255,255))
    draw()
    pygame.display.update()
    pygame.time.delay(10)


# draw array values to the screen
def draw():
    # render text to user
    txt = fnt.render('To begin sort, press Enter', 1, (0,0,0))
    window.blit(txt,(20,20))
    
    txt1 = fnt.render('To create a new array, press R', 1, (0,0,0))
    window.blit(txt1,(20,40))
    
    text3 = fnt1.render("Runtime: "+ 
            str(int(time.time() - startTime)),
                                  1, (0, 0, 0)) 
    window.blit(text3, (600, 20)) 

    element_width =(width-150)//150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(window, (0, 0, 0), (0, 95),
                                  (900, 95), 6) 

    # draw array values as lines on screen
    for i in range(1, 151): 
        pygame.draw.line(window, arr_clr[i],
                   (boundry_arr * i-3, 100), 
                   (boundry_arr * i-3, 
     array[i]*boundry_grp + 100), element_width)

# infinite loop to keep window open
while run:
    # background color white
    window.fill((255,255,255))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                generate_arr()
            if event.key == pygame.K_RETURN:
                insertion_sort(array)

    draw()
    pygame.display.update()


pygame.quit()













    
