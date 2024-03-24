from bs4 import BeautifulSoup

def pasringHtml():
    arraySchema = []
    file = open("docx/dom.html", "r", -1, "utf-8")
    soup = BeautifulSoup(file, 'lxml')
    
 
    
    indexColumn = -1
    indexRow = -1

    blockList = soup.select("#s7 > div")

    for index in range(0 , len(blockList)):
        arraySchema.insert(index, [])
    print(arraySchema)
    for block in blockList:
        indexRow = indexRow + 1
        for elem in block.select(".r1"):
            # print(elem)
            indexColumn = indexColumn + 1
            if indexColumn == 2:
                indexRow = indexRow + 1
            if indexColumn == 5:
                indexRow = indexRow + 1
            if indexColumn == 8:
                indexColumn = 0
                indexRow = indexRow - 2
            print(indexRow)
            arraySchema[indexRow].insert(indexColumn,elem.text)
    print(arraySchema)