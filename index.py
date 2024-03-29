import copyHtml
import parsing
import ai
import aiClick

path = 'https://soduko-online.com/ru/'
position = {'left': 1700, 'top': 140}
positionClose = {'left': 2550, 'top': 130}
fileName = "docx/dom.html"
copyHtml.copyHtml(path, position, fileName, False,positionClose)
print("end copyHtml")
parsingObject = parsing.pasringHtml(fileName)
print("end parsingObject")
schema = ai.logic(parsingObject.get("schema"))
print("end logic")
aiClick.keyDown(parsingObject.get("schema"),parsingObject.get("indexStart"))
print("end aiClick")