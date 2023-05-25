# curses 5

'''Loosely based off 
https://github.com/TheAILearner/Snake-Game-using-Python-Curses/blob/master/snake_game_using_curses.py
with some changes of approach, e.g. classes
'''

#===libraries
import curses
import time
import random

'''
What's the most logical structure?
Pass in each thing required as argument,
Or create the window and include the  
'''


#===classes
class Moving_object(object):
    def __init__ (self, y=5, x=5, direction=0):
        self.y = y
        self.x = x
        self.direction = direction

    # Method to move this object
    def move(self):
        if self.direction == 0:
            self.x -= 1

        if self.direction == 1:
            self.x += 1
        
        if self.direction == 2:
            self.y -= 1
        
        if self.direction == 3:
            self.y += 1

    # Prevent object from 'escaping' from the window by 'wraparound' to other limit of window.
    def wraparound(self, min_y, max_y, min_x, max_x):
        if self.y <= min_y:
            self.y = max_y
        if self.y >= max_y:
            self.y = min_y

        if self.x <= min_x:
            self.x = max_x
        if self.x >= max_x:
            self.x = min_x


    def draw(self, window):
        window.addstr(self.y, self.x, "X")

class Snake(Moving_object):
    '''Player is a snake'''

    def __init__ (self, y=3, x=3, direction=0, score=0):
        self.y = y
        self.x = x
        self.direction = direction
        self.score = score

class Assailant:
    '''Enemy is not a snake'''
    def __init__ (self, y=4, x=4, direction = 2):
        pass
        
class Apple(object):
    '''Snakes eat apples, you see'''
    def __init__ (self, y=6, x=6, points=1):
        self.y=y
        self.x=x
        self.points = points
    
    def draw(self, window):
        window.addch(self.y, self.x, "A")

    def collision(self, Object):
        if (self.y == Object.y and self.x == Object.x):
            print ("Collision detected")
            del self
            return True
    
#===functions
def main(stdscr):
    '''run program'''
    stdscr.clear()
    stdscr.refresh()    

    # Set variables for windows
    max_height, max_width = stdscr.getmaxyx()   
    if max_height >= 25: max_height = 25
    if max_width >= 50: max_width = 50

    up_win_height = 5
    global up_win
    up_win = stdscr.subwin(5, max_width, 0, 0)
    
    win_height = max_height-up_win_height
    global win
    win = stdscr.subwin(win_height, max_width, up_win_height, 0)

    # Instantiate a new enemy, which will wander around in random directions
    enemy = Assailant()
    
    # Goal is to collect apples
    apple = Apple(9,9)
    
    # create player instance, all values default
    player = Snake(5,5)
    
    player.direction = 1
    button_direction = 1
    prev_button_direction = button_direction
    key = -1
    next_key = key

    # Get immediate feedback for key input, but don't repeat input of characters
    win.keypad(1)
    win.nodelay(1)
    
    # Timer and time limit
    counter = 0
    limit = 120
    scoreadd = 1

    while counter < limit:
        # Check if in this frame the y coordinate would be out of range.
        # If it would be out of range, change y so it's on the other side of the window.
        # Later on in the loop, will redraw in the correct place.

        #Args are: min_y, max_y, min_x, max_x
        
        player.wraparound(0, max_height, 0, max_width)

        '''
        if player.y < 0:
            player.y = win_height-1
        
        elif player.y > win_height-1:
            player.y = 0
        '''

        up_win.erase()
        win.erase()
        counter += 1        
        up_win.border(0)
        win.border(0)

        key = win.getch()
        
        if key == curses.KEY_LEFT and prev_button_direction != 1:
            button_direction, prev_button_direction, player.direction = 0, 0, 0 
        
        elif key == curses.KEY_RIGHT and prev_button_direction != 0:
            button_direction, prev_button_direction, player.direction = 1, 1, 1 

        elif key == curses.KEY_UP and prev_button_direction != 3:
            button_direction, prev_button_direction, player.direction = 2, 2, 2

        elif key == curses.KEY_DOWN and prev_button_direction != 2:
            button_direction, prev_button_direction, player.direction = 3, 3, 3
                
        else:
            pass
        
        player.draw(win)
        player.move()
        
        apple.draw(win)
        if apple.collision(player) == True:
            player.score += scoreadd
            scoreadd += 1
            print ("+",scoreadd, " added")
            del apple
            print ("An apple was eaten")
            randy = random.randint(int(max_height*0.2), int(max_height*0.5)) 
            randx = random.randint(int(max_width*0.2), int(max_width*0.5))
            apple = Apple(randy, randx, scoreadd)



        # Display debug info, update display and pause briefly:
        up_win.addstr(1, 2,
f"\
player={player.y}, {player.x}; \
Screen area={max_height},{max_width}; \
dir={player.direction}; \
key={key}, \
button={button_direction} \
prevbu={prev_button_direction} \
timer={limit-counter} \
score={player.score}")

        up_win.refresh()
        win.refresh()
        
        time.sleep(0.15)


    
    win.clear()
    win.nodelay(0)

    win.addstr(0,0, f"Final score was {player.score}")
    win.addstr(1,0, f"Press any key to exit.")
    win.refresh()
    key = win.getkey()

#===program runtime
if __name__ == "__main__":
    curses.wrapper(main)
    