# VARIABLES
# VAR 1 - cuisine_name
cuisine_names = []

# VAR 2 - cuisine_type
cuisine_types = []

# VAR 3 - dish name
cuisine_dishnames = []

# VAR 4 - ingredients list
dish_ingredients = []

# VAR 5 - calories
dish_calories = []

# VAR 6 - fat
dish_fat = []

# VAR 7 - carbs
dish_carbs = []

# VAR 8 - protein
dish_proteins = []

# VAR 9 - dish url
dishes_url = []

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By

# path = 'C://chromedriver.exe'
ser = Service(r"C:\chromedriver.exe")
op = webdriver.ChromeOptions()

# open the browser
browser = webdriver.Chrome(service=ser, options=op)

# load the web page
browser.get('https://cosylab.iiitd.edu.in/recipedb/')
browser.maximize_window()

# enter input in cuisine type field
input_search = browser.find_element_by_id('cities1')

# send the input to the webpage
input_search.send_keys("Chinese")
cuisine_name = "Chinese"
sleep(1)
input_search.send_keys(Keys.ENTER)

products = []

next_page_button = browser.find_element_by_id('nextpage')
next_button_link = next_page_button.find_element_by_tag_name('a')
next_button_link.click()

for i in range(1, 15):
    print('Scraping page', i+1)
    buttons = browser.find_elements_by_xpath("//button[@class='btn-small waves-effect waves-light modal-trigger']")
    for b in buttons:

        # here each dish will be scraped
        # defining vars
        calories = 0
        fat =  0
        carbs = 0
        protein = 0

        b.send_keys(Keys.ENTER)
        nutrition_values_table = browser.find_element_by_id('modalTableBody2')
        nutrition_values = nutrition_values_table.find_elements_by_tag_name('td')
        
        calories = nutrition_values[0].text
        carbs = nutrition_values[1].text
        protein = nutrition_values[2].text
        fat = nutrition_values[3].text
        
        # finding recipe name
        dish_name_div = browser.find_element_by_id('modalRecipeTitle')
        dish_name = dish_name_div.find_element_by_tag_name('a').text
        ing = []
        ing_table = browser.find_element_by_id('modalTableBody')
        ing_list = ing_table.find_elements_by_tag_name('a')
        show_more = browser.find_element(By.ID, 'modalButton')
        dish_url = show_more.get_attribute('href')

        for i in ing_list:
            ing.append(i.text)

        close_button = browser.find_element_by_xpath("//button[@class='modal-close waves-effect btn-small']")
        close_button.send_keys(Keys.ENTER)
        print(dish_name)
        cuisine_names.append(cuisine_name)
        cuisine_dishnames.append(dish_name)
        cuisine_types.append('General')
        dish_ingredients.append(", ".join(ing))
        dish_calories.append(calories)
        dish_carbs.append(carbs)
        dish_fat.append(fat)
        dish_proteins.append(protein)
        dishes_url.append(dish_url)
        sleep(6)

        
    # Going to Next Page

    next_page_button = browser.find_element_by_id('nextpage')
    next_button_link = next_page_button.find_element_by_tag_name('a')
    next_button_link.click()


cuisines = pd.DataFrame({
    'Cuisine' : cuisine_names,
    'Cuisine Type' : cuisine_types,
    'Dish Name' : cuisine_dishnames,
    'Ingredients' : dish_ingredients,
    'Calories' : dish_calories,
    'Carbs' : dish_carbs,
    'Fat' : dish_fat,
    'Protein' : dish_proteins,
    'Recipe_url' : dishes_url,
})

cuisines.to_csv('Chinese.csv')
        