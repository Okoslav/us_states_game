from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("Státy v USA")
image = "blank_states_img.gif"
screen.addshape(image)
obrazovka = Turtle()
obrazovka.shape(image)

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].tolist()
guessed_states = []

while len(list_of_states) != len(guessed_states):

    answer_state = screen.textinput(title=f"Tvoje body:{len(guessed_states)}/50", prompt="Napiš jméno státu.").title()
    state_x = data[data.state == answer_state].x
    state_y = data[data.state == answer_state].y

    if answer_state == "Exit":

        states_to_learn = [state for state in list_of_states if state not in guessed_states]

        pandas.DataFrame(states_to_learn).to_csv("States_to_learn-csv")

        break

    if answer_state in list_of_states and answer_state not in guessed_states:

        guessed_states.append(answer_state)
        odpoved = Turtle()
        odpoved.hideturtle()
        odpoved.penup()
        odpoved.goto(int(state_x), int(state_y))
        odpoved.write(f"{answer_state}", align="left", font=("Arial", 10, "normal"))





