import tkinter as tk
import cards

# window stuff

window = tk.Tk()
window.title("Flashcards")
window.geometry("800x600")

def button_press(event):
    print("button was pressed")
    #cards.addCard()


def addCardPopUp():
    popup = tk.Toplevel()
    popup.title("new card")
    popup.geometry("400x300")

    leftsideLabel = tk.Label(popup,text="Leftside")
    leftsideLabel.pack(pady=5)
    leftSideEntry = tk.Entry(popup)
    leftSideEntry.pack(pady=5)

    rightSideLabel = tk.Label(popup,text="Rightside")
    rightSideLabel.pack(pady=5)
    rightSideEntry = tk.Entry(popup)
    rightSideEntry.pack(pady=10)



    closeButton = tk.Button(popup, text="close", command=popup.destroy)
    closeButton.pack(pady=10)


                            

addCardButton = tk.Button( window, text="Add card", command=addCardPopUp)

addCardButton.pack()

showAllCardsButton = tk.Button(text="show Cards")
showAllCardsButton.bind("<Button-1>", button_press)
showAllCardsButton.pack()


# Start the event loop.
window.mainloop()