import pyautogui
import time
import pandas as pd


# Carrega o txt com o Search a ser procurado
search_hashs = pd.read_csv('hash_pesquisa.txt')
print(search_hashs)


# abrir o Chrome
pyautogui.PAUSE = 1.0

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

# Percorre pela lista "search_hashs" e abre cada hash em paginas diferentes
for hash in search_hashs['Search_Paginas']:
    print(hash)

    # entrar no link
    link = "https://www.virustotal.com/"
    pyautogui.write(link)
    pyautogui.press("enter")

    # esperar o site carregar
    time.sleep(4)

    # navega ate o "search" atraves do tab
    pyautogui.press('tab', presses=10)
    pyautogui.press("enter")
    time.sleep(4)

    # Entra no espaço de escrita e preescreve a hash que vai ser utilizada pelo txt "pags_pesquisa1"
    pyautogui.press('tab')
    pyautogui.write(f"{hash}")
    pyautogui.press("enter")

    # abre uma nova aba/guia
    pyautogui.hotkey('ctrl', "t")