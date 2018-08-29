import numpy as np
import pickle

def ELU(x):
    if x >= 0:
        return x
    else:
        return np.exp(x) - 1

vELU = np.vectorize(ELU)

class Layer:
    
    def __init__(self, width, widthPreviousLayer):
        self.weight = np.random.rand(width, widthPreviousLayer)/50
        self.bias = np.zeros(width)
        
    def feed(self, x):
        return vELU(np.dot(self.weight, x) + self.bias)
 
class Network:
    
    def __init__(self, nLayers, widthLayer, sizeInput, sizeOutput):
        self.layers = [Layer(widthLayer, sizeInput)]
        for _ in range(nLayers - 2):
            self.layers.append(Layer(widthLayer, widthLayer))
        self.layers.append(Layer(sizeOutput, widthLayer))
        
    def feed(self, x):
        a = x
        for l in self.layers:
            a = l.feed(a)
        return a
    
    def saveAs(self, filename):
        with open(filename + '.pkl', 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
        #to open: 
        #    with open('filename.pkl', 'rb') as input:
        #    network = pickle.load(input)

#n = Network(10, 100, 81, 1)
#x = np.random.rand(81)
#print(n.feed(x))
#
#n.saveAs("oui")
#
#del n
#
#with open('oui.pkl', 'rb') as input:
#    n = pickle.load(input)
#    
#print(n.feed(x))