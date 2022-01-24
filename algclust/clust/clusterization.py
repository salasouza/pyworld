import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

iris = pd.read_csv('locallake/raw/iris.csv')

x = iris.iloc[:,[0,1,2,3]].values

def clusterization():

    kmeans = KMeans(n_clusters = 3,
                        init = 'k-means++',
                        max_iter = 300,
                        n_init = 10,
                        random_state = 0)

    y_kmeans = kmeans.fit_predict(x)

    print('Predict \n\n', y_kmeans)

    data_clusters = iris.copy()

    data_clusters['Clusters'] = y_kmeans

    print('\n Clusters centers \n\n',kmeans.cluster_centers_)

    print('\n Data with clusters \n\n', data_clusters.head(3))

    plt.scatter(kmeans.cluster_centers_[:,0],
            kmeans.cluster_centers_[:,1],
            s = 100,
            c = 'black',
            label = 'Centroids')
    plt.legend()
    plt.show()

clusterization()
