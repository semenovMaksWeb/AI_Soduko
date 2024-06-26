import webbrowser
import keyboard
from time import sleep
import pyautogui
import pyperclip

def copyHtml(path, position, fileName, checkF12 = True, positionClose = None, time = 5):
    webbrowser.open(path, new=2) # Открыть вкладку
    sleep(time) # Ожидание её загрузки
    
    # Трудно
    # pyautogui.moveTo(1500, 400, duration = 0.25)
    # pyautogui.click()
    # sleep(5)
    
    # Средне
    pyautogui.moveTo(1500, 360, duration = 0.25)
    pyautogui.click()
    sleep(5)
    
    # Магия копирования html через f12 для этого нужно указать позицию где будет край браузера
    if checkF12:
        keyboard.press("F12")
    # Магия открытие f12 когда скриптами js заблокировано открытие
    else:
       pyautogui.moveTo(500, 500, duration = 0.25) 
       sleep(2)
       pyautogui.rightClick()
       pyautogui.moveTo(500, 940, duration = 0.25)
       pyautogui.click()
    
    sleep(2)
    pyautogui.moveTo(position.get("left"), position.get("top"), duration = 0.25)
    pyautogui.click()
    sleep(1)
    pyautogui.moveTo(position.get("left"), position.get("top") + 40, duration = 0.25)
    pyautogui.click()
    sleep(3)
    keyboard.press("ctrl+c")
    sleep(3)
    # получение значения с браузера и сохранение его в файл
    html = pyperclip.waitForPaste()
    file = open(fileName, "w+", -1, "utf-8")
    file.write(html)
    file.close()
    print("Создан файл")
    if checkF12:
        keyboard.press("F12")
    if positionClose:
        pyautogui.moveTo(positionClose.get("left"), positionClose.get("top"), duration = 0.25)
        pyautogui.click()