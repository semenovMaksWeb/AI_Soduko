import keyboard

def keyDown(schema, indexStart):
    activeRow = indexStart.get("indexRow")
    activeCol = indexStart.get("indexCol")

    def click(key):
       keyboard.press(key) 
    
    for row in schema:
        for col in row:
            if col.get("vvod"):
                if activeRow > col.get("indexRow"):
                    activeRow = activeRow - 1

                if activeRow < col.get("indexRow"):
                    activeRow = activeRow + 1

                if activeCol > col.get("indexCol"):
                    activeCol = activeCol - 1

                if activeCol < col.get("indexCol"):
                    activeCol = activeCol + 1