import pyautogui

money  = int(pyautogui.prompt("돈을 입력해 주세요"))
if money >= 20000:
    print("치맥 어때요!")
elif money >= 10000:
    print("떡볶이 어때요!")
else:
    print("편의점이나 가라 그지야")