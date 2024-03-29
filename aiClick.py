import keyboard
from time import sleep

def keyDown(schema, indexStart):
    activeRow = indexStart.get("indexRow")
    activeCol = indexStart.get("indexCol")

    def click(key):
       print("Был сделан клик", key)
       sleep(0.1)
       keyboard.press(key) 
       sleep(0.5)
    
    for row in schema:
        for col in row:
            if col.get("vvod"):
                while(True):
                    if activeRow > col.get("indexRow"):
                        activeRow = activeRow - 1
                        click("up")

                    if activeRow < col.get("indexRow"):
                        activeRow = activeRow + 1
                        click("down")

                    if activeCol > col.get("indexCol"):
                        activeCol = activeCol - 1
                        click("left")

                    if activeCol < col.get("indexCol"):
                        activeCol = activeCol + 1
                        click("right")
                
                    if activeCol == col.get("indexCol") and activeRow == col.get("indexRow"):
                        click(str(col.get("val")))
                        break
    print("победа?")
                