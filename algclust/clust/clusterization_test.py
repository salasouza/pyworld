import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = pd.read_csv('locallake/raw/iris.csv')

x = iris.iloc[:,[0,1,2,3]].values

def numbercluster(rang_min = None, rang_max = None, max_iter = None, n_init = None, random_state = None):
    wcss = []
    for i in range(rang_min, rang_max):
        kmeans = KMeans(n_clusters = i,
            init = 'k-means++',
            max_iter = max_iter,
            n_init = n_init,
            random_state = random_state)

        kmeans.fit(x)
        wcss.append(kmeans.inertia_)
        
    print(wcss)

    plt.plot(range(rang_min,rang_max), wcss)
    plt.title('The elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Within cluster sum of squares (wcss)')
    plt.show()

numbercluster(1,11,300,10,0)
