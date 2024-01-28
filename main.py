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


us_states_coordinates = data.to_dict()
# print(data.loc[1])
# print(data.where(data.state == "Ohio"))
print(data.loc[data.state == "Ohio"])

def game_on(user):

    answer = turtle.textinput(title="Input us state name", prompt="What's the name of the U.S. State?")
    answer = answer.title()
    print(answer)


    if answer in us_states and answer not in user.states_remembered_list:
        print("True\n--------------------")
        user.states_remembered_list.append(answer)
        turtle.write(answer, True, align="center")
        # turtle.write((state_details.x, state_details.y), True)
        return user
    
    print("False\n--------------------")
    return user
    
    

while user.states_remembered_count < 50:
    user = game_on(user)
    
    
screen.mainloop()