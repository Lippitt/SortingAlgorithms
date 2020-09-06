# Quick Sort Algorithm Visualisation
# B Lippitt
# 06/09/2020

# algorithm without visualisation
'''
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
 
    for j in range(low, high):

        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

'''
# algorithm with visualisation included, using pygame
# imports
import pygame as pg
import random

# init window
pg.font.init()
window = pg.display.set_mode((900,650))
pg.display.set_caption('Quick Sort Algorithm Visualisation')

# variable declaration
run = True
width = 900
length = 600
arr = [0]*151
n=len(arr)
arr_clr = [(0,204,102)]*151
clr_ind = 0
clr=[(0,204,102),(255,0,0),(0,0,153),(255,102,0)]
fnt = pg.font.SysFont('comicsans',30)
fnt2 = pg.font.SysFont('comicsans',20)

# generate an array
def generate_arr():
    for i in range(1,151):
        arr_clr[i] = clr[0]
        arr[i] = random.randrange(1,100)

# generate a new array
generate_arr()

#update the window
def update():
    window.fill((255,255,255))
    draw()
    pg.display.update()
    pg.time.delay(20)

# quick sort algorithm
def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        update()
        for i in range(0,pi+1):
            arr_clr[i]=clr[3]
        quicksort(arr,pi+1,high)

# function to partition array
def partition(arr, low, high):
    pg.event.pump()
    pivot = arr[high]
    arr_clr[high] = clr[2]
    i = low - 1
    for j in range(low,high):
        arr_clr[j]=clr[1]
        update()
        arr_clr[high]=clr[2]
        arr_clr[j]=clr[0]
        arr_clr[i]=clr[0]
        if arr[j] < pivot:
            i += 1
            arr_clr[i] = clr[1]
            arr[i],arr[j] = arr[j],arr[i]
    update()
    arr_clr[i]=clr[0]
    arr_clr[high]=clr[0]
    arr[i+1],arr[high] = arr[high], arr[i+1]

    return (i+1)

#draw array values to window
def draw():
    text = fnt.render('To sort, press enter',1,(0,0,0))
    window.blit(text, (20,20))

    text2 = fnt.render('For a new array, press R',1,(0,0,0))
    window.blit(text2, (20,60))
    element_width = (width-150)//150
    boundary_arr = 900/150
    boundary_grp = 550/100
    pg.draw.line(window,(0,0,0),(0,95),(900,95),6)

    for i in range(1,151):
        pg.draw.line(window, arr_clr[i],(boundary_arr*i-3,100),
                     (boundary_arr*i-3, arr[i]*boundary_grp+100),
                     element_width)

while run:
    window.fill((255,255,255))

    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_r:
                generate_arr()
            if event.key==pg.K_RETURN:
                quicksort(arr,1,n-1)

    draw()
    pg.display.update()

pg.quit()
