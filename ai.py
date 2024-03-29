import env

def logic(schema):
    allNumber = {1,2,3,4,5,6,7,8,9}
    
    def getAllCheckArray(colThis):
        colArray = []
        for row in schema:
            colArray.append(row[colThis.get("indexCol")])

        for col in schema[colThis.get("indexRow")]:
            colArray.append(col)
        
        indexRow1 = ""
        indexRow2 = ""
        indexCol1 = ""
        indexCol2 = ""
        
        if indexRow % 3 == 0:
            indexRow1 = colThis.get("indexRow") + 1
            indexRow2 = colThis.get("indexRow") + 2
        
        if indexRow % 3 == 1:
            indexRow1 = colThis.get("indexRow") + 1
            indexRow2 = colThis.get("indexRow") - 1

        if indexRow % 3 == 2:
            indexRow1 = colThis.get("indexRow") - 1
            indexRow2 = colThis.get("indexRow") - 2
        
        if indexCol % 3 == 0:
            indexCol1 = colThis.get("indexCol") + 1
            indexCol2 = colThis.get("indexCol") + 1

        if indexCol % 3 == 1:
            indexCol1 = colThis.get("indexCol")  + 1
            indexCol2 = colThis.get("indexCol")  - 1
        
        if indexCol % 3 == 2:
            indexCol1 = colThis.get("indexCol") - 1
            indexCol2 = colThis.get("indexCol") - 2
        print("indexRow1, indexCol1", indexRow1, indexCol1)
        colArray.append(schema[indexRow1][indexCol1])
        colArray.append(schema[indexRow1][indexCol2])
        colArray.append(schema[indexRow2][indexCol1])
        colArray.append(schema[indexRow2][indexCol2])
        return colArray
        
    def getSchema():
        for row in schema:
            for col in row:
                print(col)

 
    
    def checkNumberElement(col, val):
        if val != "" and col.get("val") == "":
                col.get("notNumber").add(int(val))

    def checkNumberAll(colThis):
        elemArray = getAllCheckArray(colThis)
        for elem in elemArray:
            print(elem)
            checkNumberElement(colThis, elem.get("val"))

    def saveCheckNumber(col):
        if col.get("val") == "":
            checkNumber = allNumber.difference(col.get("notNumber"))
            col["checkNumber"] = list(checkNumber)

    for indexRow, row in enumerate(schema):
        for indexCol, col in enumerate(row):
            if col.get("val") == "" :
                checkNumberAll(col)
                saveCheckNumber(col)
    
    # print(getSchema())
    indexCol = -1
    indexRow = 0
    while(True):
        if(indexRow == 8 and indexCol == 8):
            break
        if(indexCol == 8):
            indexCol = -1
            indexRow = indexRow + 1
        indexCol = indexCol + 1
        col = schema[indexRow][indexCol]
        checkNumberAll(col)
        saveCheckNumber(col)
        if col.get("checkNumber") and len(col.get("checkNumber")) == 1:
            col.get("notNumber").add(col.get("checkNumber")[0])
            col["val"] = col.get("checkNumber")[0]
            col["vvod"] = True
            col["checkNumber"] = set()
            indexCol = -1
            indexRow = 0
        
    print(getSchema())
    return schema
    
