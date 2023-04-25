from flask import Flask, render_template, request
import pandas as pd
import json
from scipy import spatial

def get_suggestions():
    data = pd.read_csv('cuisines.csv')
    result = list(data['Dish Name'].str.capitalize())
    return result

def Cosine_Similarity(Id1, Id2):
    cuisine_df = pd.read_csv('C:/Prerna Tulsiani/COEP/Sem6/Data Science Project/Final Project/Bin_cuisines.csv')
    A = json.loads(cuisine_df['Bin Ingredients'][Id1])
    B = json.loads(cuisine_df['Bin Ingredients'][Id2])
    print(type(A), type(B))
    distance=spatial.distance.cosine(A,B)
    
    return distance, Id2

def get_similar_recipes(dish_name):
    print("Entered Similar Recipes function")
    food=[]
    cuisine_df = pd.read_csv('C:/Prerna Tulsiani/COEP/Sem6/Data Science Project/Final Project/Bin_cuisines.csv')
    found_index = 1

    for iterator in range(len(cuisine_df.index)):
        if(iterator in cuisine_df.index):
            if(cuisine_df['Dish Name'][iterator] == dish_name):
                found_index = iterator

    print(found_index)

    for i in cuisine_df.index:
        food.append(Cosine_Similarity(found_index,i))
    common_ingredients=sorted(food,key=lambda x: x[0])[1:10]
    indexes = []
    for i in range(len(common_ingredients)):
        indexes.append(common_ingredients[i][1])
    print(indexes)

# Flask API

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/search")
def search():
    suggestions = get_suggestions()
    return render_template('search.html',data=json.dumps(suggestions))

@app.route("/similar_recipe",methods=["POST"])
def similar_recipe():
    dish_name = request.form['name']
    print(dish_name)
    get_similar_recipes(dish_name)
    print(dish_name)
    return "hello pratik"

@app.route("/similar")
def similar():
    suggestions = get_suggestions()
    return render_template('similar.html',data=json.dumps(suggestions))

if __name__ == '__main__':
    app.run(debug=True)