#Projeto desenvolvido para apresentação na feira de profissões do dia 17/10/2024
#Project developed for presentation at the career fair on 10/17/2024

#Ao finalizar apresentação; 
#apagar códigos html e css e salvar arquivo (ctrl s)

import pyautogui
import time

codigo_html1 = '''
 <div class="login-container">
        <div class="login-box">
            <h2>Login</h2>
            <p>Digite os seus dados de acesso no campo abaixo.</p>'''
codigo_html2 = '''<form>
                <label for="email">E-mail</label>
                <input type="email" id="email" placeholder="Digite seu e-mail">'''
codigo_html3 = '''<label for="password">Senha</label>
                <input type="password" id="password" placeholder="Digite sua senha">'''
codigo_html4 = '''<a href="#" class="forgot-password">Esqueci minha senha</a>
                
                <button type="submit">Acessar</button>
            </form>
        </div>
    </div>'''

codigo_css1 = '''
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}'''
codigo_css2 = '''
body {
    background-color: #4B0082; /* Fundo roxo */
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}'''
codigo_css3 = '''
.login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}'''
codigo_css4 = '''
.login-box {
    background-color: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    width: 300px;
    text-align: center;
}'''
codigo_css5 = '''
h2 {
    margin-bottom: 10px;
    color: #333;
}

p {
    font-size: 14px;
    margin-bottom: 20px;
    color: #666;
}'''
codigo_css6 = '''
form {
    display: flex;
    flex-direction: column;
}'''
codigo_css7 = '''
label {
    font-size: 14px;
    color: #333;
    text-align: left;
    margin-bottom: 5px;
}'''
codigo_css8 = '''
input {
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
}'''
codigo_css9 = '''
input::placeholder {
    color: #aaa;
}'''
codigo_css10 = '''
.forgot-password {
    color: #666;
    font-size: 12px;
    text-decoration: none;
    margin-bottom: 20px;
    display: block;
    text-align: left;
}'''
codigo_css11 = '''
button {
    padding: 10px;
    background-color: #FF4081; /* Botão rosa */
    border: none;
    color: white;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}'''
codigo_css12 = '''
button:hover {
    background-color: #e60073;
}'''


pyautogui.PAUSE = 1
pyautogui.click(x=344, y=70)
pyautogui.click(x=336, y=352)
pyautogui.scroll(5000)
pyautogui.click(x=193, y=323)

pyautogui.write(codigo_html1, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_html2, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_html3, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_html4, interval=0.01)
pyautogui.hotkey('ctrl', 's')

pyautogui.click(x=476, y=67)
pyautogui.click(x=161, y=124)

pyautogui.write(codigo_css1, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css2, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css3, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css4, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css5, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css6, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css7, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css8, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css9, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css10, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css11, interval=0.01)
pyautogui.hotkey('ctrl', 's')
pyautogui.write(codigo_css12, interval=0.01)
pyautogui.hotkey('ctrl', 's')

