import pyautogui
import time
import pandas as pd
import keyboard


# Carrega o txt com o Search a ser procurado
search_hashs = pd.read_csv('hash_pesquisa.txt')
print(search_hashs)

# Define a callback function to stop the application when the 'esc' key is pressed
def on_esc_pressed():
    print('Stopping application...')
    keyboard.unhook_all() # This line will unregister all hotkeys and stop the application

# Register the callback function for the 'esc' key
keyboard.add_hotkey('esc', on_esc_pressed)

# abrir o Chrome
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(8)


# Percorre pela lista "search_hashs" e abre cada hash em paginas diferentes
for hash in search_hashs['Search_Paginas']:
    print(hash)

    # entrar no link
    link = "https://www.virustotal.com/"
    pyautogui.write(link)
    pyautogui.press("enter")

    # esperar o site carregar
    time.sleep(5)

    # navega ate o "search" atraves do tab
    pyautogui.press('tab', presses=10)
    pyautogui.press("enter")
    time.sleep(1)

    # Entra no espaço de escrita e preescreve a hash que vai ser utilizada pelo txt "pags_pesquisa1"
    pyautogui.press('tab')
    pyautogui.write(f"{hash}")
    pyautogui.press("enter")

    # abre uma nova aba/guia
    pyautogui.hotkey('ctrl', "t")