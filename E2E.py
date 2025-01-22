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

# Función para editar el nombre de un amigo
def editar_amigo(posicion, nuevo_nombre):
    # Encuentra y haz clic en el botón de editar del amigo
    editar_button = driver.find_element(By.XPATH, f'/html/body/main/section/ul[1]/li[{posicion}]/button[1]')
    editar_button.click()  # Hace clic en el botón de editar
    time.sleep(1)

    # Interactuar con el prompt emergente
    alert = Alert(driver)

    # Mostrar mensaje de lo que estamos escribiendo en el prompt (se captura antes de enviarlo)
    print(f"Escribiendo en el prompt: '{nuevo_nombre}'")

    alert.send_keys(nuevo_nombre)  # Enviar el nuevo nombre al prompt
    alert.accept()  # Aceptar el prompt

    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# Editar los nombres de los amigos
editar_amigo(1, 'Amigo1_Editado')
editar_amigo(2, 'Amigo2_Editado')
editar_amigo(3, 'Amigo3_Editado')

# Función para eliminar un amigo
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
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# Eliminar el tercer amigo
eliminar_amigo()

# Espera a que el botón "Sortear amigo" sea visible
sortear_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div[2]/button')))

# Asegura que el botón esté en pantalla
driver.execute_script("arguments[0].scrollIntoView(true);", sortear_button)
time.sleep(1)

# Haz clic en el botón
print('Haciendo clic en el botón "Sortear amigo"')
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/div[2]/button'))).click()

# Pausa para observar el resultado
time.sleep(3)

# Cierra el navegador
driver.quit()
