from selenium import webdriver

options = webdriver.EdgeOptions()
options.add_argument("--headless=new")
driver = webdriver.Edge(options=options)

url = "https://www.megasena.com/"

driver.get(url)
last_result = driver.find_element("class name", "draw-number").text
driver.close()

last_result = last_result.split(sep=" ")[1]
print(last_result)