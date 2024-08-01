import json
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time

service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

try:
    driver.get("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")

    time.sleep(4)

    title_elements = driver.find_elements(By.CSS_SELECTOR, "a h3.ipc-title__text")
    titles = [element.text for element in title_elements]
    
    with open("titulos_imdb.json", "w", encoding="utf-8") as file:
        json.dump(titles, file, ensure_ascii=False, indent=4)
        
finally:
    driver.quit()