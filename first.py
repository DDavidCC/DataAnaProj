import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)

np_weight = np.array(weight)

bmi = np_weight / np_height ** 2

print(bmi)

#Baseball Players Height and Weight

np_height_in = np.array(height)

print(np_height_in)

np_height_m = np_height_in * 0.0254

print(np_height_m)