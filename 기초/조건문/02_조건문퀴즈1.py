import pyautogui

current_price = int(pyautogui.prompt("현재 가격을 입력하세요"))

if current_price >= 90000:
    print("매도합니다")
elif current_price >= 80000:
    print("대기중입니다")
else:
    print("매수합니다")