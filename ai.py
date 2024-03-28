def logic(schema):

    def getSchema():
        for row in schema:
            for col in row:
                print(col)

    allNumber = {1,2,3,4,5,6,7,8,9}
    def checkNumberElement(col, val):
        if val != "" and col.get("val") == "":
                col.get("notNumber").add(int(val))

    def checkNumberAll(indexRowThis, indexColThis, colThis):
        for row in schema:
            val = row[indexColThis].get("val")
            checkNumberElement(colThis, val)
        
        for col in schema[indexRowThis]:
            val = col.get("val")
            checkNumberElement(colThis, val)
            indexRow1 = ""
            indexRow2 = ""
            indexCol1 = ""
            indexCol2 = ""
        
        if indexRow % 3 == 0:
            indexRow1 = indexRowThis + 1
            indexRow2 = indexRowThis + 2
        
        if indexRow % 3 == 1:
            indexRow1 = indexRowThis + 1
            indexRow2 = indexRowThis - 1

        if indexRow % 3 == 2:
            indexRow1 = indexRowThis - 1
            indexRow2 = indexRowThis - 2
        
        if indexCol % 3 == 0:
            indexCol1 = indexColThis + 1
            indexCol2 = indexColThis + 2

        if indexCol % 3 == 1:
            indexCol1 = indexColThis + 1
            indexCol2 = indexColThis - 1
        
        if indexCol % 3 == 2:
            indexCol1 = indexColThis - 1
            indexCol2 = indexColThis - 2

        checkNumberElement(colThis, schema[indexRow1][indexCol1].get("val"))
        checkNumberElement(colThis, schema[indexRow1][indexCol2].get("val"))
        checkNumberElement(colThis, schema[indexRow2][indexCol1].get("val"))
        checkNumberElement(colThis, schema[indexRow2][indexCol2].get("val"))

    def saveCheckNumber(col):
        if col.get("val") == "":
            checkNumber = allNumber.difference(col.get("notNumber"))
            col["checkNumber"] = list(checkNumber)

    for indexRow, row in enumerate(schema):
        for indexCol, col in enumerate(row):
            if col.get("val") == "" :
                checkNumberAll(indexRow, indexCol, col)
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
        checkNumberAll(indexRow, indexCol, col)
        saveCheckNumber(col)
        if col.get("checkNumber") and len(col.get("checkNumber")) == 1:
            # print(col)
            col.get("notNumber").add(col.get("checkNumber")[0])
            col["val"] = col.get("checkNumber")[0]
            col["vvod"] = True
            col["checkNumber"] = set()
            indexCol = -1
            indexRow = 0
    return schema

