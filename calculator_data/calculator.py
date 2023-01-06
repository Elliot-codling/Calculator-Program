#calcuator program in pygame written in python
import pygame, os
from engine import game_engine_50123 as game_engine
pygame.font.init()

file_dir = os.getcwd()
#create window
w, h = 340, 300
window = game_engine.window.define("Galculator", w, h)

#variables
run = True
clock = pygame.time.Clock()
result = 0
operation = None
inputNum1 = ""
inputNum2 = ""
stage = 0
screen = ""

#lists
#display
display = []
background = game_engine.properties_object("background", f"{file_dir}/textures/background.png", 0, 0, w, h, False)
display += [background]
#display_sprite
display_sprite = []
#foreground
foreground = []
#text_foreground
text_foreground = []

#sub code -----------------------------------------------
#init buttons
def init_buttons():
    global foreground, text_foreground
    #screen - row 0
    screen_text = game_engine.properties_text("screen_text", f" {screen} ", "white", w, h - 250, 45, True)
    #text - row 1
    number1 = game_engine.properties_text("number1", "  1  ", "white", 20, 60, 45, False)
    number2 = game_engine.properties_text("number2", "  2  ", "white", 100, 60, 45, False)
    number3 = game_engine.properties_text("number3", "  3  ", "white", 180, 60, 45, False)
    divide_text = game_engine.properties_text("divide_text", "  /  ", "white", 260, 60, 45, False)
    #row 2
    number4 = game_engine.properties_text("number4", "  4  ", "white", 20, 120, 45, False)
    number5 = game_engine.properties_text("number5", "  5  ", "white", 100, 120, 45, False)
    number6 = game_engine.properties_text("number6", "  6  ", "white", 180, 120, 45, False)
    multiply_text = game_engine.properties_text("multipy_text", "  *  ", "white", 260, 120, 45, False)
    #row 3
    number7 = game_engine.properties_text("number7", "  7  ", "white", 20, 180, 45, False)
    number8 = game_engine.properties_text("number8", "  8  ", "white", 100, 180, 45, False)
    number9 = game_engine.properties_text("number9", "  9  ", "white", 180, 180, 45, False)
    add_text = game_engine.properties_text("add_text", "  +  ", "white", 260, 180, 45, False)
    #row 4
    equal_text = game_engine.properties_text("equal_text", "  =  ", "white", 20, 240, 45, False)
    number0 = game_engine.properties_text("number0", "  0  ", "white", 100, 240, 45, False)
    clear_text = game_engine.properties_text("clear_text", "  c  ", "white", 180, 240, 45, False)
    sub_text = game_engine.properties_text("sub_text", "  -  ", "white", 260, 240, 45, False)
    #screen - row 0
    screen_outline = game_engine.properties_object("screen_outline", f"{file_dir}/textures/button.png", 5, screen_text.y - 5, w - 10, screen_text.texture.get_height() + 11, True)
    #buttons - row 1
    button1 = game_engine.properties_object("button1", f"{file_dir}/textures/button.png", number1.x - 10, number1.y - 10, number1.texture.get_width() + 20, number1.texture.get_height() + 20, True)
    button2 = game_engine.properties_object("button2", f"{file_dir}/textures/button.png", number2.x - 10, number2.y - 10, number2.texture.get_width() + 20, number2.texture.get_height() + 20, True)
    button3 = game_engine.properties_object("button3", f"{file_dir}/textures/button.png", number3.x - 10, number3.y - 10, number3.texture.get_width() + 20, number3.texture.get_height() + 20, True)
    divide_button = game_engine.properties_object("divide_button", f"{file_dir}/textures/button.png", divide_text.x - 10, divide_text.y - 10, divide_text.texture.get_width() + 20, divide_text.texture.get_height() + 20, True)
    #row 2
    button4 = game_engine.properties_object("button4", f"{file_dir}/textures/button.png", number4.x - 10, number4.y - 10, number4.texture.get_width() + 20, number4.texture.get_height() + 20, True)
    button5 = game_engine.properties_object("button5", f"{file_dir}/textures/button.png", number5.x - 10, number5.y - 10, number5.texture.get_width() + 20, number5.texture.get_height() + 20, True)
    button6 = game_engine.properties_object("button6", f"{file_dir}/textures/button.png", number6.x - 10, number6.y - 10, number6.texture.get_width() + 20, number6.texture.get_height() + 20, True)
    multiply_button = game_engine.properties_object("multiply_button", f"{file_dir}/textures/button.png", multiply_text.x - 10, multiply_text.y - 10, multiply_text.texture.get_width() + 20, multiply_text.texture.get_height() + 20, True)
    #row 3
    button7 = game_engine.properties_object("button7", f"{file_dir}/textures/button.png", number7.x - 10, number7.y - 10, number7.texture.get_width() + 20, number7.texture.get_height() + 20, True)
    button8 = game_engine.properties_object("button8", f"{file_dir}/textures/button.png", number8.x - 10, number8.y - 10, number8.texture.get_width() + 20, number8.texture.get_height() + 20, True)
    button9 = game_engine.properties_object("button9", f"{file_dir}/textures/button.png", number9.x - 10, number9.y - 10, number9.texture.get_width() + 20, number9.texture.get_height() + 20, True)
    add_button = game_engine.properties_object("add_button", f"{file_dir}/textures/button.png", add_text.x - 10, add_text.y - 10, add_text.texture.get_width() + 20, add_text.texture.get_height() + 20, True)
    #row 4
    equal_button = game_engine.properties_object("equal_button", f"{file_dir}/textures/button.png", equal_text.x - 10, equal_text.y - 10, equal_text.texture.get_width() + 20, equal_text.texture.get_height() + 20, True)
    button0 = game_engine.properties_object("button0", f"{file_dir}/textures/button.png", number0.x - 10, number0.y - 10, number0.texture.get_width() + 20, number0.texture.get_height() + 20, True)
    clear_button = game_engine.properties_object("clear_button", f"{file_dir}/textures/button.png", clear_text.x - 10, clear_text.y - 10, clear_text.texture.get_width() + 20, clear_text.texture.get_height() + 20, True)
    sub_button = game_engine.properties_object("sub_button", f"{file_dir}/textures/button.png", sub_text.x - 10, sub_text.y - 10, sub_text.texture.get_width() + 20, sub_text.texture.get_height() + 20, True)
    
    foreground += [button1, button2, button3, button4, button5, button6, button7, button8, button9, button0, equal_button, clear_button, divide_button, multiply_button, add_button, sub_button, screen_outline]
    text_foreground += [number1, number2, number3, number4, number5, number6, number7, number8, number9, number0, equal_text, clear_text, divide_text, multiply_text, add_text, sub_text, screen_text]

def update_display(entered_text):               #updates the display at the top of the calculator - requires data to be updated
    global foreground, text_foreground
    global screen
    screen = entered_text
    foreground = []
    text_foreground = []
    init_buttons()

def update_numbers(inputted_number, stage):             #updates the numbers according to the stage
    global inputNum1, inputNum2
    if stage == 0:
        inputNum1 += inputted_number
        update_display(inputNum1)
    else:
        inputNum2 += inputted_number
        update_display(inputNum2)    

def calculate(a, b, operation):         #calculates the answer from the input of a, b and the operation passed through
    a = int(a)
    b = int(b)
    if operation == "/":
        update_display(a / b)
    elif operation == "*":
        update_display(a * b)
    elif operation == "+":
        update_display(a + b)
    elif operation == "-":
        update_display(a - b)

def set_op(operation):                  #sets the operation to be displayed on the screen
    global stage
    stage += 1
    update_display(operation)
    return operation

#main code 
def main():
    #collisions of all the buttons - these then can control the functions of each button.
    global operation, inputNum1, inputNum2, stage
    #row 1
    pygame.time.delay(105)
    if not pygame.mouse.get_pressed()[0]:
        pass
    elif game_engine.mouse.collision("button1", foreground):
        update_numbers("1", stage)
    elif game_engine.mouse.collision("button2", foreground):
        update_numbers("2", stage)
    elif game_engine.mouse.collision("button3", foreground):
        update_numbers("3", stage)
    elif game_engine.mouse.collision("divide_button", foreground):
        operation = set_op("/")
    #row 2
    elif game_engine.mouse.collision("button4", foreground):
        update_numbers("4", stage)
    elif game_engine.mouse.collision("button5", foreground):
        update_numbers("5", stage)
    elif game_engine.mouse.collision("button6", foreground):
        update_numbers("6", stage)
    elif game_engine.mouse.collision("multiply_button", foreground):
        operation = set_op("*")
    #row 3
    elif game_engine.mouse.collision("button7", foreground):
        update_numbers("7", stage)
    elif game_engine.mouse.collision("button8", foreground):
        update_numbers("8", stage)
    elif game_engine.mouse.collision("button9", foreground):
        update_numbers("9", stage)
    elif game_engine.mouse.collision("add_button", foreground):
        operation = set_op("+")
    #row 4
    elif game_engine.mouse.collision("equal_button", foreground):
        calculate(inputNum1, inputNum2, operation)
    elif game_engine.mouse.collision("button0", foreground):
        update_numbers("0", stage)
    elif game_engine.mouse.collision("clear_button", foreground):
        inputNum1, inputNum2, stage, operation = "", "", 0, None
        update_display("")
    elif game_engine.mouse.collision("sub_button", foreground):
        operation = set_op("-")
    
#init the buttons to appear on screen
init_buttons()
while run:
    #keyboard and exit button, main code -----------------------------
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    main()
    game_engine.window.update(window, display, display_sprite, foreground, text_foreground, clock, 0)
    clock.tick(30)

pygame.quit()
print("Quiting...")