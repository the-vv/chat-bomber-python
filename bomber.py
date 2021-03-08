try:
    import pyautogui as pg
except ModuleNotFoundError:
    input('Install the required library: \'pyautogui\' before starting...\nPress enter to exit')
import time
import os

word = input('Enter message to send: ')
num = input('Enter number of times to send: ')
print('Place the cursor where you want to send messages')
print("sending in 10 secs")
for i in range(10):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Place the cursor where you want to send messages')
    print('Sending starts in', 10 - i, 'seconds')
    time.sleep(1)
count = 0
for i in range(int(num)):
    pg.write(word)
    pg.press('enter')
    count += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Sending ' + num + ' ' + '\'' + word + '\'' + '\nTotal Send:', count)

os.system('cls' if os.name == 'nt' else 'clear')
input('Operation Completed, press enter to exit...')
