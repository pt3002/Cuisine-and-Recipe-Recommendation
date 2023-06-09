from flask import Flask, render_template, request
import pandas as pd
import json
from scipy import spatial
import config
import recommend_recipe
import nutrition_recommend
from scipy.spatial.distance import cosine

def get_suggestions():
    data = pd.read_csv(config.RECIPES_PATH)
    result = list(data['Dish Name'])
    return result


def Cosine_Similarity(Id1, Id2):
    cuisine_df = pd.read_csv(
        'C:/Prerna Tulsiani/COEP/Sem6/Data Science Project/Final Project/Bin_cuisines.csv')
    A = json.loads(cuisine_df['Bin Ingredients'][Id1])
    B = json.loads(cuisine_df['Bin Ingredients'][Id2])
    distance = spatial.distance.cosine(A, B)

    return distance, Id2


def get_similar_recipes(dish_name):
    print("Entered Similar Recipes function")
    food = []
    cuisine_df = pd.read_csv(config.RECIPES_PATH)
    found_index = 0

    for iterator in range(len(cuisine_df.index)):
        if (iterator in cuisine_df.index):
            if (cuisine_df['Dish Name'][iterator] == dish_name):
                found_index = iterator

    print(found_index)

    for i in cuisine_df.index:
        #food.append(Cosine_Similarity(found_index, i))
        food.append(cosine(cuisine_df.loc[found_index], cuisine_df.loc[i]))

    print(food)

    common_ingredients = sorted(food, key=lambda x: x[0])[1:10]
    indexes = []
    for i in range(len(common_ingredients)):
        indexes.append(common_ingredients[i][1])

    print(indexes)
    return indexes


def get_full_information_recipe(dishes_array):
    cuisine_df = pd.read_csv(config.RECIPES_PATH)
    cuisine_dict = []
    print(dishes_array)
    for iterator in cuisine_df.index:
        if (cuisine_df['Dish Name'][iterator] in dishes_array):
            cuisine_dict.append([cuisine_df['Cuisine'][iterator], cuisine_df['Dish Name'][iterator],
                                cuisine_df['Ingredients'][iterator], cuisine_df['Calories'][iterator], cuisine_df['Recipe_url'][iterator]])

    return cuisine_dict

def get_full_information_recipe_nut(recipe_ids):
    cuisine_df = pd.read_csv(config.RECIPES_PATH)
    cuisine_dict = []
    for iterator in cuisine_df.index:
        if (iterator in recipe_ids):
            cuisine_dict.append([cuisine_df['Cuisine'][iterator], cuisine_df['Dish Name'][iterator],
                                cuisine_df['Ingredients'][iterator], cuisine_df['Calories'][iterator], cuisine_df['Recipe_url'][iterator]])

    return cuisine_dict

# Flask API


ing_list_recipe = []
ing_count_flag = 0

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/search")
def search():
    suggestions = get_suggestions()
    return render_template('search.html', data=json.dumps(suggestions))

@app.route("/search_info", methods=["POST"])
def search_info():
    recipe = request.form['recipe']
    info_recipe = get_full_information_recipe([recipe])
    return info_recipe


@app.route("/similar_recipe", methods=["POST"])
def similar_recipe():
    return "hello pratik"


@app.route("/similar")
def similar():
    suggestions = get_suggestions()
    return render_template('similar.html', data=json.dumps(suggestions))

@app.route("/nutri", methods=["POST"])
def nutri():
    recipe_id = request.form['name']
    cuisine_df = pd.read_csv(config.RECIPES_PATH)
    found_index = 0

    for iterator in range(len(cuisine_df.index)):
        if (iterator in cuisine_df.index):
            if (cuisine_df['Dish Name'][iterator] == recipe_id):
                found_index = iterator

    ids = nutrition_recommend.N_SYS(found_index)
    c_dict = get_full_information_recipe_nut(ids)
    return c_dict

@app.route("/search_recipe_ingredients", methods=["POST"])
def search_recipe_ingredients():
    ing_list = request.form['ing_array']
    ing_list_recipe = ing_list.split("+")
    ing_list_recipe = " ".join(ing_list_recipe)
    dishes_array = recommend_recipe.RecSys(ing_list_recipe)
    recommended_recipes = get_full_information_recipe(dishes_array)
    return recommended_recipes


@app.route("/recipe_recommend")
def recipe_recommend():
    return render_template('recipe_recommend.html')

@app.route("/cuisine_classify")
def cuisine_classify():
    return render_template('cuisine.html')


if __name__ == '__main__':
    app.run(debug=True)
