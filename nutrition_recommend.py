import config 
import pandas as pd
from sklearn.preprocessing import normalize
from scipy.spatial.distance import cosine, euclidean, hamming

def cosine_calculator(recipe_id):
    df_normalized = pd.read_csv(config.NUTRITION_NORMALISED)
    distance = []
    for x in range(len(df_normalized.index)):
        if(x in df_normalized.index and x!=recipe_id):
            distance.append(cosine(df_normalized.loc[recipe_id], df_normalized.loc[x]))
        if(x==recipe_id):
            distance.append(0)
    return distance

def hamming_calulator(recipe_id):
    df_normalized = pd.read_csv(config.NUTRITION_NORMALISED)
    distance = []
    for x in range(len(df_normalized.index)):
        if(x in df_normalized.index and x!=recipe_id):
            distance.append(hamming(df_normalized.loc[recipe_id], df_normalized.loc[x]))
        if(x==recipe_id):
            distance.append(0)
    return distance

def euclidean_calculator(recipe_id):
    df_normalized = pd.read_csv(config.NUTRITION_NORMALISED)
    distance = []
    for x in range(len(df_normalized.index)):
        if(x in df_normalized.index and x!=recipe_id):
            distance.append(euclidean(df_normalized.loc[recipe_id], df_normalized.loc[x]))
        if(x==recipe_id):
            distance.append(0)
    return distance


def nutrition_recommender(recipe_id):

    # cosine_df = pd.DataFrame(df_normalized)
    # cosine_df['distance'] = cosine_calculator(recipe_id)
    
    # hamming_df = pd.DataFrame(df_normalized)
    # hamming_df['distance'] = hamming_calulator(recipe_id)

    euclidean_df = pd.read_csv(config.NUTRITION_NORMALISED)
    print(euclidean_df.loc[5221])
    euclidean_df['distance'] = euclidean_calculator(recipe_id)
    
    # Top2Recommendation_cosine = cosine_df.sort_values(["distance"]).tail(5).sort_values(by=['distance'])
    # Top2Recommendation_euclidean = hamming_df.sort_values(["distance"]).tail(5).sort_values(by=['distance'])
    Top2Recommendation_hamming = euclidean_df.sort_values(["distance"]).tail(10).sort_values(by=['distance'])
    # print(Top2Recommendation_cosine, Top2Recommendation_euclidean, Top2Recommendation_hamming)
    # print(list(Top2Recommendation_hamming.index))
    return list(Top2Recommendation_hamming.index)
    #print(allRecipes["distance"])
    #TopNRecommendation = allRecipes.sort_values(["distance"]).head(N).sort_values(by=['distance'])
    

def Nutrition_SYS(recipe):
    data = pd.read_csv(config.RECIPES_PATH)
    df = pd.DataFrame(data)
    original_df = pd.DataFrame(data)
    df = df.drop(['Cuisine', 'Dish Name', 'Ingredients', 'Recipe_url'], axis=1)
    # drop url also

    # apply normalisation
    df_nutrients_normalised = pd.DataFrame(normalize(df, axis=0))
    df_nutrients_normalised.index = df.index
    print(df_nutrients_normalised.head())
    df_nutrients_normalised.to_csv('Nutrition_Normalized.csv', index=False)

#Nutrition_SYS("hi")
def N_SYS(recipe_id):
    l = nutrition_recommender(recipe_id)
    return l