import json
import os


def addCard(leftSide, rightSide, topic):

    newCard = {
        "leftSide" : leftSide,
        "rightSide": rightSide,
        "topic": topic
    }
    with open( "cards.json", "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
    
    data.append(newCard)
    with open("cards.json", "w") as file:
        json.dump(data, file, indent=4)



addCard("OOP", "Object oriented programming", "Programming")


