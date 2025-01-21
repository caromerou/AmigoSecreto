from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

# Configura el controlador de Selenium (aquí usamos Chrome)
driver = webdriver.Chrome()

# Abre la URL
driver.get('https://caromerou.github.io/AmigoSecreto/')

# Espera hasta que el campo de texto esté presente
wait = WebDriverWait(driver, 10)
input_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div[1]/input')))

# Hacer scroll hacia abajo para ver la página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Lista de nombres de amigos
nombres_amigos = ['Amigo1', 'Amigo2', 'Amigo3']

# Añadir amigos
for nombre in nombres_amigos:
    # Encuentra el campo de texto e ingresa el nombre
    input_field = driver.find_element(By.XPATH, '/html/body/main/section/div[1]/input')
    input_field.send_keys(nombre)
    time.sleep(1)

    # Encuentra y haz clic en el botón de añadir
    add_button = driver.find_element(By.XPATH, '/html/body/main/section/div[1]/button')
    add_button.click()
    time.sleep(1)

# Hacer otro scroll hacia abajo después de agregar Amigo3 para asegurar que todo sea visible
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)


# Función para eliminar el tercer amigo (Amigo3)
def eliminar_amigo():
    # Encuentra y haz clic en el botón de eliminar del tercer amigo
    eliminar_button = driver.find_element(By.XPATH, '/html/body/main/section/ul[1]/li[3]/button[2]')
    eliminar_button.click()  # Hace clic en el botón de eliminar
    time.sleep(1)

    # Maneja la ventana emergente (alerta)
    alert = Alert(driver)
    print("Aceptando la ventana emergente para confirmar la eliminación...")
    alert.accept()  # Acepta la acción en la ventana emergente
    time.sleep(1)


# Eliminar el tercer amigo (Amigo3)
eliminar_amigo()

# Espera un momento antes de cerrar el navegador
time.sleep(3)

# Cierra el navegador
driver.quit()
