import numpy as np #numpy imported as np

np.random.seed(123)

#starting steps
steps = 50

#dice
dice = np.random.randint(1, 7)

if dice <= 2:
    steps = steps - 1
elif dice <= 5:
    steps = steps + 1
else:
    steps = steps + np.random.randint(1, 7)

print("turn: ", dice) 
print("steps: ", steps)


#Random Walk

random_walk = [0]

for x in range(100):
    steps = random_walk[-1]
    dice = np.random.randint(1, 7)
    if dice <= 2:
        steps = max(0, steps - 1)
    elif dice <= 5:
        steps = max(0, steps + 1)
    else:
        steps = max(0, steps + np.random.randint(1, 7))
    random_walk.append(steps)

print("Random Walk:", random_walk)

import matplotlib.pyplot as plt #matplotlib imported as plt


all_walks = []

for i in range(5):
    random_walk = [0]
    for x in range(100):
        steps = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            steps = max(0, steps - 1)
        elif dice <= 5:
            steps = steps + 1
        else:
            steps = steps + np.random.randint(1, 7)

        #Clumsiness
        if np.random.rand() < 0.005:
            steps = 0

        random_walk.append(steps)
    all_walks.append(random_walk)
    

# Convert the list of walks to a NumPy array for easier manipulation
np_aw = np.array(all_walks)

# Transpose the array to have each walk as a row
np_aw_t  = np.transpose(np_aw)

# Plotting the transposed array
plt.plot(np_aw_t)
plt.title("All Random Walks")
plt.xlabel("Steps")
plt.ylabel("Position")
plt.show()

# Transpose the array to have each walk as a row
np_aw_t = np.transpose(np.array(all_walks))

#Last row selection
ends = np_aw_t[-1, :]

# Histogram of the last positions
plt.hist(ends)
plt.title("Histogram of Last Positions")
plt.xlabel("Final Position")
plt.ylabel("Frequency")
plt.show()

