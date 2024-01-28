import turtle
import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
us_states = data["state"].to_list()
states_remembered = 0
states_remembered_list = []

def game_on(states_remembered, states_remembered_list):

    answer = turtle.textinput(title=f"{states_remembered}/50 states", prompt="What's the name of the U.S. State?")
    answer = answer.title()
    print(answer)

    if answer in us_states and answer not in states_remembered_list:
        print("True\n--------------------------------")
        states_remembered_list.append(answer)
        return states_remembered + 1, states_remembered_list

    print("False\n--------------------------------")
    return states_remembered, states_remembered_list
    
while states_remembered < 50:
    states_remembered, states_remembered_list = game_on(states_remembered, states_remembered_list)
    
    
screen.mainloop()