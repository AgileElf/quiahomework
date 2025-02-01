from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url = "https://www.quia.com/web"
driver.get(url)
username = 'acowl139'#input('Username: ')
password = '46party'#input('password: ')
lesson = 'U5L1'
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.NAME, "quiaFormSubmit").click()
driver.find_element(By.XPATH, '//*[@id="qwbody"]/table/tbody/tr/td/form/table[1]/tbody/tr[5]/td[2]/a').click()
for x in range(1, len(driver.find_elements(By.CLASS_NAME, 'qia12'))):
    lesson_text = driver.find_element(By.XPATH, '//*[@id="quizActivity"]/tbody/tr[' + str(x) + ']/td/table/tbody/tr/td[2]/a').text
    if lesson in lesson_text:
        driver.find_element(By.XPATH, '//*[@id="quizActivity"]/tbody/tr[' + str(x) + ']/td/table/tbody/tr/td[2]/a/font/b').click()
        break

driver.find_element(By.NAME, "tag_quiz_username").send_keys(username)
driver.find_element(By.NAME, "tag_quiz_password").send_keys(password)
driver.find_element(By.NAME, "tagStartQuiz").click()

word_dict = {
    "sugar": "el azúcar",
    "to taste": "probar",
    "carrot": "la zanahoria",
    "to have breakfast": "desayunar",
    "to have dinner": "cenar",
    "lettuce": "la lechuga",
    "hot (temperature)": "caliente",
    "afternoon snack": "la merienda",
    "strawberry": "la fresa",
    "flavor": "el sabor",
    "salt": "la sal",
    "mustard": "la mostaza",
    "vinegar": "el vinagre",
    "fresh": "fresco",
    "spicy; hot": "picante",
    "to mix": "mezclar",
    "pepper": "la pimienta",
    "onion": "la cebolla",
    "recipe": "la recenta",
    "delicious": "delicioso",
    "mayonnaise": "la mayonesa",
    "oil": "el aceite",
    "ingredient": "el ingrediente",
    "salty": "salado",
    "garlic": "el ajo",
    "spinach": "las espinacas",
    "sour": "agrio",
    "supermarket": "el supermercado",
    "to fry": "freír",
    "sweet": "dulce",
    "how disgusting!": "¡qué asco!",
    "to beat": "batir",
    "tasty": "sabroso",
    "potato omelet": "la torilla de patatas",
    "lemon": "el limón",
    "to add": "añadir",
    "to boil": "hervir"
}

for x in range(1,38):
    first = '//*[@id="drawAllQuestionsTbl"]/tbody/tr['
    second = ']/td/ol/li'
    question = f'{first}{x}{second}'
    word = driver.find_element(By.XPATH, question).text.strip().lower()
    new_word = word_dict[word]
    driver.find_element(By.XPATH, question + "/input").send_keys(new_word)


driver.find_element(By.NAME, 'tag_submit_all_at_once').click()

time.sleep(2)