import csv
import os
from selenium import webdriver

def set_driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Edge(options=options)
    url="https://www.megasena.com"
    return url, driver

def get_last_draw(url, driver):
    driver.get(url)
    last_draw = driver.find_element("class name", "draw-number").text
    last_draw = last_draw.split(sep=" ")[-1]
    return int(last_draw)

def get_draw_info(url, driver, draw):
    driver.get(f'{url}/{draw}')
    prize = driver.find_element("xpath","/html/body/div[2]/main/div/div[1]/div[1]/div[1]/div[2]/div/div[2]").text
    date = driver.find_element("xpath", "/html/body/div[2]/main/div/h1/span").text
    numbers = driver.find_elements("class name", "ball")

    prize = prize.replace(".","")
    prize = prize.replace(",",".")
    prize = float(prize.split(sep=" ")[-1])

    numbers_list = [int(element.text) for element in numbers]
    return numbers_list, prize, date

def get_results(url, driver, start=1):
    header = ["concurso","dia","mes","ano","premio","numeros"]
    create_csv_file_if_not_exists('resultados.csv', header)

    last_draw = get_last_draw(url, driver)
    for draw in range(start, last_draw + 1):
        numbers, prize, date = get_draw_info(f'{url}/resultados', driver, draw)
        day, month, year = map(lambda x: int(x), date.split(sep="/"))
        to_csv([draw, day, month, year, prize, numbers])

def update_results(url, driver, file='resultados.csv'):
    last_draw = last_entry(file)
    get_results(url, driver, last_draw+1)

def create_csv_file_if_not_exists(file, header):
    if not os.path.exists(file):
        with open(file, "w+", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)

def to_csv(info):
    with open("resultados.csv", 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(info)

def last_entry(csv_file):
    with open(csv_file, 'r') as file:
        last_line = file.readlines()[-1].split(sep=',')
    return int(last_line[0])

def str_to_list_of_int(str):
    return [int(x) for x in str.replace("[","").replace("]","").replace('\n',"").split(sep=",")]