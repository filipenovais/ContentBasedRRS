from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from matplotlib import pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)
import numpy as np

text = ["Home Sweet Home", "Sweet Sweet Home"]

# count number of times each word appears in each string of the list
cv = CountVectorizer()

count_matrix = cv.fit_transform(text)
# first sentence - Home 2x Sweet 1x *** second sentence - Home 1x Sweet 2x
matrix = count_matrix.toarray()
print(matrix)

similarity_scores = cosine_similarity(count_matrix)
#the first sentence is similar to the first sentence by 1 and similar to the second sentence by 0.8
#the second sentence is similar to the first sentence by 0.8 and similar to the second sentence by 1
print(similarity_scores)

# plot vectors
if 1:
    origin = [0], [0]

    plt.quiver(*origin, matrix[:, 0], matrix[:, 1], color=['r','b'], angles='xy', scale_units='xy', scale=1)
    plt.plot(matrix[0][0], matrix[0][1], 'ro', label = 'Home Sweet Home')
    plt.plot(matrix[1][0], matrix[1][1], 'bo', label = 'Sweet Sweet Home')

    plt.legend(loc='lower right')
    plt.xlim(-1, 3)
    plt.ylim(-1, 3)
    plt.yticks(np.arange(0, 3, step=1))
    plt.xticks(np.arange(0, 3, step=1))
    plt.xlabel('Home', fontsize=14)
    plt.ylabel('Sweet', fontsize=14)
    plt.title('Cosine Similarity', fontsize=18)
    plt.savefig('CosineSimilarity.png')
    plt.show()