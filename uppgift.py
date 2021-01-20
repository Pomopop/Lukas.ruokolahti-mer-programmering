import numpy as np

#def människor(z):
    #befolkning = 11/(1+3.4 * np.exp(-0.03 * z))
    #return befolkning

#print(f"{människor(0)} miljader")

#import numpy as np


def människor(z):
    befolkning = 11/(1+3.4 * np.exp(-0.03 * z))
    return befolkning

print(f"{människor(100000000)} miljader")

