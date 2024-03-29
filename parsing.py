from bs4 import BeautifulSoup

def pasringHtml(fileName):
    indexStart = None
    arraySchema = []
    file = open(fileName, "r", -1, "utf-8")
    soup = BeautifulSoup(file, 'lxml')

    blockList = soup.select("#s7 > div")    
    for indexBlock, block in enumerate(blockList):
        arraySchema.insert(indexBlock , [])

    for elem in soup.select(".r1"):
        strElem = elem.text.replace(" ", "").replace("\n", "")
        idText = elem.attrs.get("id")
        idText = idText[3:len(idText)]
        indexCol = int(idText[0:1])
        indexRow = int(idText[2:3])
        if strElem != "":
            arraySchema[indexRow].insert(int(indexCol), {"val": int(strElem), "indexRow":indexRow, "indexCol":indexCol })
        else:
            if indexStart == None:
                indexStart = {"indexRow":indexRow, "indexCol": indexCol }
            arraySchema[indexRow].insert(int(indexCol), {"val": "", "indexRow":indexRow, "indexCol":indexCol, "checkNumber": set(), "notNumber": set() })
    return {"schema": arraySchema, "indexStart": indexStart}