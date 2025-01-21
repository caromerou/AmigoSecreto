from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura el controlador de Selenium (aquí usamos Chrome)
driver = webdriver.Chrome()

# Abre la URL
driver.get('https://caromerou.github.io/AmigoSecreto/')

# Espera a que la página se cargue
time.sleep(2)

# Hacer scroll hacia abajo
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Lista de nombres de amigos
nombres_amigos = ['Amigo1', 'Amigo2', 'Amigo3']

for nombre in nombres_amigos:
    # Encuentra el campo de texto e ingresa el nombre
    input_field = driver.find_element(By.XPATH, '/html/body/main/section/div[1]/input')
    input_field.send_keys(nombre)
    time.sleep(1)

    # Encuentra y haz clic en el botón de añadir
    add_button = driver.find_element(By.XPATH, '/html/body/main/section/div[1]/button')
    add_button.click()
    time.sleep(1)

# Espera un momento antes de cerrar el navegador
time.sleep(3)

# Cierra el navegador
driver.quit()
