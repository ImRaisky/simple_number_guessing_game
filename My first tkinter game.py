import tkinter
import random

window = tkinter.Tk()
window.config(bg="#263238")

color_gold = "#FDD835"
color_tea = "#7CB342"
light_tea = "#81C784"
color_brown = "#795548"
color_white = "#FFFFFF"
color_black = "#000000"
bg = "#263238"

point = 0
triesscore = 0
tries = 0
number = random.randint(0,100)

def main():
    global number, number_choosen, point, triesscore, tries

    try:
        number_choosen = int(input1.get("1.0", "end"))
    except ValueError:
            numlabel["text"] = "Please Enter A Valid Number !"
            input1.delete("1.0", "end")
            return

    if number > number_choosen:
        numlabel["text"] = str(number_choosen) +  " is too low"
        tries += 1
        trieslabel["text"] = "tries : " + str(tries)
        input1.delete("1.0", "end")
    elif number < number_choosen:
        numlabel["text"] = str(number_choosen) +  " is too high"
        tries += 1
        trieslabel["text"] = "tries : " + str(tries)
        input1.delete("1.0", "end")
    elif number == number_choosen:
        numlabel["text"] = str(number_choosen) + "You Got It !"
        point += 1
        ptlabel["text"] = "⭐point : " + str(point)
        input1.delete("1.0", "end")
        number = random.randint(0, 100)
        if triesscore < tries:
            triesscore = tries
            scorelabel["text"] = "🏆Best : " + str(triesscore)

label1 = tkinter.Label(window, text="Welcome !", font=("Arial", 32, "bold"), bg=bg, fg=color_gold)
numlabel = tkinter.Label(window, text="Enter A Number !", font=("Arial", 25), bg=bg, fg=color_tea)
input1 = tkinter.Text(window, font=("Arial", 30, "bold"), height=1, width=3, bg=bg, fg=color_black)
enter = tkinter.Button(window, text="Enter", command=main, font=("Arial", 20, "bold"), bg=light_tea, fg=color_white, padx=5, pady=10)
frame = tkinter.Frame(window, pady=20, bg=bg)
ptlabel = tkinter.Label(frame, text="⭐point : 0", font=("Arial", 15), bg=bg, fg=color_white)
scorelabel = tkinter.Label(frame, text="🏆Best : 0", font=("Arial", 15), bg=bg, fg=color_white)
trieslabel = tkinter.Label(window, text="tries : 0", font=("Arial", 15), bg=bg, fg=color_white)

label1.pack()
numlabel.pack()
input1.pack()
enter.pack()
frame.pack()
ptlabel.pack(side="left", padx=20)
scorelabel.pack(side="left", padx=20)
trieslabel.pack()
window.mainloop()