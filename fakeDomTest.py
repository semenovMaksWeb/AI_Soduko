from bs4 import BeautifulSoup

def fakeDomTest(schema):
    file = open("docx/dom.html", "r", -1, "utf-8")
    soup = BeautifulSoup(file, 'lxml')
    for indexRow, row in enumerate(schema):
        for indexCol, col in enumerate(row):
            idText = "vc_" + str(indexCol) + "_" + str(indexRow)
            elem = soup.select_one("#" + idText)
            print(elem)
            if col.get("vvod"):
                print(idText)
                elem.append(str(col.get("val")))


    fileSave = open("docx/dom_check.html", "w+", -1, "utf-8")
    fileSave.write(soup.prettify())
    fileSave.close()