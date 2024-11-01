import tkinter as tk
import cards

window = tk.Tk()
window.title("Anki clone")

def button_press(event):
    print("button was pressed")
    #cards.addCard()

addCardButton = tk.Button(text="Add card")
showAllCardsButton = tk.Button(text="show Cards")

addCardButton.bind("<Button-1>", button_press)
addCardButton.pack()

showAllCardsButton.bind("<Button-1>", button_press)
showAllCardsButton.pack()


# Start the event loop.
window.mainloop()