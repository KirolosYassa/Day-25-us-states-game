import turtle
import pandas
import User
import os

screen = turtle.Screen()

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

user = User.User()

data = pandas.read_csv("50_states.csv")
us_states = data["state"].to_list()

if os.path.exists("missing_states.csv"):
    old_data = pandas.read_csv("missing_states.csv")
    print(old_data['0'].to_list())
    us_states_missed = old_data['0'].to_list()
    count = 0
    
    for state in us_states:
        if state not in us_states_missed:
            user.add_state(state)
            state_details = data.loc[data.state == state]
            x = int(state_details.x.iloc[0])
            y = int(state_details.y.iloc[0])
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x, y)
            # t.pendown()
            t.pencolor("green")
            t.write(state, True, align="center")
        



def game_on(user):

    answer = turtle.textinput(title=f"{user.states_remembered_count}/50 U.S. States", prompt="What's the name of the U.S. State?").title()
    print(answer)

    if answer == "Exit":
        user.exit_game()
    
    if answer == "Solve":
        for state in us_states:
            if state not in user.states_remembered_list:
                user.add_state(state)
                state_details = data.loc[data.state == state]
                x = int(state_details.x.iloc[0])
                y = int(state_details.y.iloc[0])
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(x, y)
                # t.pendown()
                t.pencolor("red")
                t.write(state, True, align="center")     
        user.exit_game()   
                
    if answer in us_states and answer not in user.states_remembered_list:
        user.add_state(answer)
        print("True\n--------------------")
        state_details = data.loc[data.state == answer]
        x = int(state_details.x.iloc[0])
        y = int(state_details.y.iloc[0])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        # t.pendown()
        t.pencolor("green")
        t.write(answer, True, align="center")
    else:
        print("False\n--------------------")
        
    return user
    
    

while user.states_remembered_count < 50:
    user = game_on(user)
    if user.continue_game == False:
        break

user.missing_states_list = [state for state in us_states if state not in user.states_remembered_list]

if len(user.missing_states_list) != 0:
    missing_states = pandas.DataFrame(user.missing_states_list)
    missing_states.to_csv("missing_states.csv")
else:
    os.remove("missing_states.csv")

screen.mainloop()