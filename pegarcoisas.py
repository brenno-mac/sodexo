from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configurando as opções do Chrome
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Executar em modo headless (sem exibição gráfica)
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# Caminho para o executável do ChromeDriver
webdriver_service = Service('chromedriver.exe')

# Inicializando o driver do Chrome
driver = webdriver.Chrome(service=webdriver_service)

# Exemplo de uso do driver
# driver.get("https://www.google.com/search?q=hospital+benefic%C3%AAncia+portuguesa+sp&ei=DpxaZPCnJ7fK1sQPpNeDgAo&ved=0ahUKEwjw5vm9-ej-AhU3pZUCHaTrAKAQ4dUDCA8&uact=5&oq=hospital+benefic%C3%AAncia+portuguesa+sp&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzILCC4QgAQQxwEQrwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIICAAQFhAeEA8yBggAEBYQHjIZCC4QgAQQxwEQrwEQlwUQ3AQQ3gQQ4AQYAjoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQzoVCC4QrwEQxwEQigUQyAMQsAMQQxgBOhUILhCKBRDHARCvARDIAxCwAxBDGAE6BwgAEIoFEEM6CwguEK8BEMcBEIAESgQIQRgAULgDWL8FYO4GaAFwAXgAgAGxAYgBpQOSAQMwLjOYAQCgAQHIARPAAQHaAQYIARABGAjaAQYIAhABGBQ&sclient=gws-wiz-serp#lrd=0x94ce59a2cdebc79b:0xf22d5583a67de3f,1,,,,")
# print(driver.title)

driver.get(r"https://www.google.com/maps/place/Hospital+Gl%C3%B3ria+D'Or/@-22.9215267,-43.1870835,16.5z/data=!4m12!1m2!2m1!1shospital+benefic%C3%AAncia+portuguesa!3m8!1s0x997f1ae5a46737:0x7c0efe070848f60c!8m2!3d-22.9220345!4d-43.179922!9m1!1b1!15sCiFob3NwaXRhbCBiZW5lZmljw6puY2lhIHBvcnR1Z3Vlc2FaIyIhaG9zcGl0YWwgYmVuZWZpY8OqbmNpYSBwb3J0dWd1ZXNhkgEIaG9zcGl0YWyaASRDaGREU1VoTk1HOW5TMFZKUTBGblNVUnhNbGxpUTI5blJSQULgAQA!16s%2Fg%2F11fhwwhk6r")



###número de comentarios###

# ncomments = driver.find_element(By.XPATH, "/html/body/span[2]/g-lightbox/div/div[2]/div[3]/span/div/div/div/div[1]/div[3]/div[1]/div").text

# SCROLL_PAUSE_TIME = 2.0
# time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height