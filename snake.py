import curses
from random import randint


#setup screen
curses.initscr()
win = curses.newwin(35,85,0,0) # y,x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) #-1


#Initial Variables ##########

# snake and food
snake = [(4,10),(4,9),(4,8),(4,7)]
food = (10,20)

score = 0 # initial score

# keys
ESC = 27
key = curses.KEY_RIGHT

keys=[curses.KEY_LEFT, curses.KEY_UP,curses.KEY_RIGHT,  curses.KEY_DOWN]


#Game Logic ################


while key != ESC:
    win.addstr(0,2,'Score ' + str(score) + '')
    win.timeout(90 - (len(snake)//5 + len(snake)//10 % 120 )) #increase speed based on
                                                              # lenght of snake
    prev_key = key
    event = win.getch()

    key = event if event != -1 else prev_key

    #check key is one of the arrows
    if key not in keys:
        key = prev_key

    if key == keys[keys.index(prev_key)-2]:
        key = prev_key



    #calculate the next coordinates of snake

    y = snake[0][0]
    x = snake[0][1]



    if key == curses.KEY_DOWN:
        y += 1
    elif key == curses.KEY_UP:
        y -= 1
    elif key == curses.KEY_LEFT:
        x -= 1
    elif key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0 ,(y,x)) #append

    # Did we run into a border?

    if y == 0 or y == 34: break
    if x == 0 or x == 84: break

    # Is the snake over itself?
    if snake[0] in snake[1:]: break

    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = ( randint( 1,34 ), randint(1 , 84) )
            if food in snake:
                food = ()
        win.addch( food[0], food[1], "*" )
    else:
        last = snake.pop()
        win.addch( last[0], last[1], ' ' )

    win.addch( snake[0][0], snake[0][1], '#' )


    win.addch(food[0],food[1],'*')



curses.endwin()
print(f"You have reached the low low score of: {score}")
