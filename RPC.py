import tkinter as tk
from tkinter import ttk
import random

def play():
    player_choice = player_choice_var.get()
    computer_choice = random.choice(choices)
    
    player_choice_icon.config(image=icons[player_choice])
    computer_choice_icon.config(image=icons[computer_choice])
    
    if player_choice == computer_choice:
        result_var.set("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_var.set("You win!")
    else:
        result_var.set("Computer wins!")

# Create the main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Load icons
rock_icon = tk.PhotoImage(file="Rock.png")
paper_icon = tk.PhotoImage(file="Paper.png")
scissors_icon = tk.PhotoImage(file="Scissor.png")

# Icon dictionary
icons = {
    "Rock": rock_icon,
    "Paper": paper_icon,
    "Scissors": scissors_icon,
}

# Define the choices
choices = ["Rock", "Paper", "Scissors"]

# Widgets
label = tk.Label(root, text="Select your choice:", font=("Arial", 16))
label.pack()

player_choice_var = tk.StringVar(root)
player_choice_var.set(choices[0])

player_choice_menu = ttk.Combobox(root, textvariable=player_choice_var, values=choices, font=("Arial", 14))
player_choice_menu.pack()

play_button = tk.Button(root, text="Play", command=play, font=("Arial", 14))
play_button.pack()

player_choice_icon = tk.Label(root, image=rock_icon)
player_choice_icon.pack()

computer_choice_icon = tk.Label(root, image=rock_icon)
computer_choice_icon.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 16))
result_label.pack()

# Start the main event loop
root.mainloop()
