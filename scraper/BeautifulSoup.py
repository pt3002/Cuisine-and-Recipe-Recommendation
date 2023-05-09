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

from bs4 import BeautifulSoup
import requests
import pandas as pd

# website url
website_url = 'https://www.allrecipes.com/cuisine-a-z-6740455'
website_html_text = requests.get(website_url).text
website_soup = BeautifulSoup(website_html_text, 'lxml')

# list of cuisines variable
cuisines_list = website_soup.find_all('li', class_ = 'comp link-list__item')

# running through all the cuisines one by one
for c in range(1, 3):
    
    cuisine_particular = cuisines_list[c]
    # Variable 1
    cuisine_name = cuisine_particular.find('a').text.replace('\n', '')
    print(cuisine_name, len(cuisine_dishnames))

    cuisine_url = cuisine_particular.find('a')['href']
    cuisine_html_text = requests.get(cuisine_url).text
    cuisine_soup = BeautifulSoup(cuisine_html_text, 'lxml')

    # finding types of dishes from a particular cuisine
    cuisinetype_list_ul = cuisine_soup.find('ul', id = 'taxonomy-nodes__list_1-0')

    if(cuisinetype_list_ul):

        cuisinetype_list_li = cuisinetype_list_ul.find_all('li', class_ = 'comp taxonomy-nodes__item mntl-block')

        if(cuisinetype_list_li):

            for cuisine_type_element in cuisinetype_list_li:
                
                # Variable 2
                cuisine_type_name = cuisine_type_element.find('a').text
                print(cuisine_type_name)

                cuisine_particular_type_url = cuisine_type_element.find('a')['href']
                c_type_html_text = requests.get(cuisine_particular_type_url).text
                c_type_soup = BeautifulSoup(c_type_html_text, 'lxml')
                c_type_total = c_type_soup.find_all('span', class_ = 'card__title-text')
                c_type_id_parser = "mntl-card-list-items_"

                possible_ids = []

                for i in range(1, len(c_type_total) + 1):

                    id = c_type_id_parser + str(i) + "-0"
                    possible_ids.append(id)

                    for j in range(1, len(c_type_total) + 1):
                        possible_ids.append(id + "-" + str(j))

                for item_id in possible_ids:

                    dish = c_type_soup.find('a', id = item_id)

                    if(dish):

                        # Variable 3
                        dish_name = dish.find('span', class_ = 'card__title-text').text
                        dish_url = dish['href']
                        dish_html_text = requests.get(dish_url).text
                        dish_soup = BeautifulSoup(dish_html_text, 'lxml')

                        x = dish_soup.find('ul', class_ = 'mntl-structured-ingredients__list')

                        # Variable 4
                        ing = []

                        if(x):

                            y = x.find_all('span', attrs = {"data-ingredient-name":"true"})

                            for z in y:
                                ing.append(z.text)

                        # Variable 5, 6, 7, 8
                        nutrition = dish_soup.find_all('tr', class_ = 'mntl-nutrition-facts-summary__table-row')

                        calories = 0
                        fat =  0
                        carbs = 0
                        protein = 0

                        for n in nutrition:
                            n_type = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dogg')
                            if(n_type):
                                if(n_type.text == 'Calories'):
                                    n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                                    calories = n_q.text

                                elif(n_type.text == 'Fat'):
                                    n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                                    fat = n_q.text

                                elif(n_type.text == 'Carbs'):
                                    n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                                    carbs = n_q.text

                                elif(n_type.text == 'Protein'):
                                    n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                                    protein = n_q.text

                            # type 2
                            n_type = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog')
                            if(n_type):
                                if(n_type.text == 'Calories'):
                                    n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                                    calories = n_q.text

                                elif(n_type.text == 'Fat'):
                                    n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                                    fat = n_q.text

                                elif(n_type.text == 'Carbs'):
                                    n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                                    carbs = n_q.text

                                elif(n_type.text == 'Protein'):
                                    n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                                    protein = n_q.text

                        cuisine_names.append(cuisine_name)
                        cuisine_types.append('General')
                        cuisine_dishnames.append(dish_name)
                        dish_ingredients.append(", ".join(ing))
                        dish_calories.append(calories)
                        dish_carbs.append(carbs)
                        dish_fat.append(fat)
                        dish_proteins.append(protein)
                        dishes_url.append(dish_url)

    else:

        total_items = cuisine_soup.find_all('span', class_ = 'card__title-text')

        possible_ids = []

        id_parser = "mntl-card-list-items_"

        for i in range(1, len(total_items) + 1):

            id = id_parser + str(i) + "-0"
            possible_ids.append(id)

            for j in range(1, len(total_items) + 1):
                possible_ids.append(id + "-" + str(j))

        for item_id in possible_ids:

            dish = cuisine_soup.find('a', id = item_id)

            if(dish):

                # Variable 3
                dish_name = dish.find('span', class_ = 'card__title-text').text
                dish_url = dish['href']
                dish_html_text = requests.get(dish_url).text
                dish_soup = BeautifulSoup(dish_html_text, 'lxml')

                x = dish_soup.find('ul', class_ = 'mntl-structured-ingredients__list')

                # Variable 4
                ing = []

                if(x):

                    y = x.find_all('span', attrs = {"data-ingredient-name":"true"})

                    for z in y:
                        ing.append(z.text)

                # Variable 5, 6, 7, 8
                nutrition = dish_soup.find_all('tr', class_ = 'mntl-nutrition-facts-summary__table-row')

                calories = 0
                fat =  0
                carbs = 0
                protein = 0

                for n in nutrition:
                    n_type = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dogg')
                    if(n_type):
                        if(n_type.text == 'Calories'):
                            n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                            calories = n_q.text

                        elif(n_type.text == 'Fat'):
                            n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                            fat = n_q.text

                        elif(n_type.text == 'Carbs'):
                            n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                            carbs = n_q.text

                        elif(n_type.text == 'Protein'):
                            n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                            protein = n_q.text

                    # type 2
                    n_type = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog')
                    if(n_type):
                        if(n_type.text == 'Calories'):
                            n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                            calories = n_q.text

                        elif(n_type.text == 'Fat'):
                            n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                            fat = n_q.text

                        elif(n_type.text == 'Carbs'):
                            n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                            carbs = n_q.text

                        elif(n_type.text == 'Protein'):
                            n_q = n.find('td', class_ = 'mntl-nutrition-facts-summary__table-cell type--dog-bold')
                            protein = n_q.text
                
                cuisine_names.append(cuisine_name)
                cuisine_types.append('General')
                cuisine_dishnames.append(dish_name)
                dish_ingredients.append(", ".join(ing))
                dish_calories.append(calories)
                dish_carbs.append(carbs)
                dish_fat.append(fat)
                dish_proteins.append(protein)
                dishes_url.append(dish_url)

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

cuisines.to_csv('cuisines_1.csv')