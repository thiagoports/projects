#Automação desenvolvida utilizando as aulas da Hashtag Treinamentos
#Automation developed using Hashtag Trainings classes

import pyautogui
import time
import pandas 

pyautogui.PAUSE = 0.3

#pyautogui.press("win")
#pyautogui.write("opera")
#pyautogui.press("enter")

pyautogui.click(x=472, y=56)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(10)

pyautogui.click(x=609, y=411)

pyautogui.write("thiago123@teste.com")
pyautogui.press("tab") 
pyautogui.write("senha12345")
pyautogui.click(x=676, y=562) 
time.sleep(10)


tabela = pandas.read_csv("C:/Users/thiag/Projetos/autobot/produtos.csv")

print(tabela)

for linha in tabela.index:
    
    pyautogui.click(x=565, y=287)
    
    codigo = tabela.loc[linha, "codigo"]
    
    pyautogui.write(str(codigo))
    
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    pyautogui.scroll(5000)
    