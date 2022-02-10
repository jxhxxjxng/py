#pyautogui는 입력받는 것. prompt는 창을 띄운다.
import pyautogui

bag_price = int(pyautogui.prompt("가방 가격을 입력하세요"))
watch_price = int(pyautogui.prompt("시계 가격을 입력하세요"))

aggregated_price = bag_price + watch_price

if aggregated_price >= 100000:
    discount_rate = 0.3
elif aggregated_price >= 50000:
    discount_rate = 0.2
else:
    discount_rate = 0.1
    
discounted_price = (1 - discount_rate) * aggregated_price
print("지불하실 가격은 " + str(discounted_price) + " 원 입니다.")