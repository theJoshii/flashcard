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

    topicLable = tk.Label(popup, text="Topic")
    topicLable.pack(pady=5)
    topicEntry = tk.Entry(popup)
    topicEntry.pack(pady=5)

    testBUtton = tk.Button(popup, text="test", command=lambda: print(f"{leftSideEntry.get()}"))
    testBUtton.pack(pady=5)

    addButton = tk.Button(popup, text="add", command=lambda: cards.addCard(leftSideEntry.get(),rightSideEntry.get(),topicEntry.get()))
    addButton.pack(pady=5)
    closeButton = tk.Button(popup, text="close", command=popup.destroy)
    closeButton.pack(pady=10)

def showCardsPopUp():
    popup = tk.Toplevel()
    popup.title("All cards")
    popup.geometry("400x300")

    data = cards.getAllCards()
    for i in range(21):
        table = tk.Label(popup, text=f"{data[i]}")
        table.grid(row=i)



mainMenu = tk.Menu(window)

profilMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Profil", menu=profilMenu)
profilMenu.add_command(label="Change Username", command= None)

settingsMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Settings", menu=settingsMenu)
settingsMenu.add_command(label="Repetition", command= None)

cardsMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Cards", menu=cardsMenu)
cardsMenu.add_command(label="Add  new aCard", command=addCardPopUp)
cardsMenu.add_command(label="Show all Cards", command=showCardsPopUp)
window.config(menu=mainMenu)



# Start the event loop.
window.mainloop()