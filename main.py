import get_results
from selenium import webdriver

def main():
    options = webdriver.EdgeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Edge(options=options)
    url = "https://www.megasena.com"

    numbers, prize, date = get_results.get_draw_info(f'{url}/resultados', driver, 2660)
    driver.close()
main()