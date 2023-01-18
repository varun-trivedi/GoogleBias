
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset
# np.random.seed(10)
 
def showbox(data, cities):
    
    print(data)

    fig = plt.figure(figsize =(10, 7))
    
    # Creating axes instance
    ax = fig.add_axes([0.15, 0.1, 0.7, 0.7])
    ax.set_xticklabels(cities)
    
    # Creating plot
    bp = ax.boxplot(data)
    
    # show plot
    plt.show()  