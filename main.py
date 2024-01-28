import turtle
import pandas
import User

screen = turtle.Screen()

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
us_states = data["state"].to_list()
states_remembered = 0

def game_on(states_remembered):

    answer = turtle.textinput(title="Input us state name", prompt="What's the name of the U.S. State?")
    answer = answer.title()
    print(answer)


    if answer in us_states:
        return states_remembered + 1

while states_remembered < 50:
    states_remembered = game_on(states_remembered)
    
    
screen.mainloop()