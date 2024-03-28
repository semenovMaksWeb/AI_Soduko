import copyHtml
import parsing
import ai
import fakeDomTest

schema = parsing.pasringHtml()
schema = ai.logic(schema)
fakeDomTest.fakeDomTest(schema)
path = 'https://soduko-online.com/ru/'
position = {'left': 1700, 'top': 140}
fileName = "dom.html"
# copyHtml.copyHtml(path, position, fileName, False)