import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

class Support_Vector_Machine:
    
    def __init__(self, visualization = True):
        self.visualization = visualization
        self.colors = {1:'r', -1:'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)

    # Train
    def fit(self, data):
        self.data = data
        # { ||w|| : [w, b] }
        opt_dict = {}

        transforms = [[1,1],
                    [-1,1],
                    [-1,-1],
                    [1,-1]]

        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None

        step_sizes = [self.max_feature_value*0.1,
                    self.max_feature_value*0.01,
                    # point of expense
                    self.max_feature_value*0.001,]

        # extremly expensive
        b_range_multiple = 5
        b_multiple = 5
        latest_optimum = slef.max_feature_value*10

        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            # we can do this because convex
            optimized = False
            while not optimized:
                pass

    def predict(self, features):
        # sign( x.w + b )
        classification = np.sign(np.dot(np.array(features), self.w) + self.b)
        if classification!=0 and self.visualization:
            self.ax.scatter(features[0], features[1], s=200, marker=*, c=self.colors[classification])
        return classification

    def visualize(self):
        [[self.ax.scatter(x[0], x[1], s=100, color = self.colors[i]) for x in data_dict[i]] for i in data_dict]

        # hyperplane = w.x+b
        # v = w.x+b
        # psv = 1
        # nsv = -1
        # dec = 0
        def hyperplane(x,w,b,v):
            return (-w[0]*x-b+v) / w[1]

        datarange = (self.min_feature_value*0.9, self.max_feature_value*1.1)
        hyp_x_min = datarange[0]
        hyp_x_max = datarange[1]


data_dict = {-1:np.array([[1,7],
                [2,8],
                [3,8],]), 
            1:np.array([[5,1],
                [6,-1],
                [7,3],])}