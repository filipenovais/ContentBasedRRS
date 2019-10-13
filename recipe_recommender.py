import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sys import exit

def combine_features(row):
    try:
        newrow = ''
        for feature in features:
            newrow += row[feature] + ' '
        return newrow[:-1]
    except:
        print("****************ERROR****************")
        print(row)
        exit()

def get_title_from_index(index):
	return df[df.index == index]["Title"].values[0]

def get_index_from_title(title):
    try:
	    return df[df.Title == title].index[0]
    except:
        print("****************ERROR****************")
        print("No recipe named: " + title)
        exit()

# Read CSV File
df = pd.read_csv( 'recipes.csv', index_col=None, header=0, engine='python' )
#print(df.head().to_string())

# Select Features and remove NA values
features = []
for i in range(1,20):
    features.append('Ingredient'+str(i))
    df[features[i - 1]]= df[features[i-1]].fillna('')

# Combine all features in one column
df["combined_features"] = df.apply(combine_features, axis=1)
#print(df["combined_features"].head())

# Make matrix that counts the number of times each word appears in each string of each row
cv = CountVectorizer()
count_matrix =  cv.fit_transform(df["combined_features"])

# Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)

# Get index of recipe from its title
selected_recipe = "Chocolate Cake"
recipe_index = get_index_from_title(selected_recipe)

# Get list of tuples from cosine_sim matrix corresponding to the chosen recipe row
similar_recipes = list(enumerate(cosine_sim[recipe_index]))
#print(similar_recipes)

# Get a list of similar recipes in descending order of similarity score
sorted_similar_recipes = sorted(similar_recipes, key=lambda x:x[1], reverse=True)
#print(sorted_similar_recipes)

# Print titles of first 10 recipes similar to the chosen recipe
print('Recipes similar to: ' + get_title_from_index(sorted_similar_recipes[0][0]) + '\n')
i = 0
for recipe in sorted_similar_recipes:
    if i < 11 and i > 0:
        print(get_title_from_index(recipe[0]))
    elif i == 0:
        pass
    else:
        break
    i += 1
