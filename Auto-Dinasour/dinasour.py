
import pyautogui as gui
import time
import keyboard 
import math
screenWidth, screenHeight = gui.size() # Get the size of the primary monitor.
print(screenWidth, screenHeight)

last_jumping =0
current_jumping=0
# jumping = 0 
time_diff = 0
x, y, width, height = 0, 102, 1920, 872

x_start,x_end = 400, 415


while True:
    scan_obstacle = gui.screenshot(region=(x, y, width, height))
    back_ground = scan_obstacle.getpixel((100,100))
    
    for i in range(x_end,x_start,-1):
        if scan_obstacle.getpixel((i,557)) != back_ground or scan_obstacle.getpixel((i,486)) != back_ground:
            keyboard.press("up")
            current_jumping = time.time()
            break
        
        if scan_obstacle.getpixel((i,460)) != back_ground:
            keyboard.press("down")
            time.sleep(0,3)
            keyboard.release("down")
            break
        
        
    
    _current_time_diff = current_jumping - last_jumping
    
    if time_diff != 0 and math.floor(_current_time_diff) != math.floor(time_diff):
        if x_end < width:   
            x_end +=3
        else:
            x_end = width
            
    
    time_diff = _current_time_diff
    last_jumping = current_jumping
    
    
    
    