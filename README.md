# ContentBasedRRS

## Personal Project

### Name
Content-Based Recipe Recommender System

### Year
2019

### Overview
This project develops a content-based recipe recommender system that suggests similar recipes to users based on a given recipe. It leverages ingredients listed in recipes as metadata and utilizes cosine similarity to quantify the likeness between two recipes.

### Features
- **Ingredient-based Recommendations**: The system uses recipe ingredients as a key metadata component for generating suggestions.
- **Cosine Similarity Calculations**: Employs cosine similarity to accurately measure the similarity between recipes.

### Functionality
Upon receiving a recipe from the user, the system processes the ingredients list and compares it with other recipes in the database using cosine similarity. This approach allows for the identification of recipes with similar ingredient profiles, thereby suggesting alternatives that closely match the user's initial choice.

### How It Works
The core algorithm analyzes the ingredients of the provided recipe and calculates similarity scores against a vast database of recipes. By ranking these scores, the system is able to recommend recipes that share a high degree of similarity in terms of ingredients, offering users personalized options that align with their initial preferences.


![alt-text](https://github.com/filipenovais/ContentBasedRRS/blob/master/outputscreenshot.png)

![alt-text](https://github.com/filipenovais/ContentBasedRRS/blob/master/cossimilarity_plot.png) 

### Cosine Calculation between two Vectors (A and B):
 
![alt-text](https://github.com/filipenovais/ContentBasedRRS/blob/master/cos_calculation.png)

Credit to: https://github.com/codeheroku/Introduction-to-Machine-Learning
Database from: https://github.com/cweber/cookbook/blob/master/recipes.csv
