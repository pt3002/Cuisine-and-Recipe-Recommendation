import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle 
import config

# load in parsed recipe dataset 
df_recipes = pd.read_csv(config.RECIPES_PATH)

# convert the data type of an array to Unicode
df_recipes['Ingredients'] = df_recipes.Ingredients.values.astype('U')

# TF-IDF feature extractor 
tfidf = TfidfVectorizer()
tfidf.fit(df_recipes['Ingredients'])
tfidf_recipe = tfidf.transform(df_recipes['Ingredients'])

# save the tfidf model and encodings 
with open(config.TFIDF_MODEL_PATH, "wb") as f:
    pickle.dump(tfidf, f)

with open(config.TFIDF_ENCODING_PATH, "wb") as f:
    pickle.dump(tfidf_recipe, f)