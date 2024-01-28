import turtle
import pandas
import User

screen = turtle.Screen()

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
us_states = data["state"].to_list()
user = User.User()
us_states_dict = data["state"].to_dict()


def game_on(user):

    answer = turtle.textinput(title=f"{user.get_states_remembered_count()}/50 states", prompt="What's the name of the U.S. State?")
    answer = answer.title()
    print(answer)

    if answer in us_states and answer not in user.get_states_remembered_list():
        print("True\n--------------------------------")
        user.states_remembered_list.append(answer)
        user.states_remembered_count += 1
        
        turtle.write(answer, True, align="center")
        # turtle.write((0,0), True)

        return user

    print("False\n--------------------------------")
    return user

    
while user.get_states_remembered_count() < 50:
    user = game_on(user)
    
    
screen.mainloop()