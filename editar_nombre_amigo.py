from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


# Función para editar el nombre del tercer amigo (Amigo3) y cambiarlo por 'AMIGOEDITADO'
def editar_nombre():
    # Encuentra y haz clic en el botón de editar del tercer amigo
    editar_button = driver.find_element(By.XPATH, '/html/body/main/section/ul[1]/li[3]/button[1]')
    editar_button.click()  # Hace clic en el botón de editar
    time.sleep(1)

    # Interactuar con el prompt emergente
    alert = Alert(driver)

    # Mostrar mensaje de lo que estamos escribiendo en el prompt (se captura antes de enviarlo)
    print("Escribiendo en el prompt: 'AMIGOEDITADO'")

    alert.send_keys('AMIGOEDITADO')  # Enviar el nuevo nombre al prompt
    alert.accept()  # Aceptar el prompt

    time.sleep(1)


# Editar el tercer amigo (Amigo3) y cambiar su nombre a 'AMIGOEDITADO'
editar_nombre()

# Espera un momento antes de cerrar el navegador
time.sleep(3)

# Cierra el navegador
driver.quit()
