def get_last_draw(url, driver):
    driver.get(url)
    last_draw = driver.find_element("class name", "draw-number").text
    last_draw = last_draw.split(sep=" ")[-1]
    return last_draw


def get_draw_info(url, driver, draw):
    driver.get(f'{url}/{draw}')
    prize = driver.find_element("class name", "jackpot").text
    numbers = driver.find_elements("class name", "ball")
    date = driver.find_element("xpath", "/html/body/div[2]/main/div/h1/span").text

    prize = prize.replace(".","")
    prize = prize.replace(",",".")
    prize = prize.split(sep=" ")[-1]

    numbers_list = [int(element.text) for element in numbers]
    return numbers_list, prize, date