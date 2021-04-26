import turtle
import pandas
from writestates import WriteStates
IMAGE_PATH = './blank_states_img.gif'
NO_OF_STATES = 50

user_score = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)


states_data = pandas.read_csv('50_states.csv').to_dict()
states = states_data['state']
states_correctly_guessed = []
states_x_cords = states_data['x']
states_y_cords = states_data['y']



while user_score < NO_OF_STATES:
    answer_state = screen.textinput(title=f"{user_score}/{NO_OF_STATES} States Correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break

    for i in range(NO_OF_STATES):
        if answer_state == states[i]:
            WriteStates(state_name=states[i], x_cord=states_x_cords[i], y_cord=states_y_cords[i])
            user_score += 1
            states_correctly_guessed.append(answer_state)

states_remaining = []

for i in range(NO_OF_STATES):
    if states[i] not in states_correctly_guessed:
        states_remaining.append(states[i])

df = pandas.DataFrame(states_remaining)
df.to_csv("learn.csv")











screen.exitonclick()