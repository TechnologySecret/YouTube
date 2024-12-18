# Write a Program Where Create A Game Snake and Pop-Up Mound/

from tkinter import*
import random

# body Setup of Snake   

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 300
SPACE_SIZE = 50
BODY_PARTS =1
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

 
class Snake: 
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
            
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

class Food: 
    def __init__(self):        
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) -1) *SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) -1) *SPACE_SIZE

        self.coordinates = (x, y)
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

# Funtion Generate

def next_turn(snake, food):
    global direction, score

    # Get the current head coordinates
    x, y = snake.coordinates[0]
    
    # Update the head position based on the current direction
    if direction == "Up":
        y -= SPACE_SIZE
    elif direction == "Down":
        y += SPACE_SIZE
    elif direction == "Left":
        x -= SPACE_SIZE
    elif direction == "Right":
        x += SPACE_SIZE

    # Insert the new head coordinates
    snake.coordinates.insert(0, (x, y))

    # checks if the snake eats food
    if (x, y) == food.coordinates:
        score +=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food.__init__()    #Generate a new food functions
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        
    # Draw the new head rectangle
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
    snake.squares.insert(0, square)
    
    # if x == food.coordinates[0]  and y == food.coordinates[-1]:
    #     global score
    #     score +=1
    #     label.config(text="Score:{}".format(score))
    #     canvas.delete("food")
    #     food = Food()

    # else:
    #     del snake.coordinates[-1]
    #     canvas.delete(snake.squares[-1])
    #     del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

# Prevent the snake from reversing direction

    if new_direction == "Up" and direction != "Down":
        direction = new_direction
    elif new_direction == "Down" and direction != "Up":
        direction = new_direction
    elif new_direction == "Left" and direction != "Right":
        direction = new_direction
    elif new_direction == "Right" and direction != "Left":
        direction = new_direction
    
def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() /2, 
                        canvas.winfo_width() /2,
                        font=("consolas",70), 
                        text="GAME OVER", 
                        fill="red", 
                        tags="game_over"
                        )


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down' 

label = Label(window, text="Score:{}".format(score), font=('consolas',40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH, )
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) -(window_width/2))
y = int((screen_height/2) -(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


window.bind('<Left>', lambda event: change_direction('Left'))
window.bind('<Right>', lambda event: change_direction('Right'))
window.bind('<Up>', lambda event: change_direction('Up'))
window.bind('<Down>', lambda event: change_direction('Down'))


snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
