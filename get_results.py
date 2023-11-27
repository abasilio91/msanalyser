def get_last_draw(url, driver):
    driver.get(url)
    last_draw = driver.find_element("class name", "draw-number").text
    last_draw = last_draw.split(sep=" ")[-1]
    return last_draw


def get_draw_results(url, driver, draw):
    driver.get(f'{url}/{draw}')
    prize = driver.find_element("class name", "jackpot").text
    numbers = driver.find_elements("class name", "ball")
    prize = prize.replace(".","")
    prize = prize.replace(",",".")
    numbers_list = [int(element.text) for element in numbers]

    prize = prize.split(sep=" ")[-1]
    return numbers_list, prize