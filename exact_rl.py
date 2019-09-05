from wumpusWorld import *
import matplotlib.pyplot as plt
import numpy as np

q_values = {((1,1), "up"): 0, ((1,1), "down"): 0, ((1,1), "left"): 0, ((1,1), "right"): 0, ((1,1), "stay"): 0,
            ((1,2), "up"): 0, ((1,2), "down"): 0, ((1,2), "left"): 0, ((1,2), "right"): 0, ((1,2), "stay"): 0,
            ((1,3), "up"): 0, ((1,3), "down"): 0, ((1,3), "left"): 0, ((1,3), "right"): 0, ((1,3), "stay"): 0,
            ((1,4), "up"): 0, ((1,4), "down"): 0, ((1,4), "left"): 0, ((1,4), "right"): 0, ((1,4), "stay"): 0,
            ((2,1), "up"): 0, ((2,1), "down"): 0, ((2,1), "left"): 0, ((2,1), "right"): 0, ((2,1), "stay"): 0,
            ((2,2), "up"): 0, ((2,2), "down"): 0, ((2,2), "left"): 0, ((2,2), "right"): 0, ((2,2), "stay"): 0,
            ((2,3), "up"): 0, ((2,3), "down"): 0, ((2,3), "left"): 0, ((2,3), "right"): 0, ((2,3), "stay"): 0,
            ((2,4), "up"): 0, ((2,4), "down"): 0, ((2,4), "left"): 0, ((2,4), "right"): 0, ((2,4), "stay"): 0,
            ((3,1), "up"): 0, ((3,1), "down"): 0, ((3,1), "left"): 0, ((3,1), "right"): 0, ((3,1), "stay"): 0,
            ((3,2), "up"): 0, ((3,2), "down"): 0, ((3,2), "left"): 0, ((3,2), "right"): 0, ((3,2), "stay"): 0,
            ((3,3), "up"): 0, ((3,3), "down"): 0, ((3,3), "left"): 0, ((3,3), "right"): 0, ((3,3), "stay"): 0,
            ((3,4), "up"): 0, ((3,4), "down"): 0, ((3,4), "left"): 0, ((3,4), "right"): 0, ((3,4), "stay"): 0,
            ((4,1), "up"): 0, ((4,1), "down"): 0, ((4,1), "left"): 0, ((4,1), "right"): 0, ((4,1), "stay"): 0,
            ((4,2), "up"): 0, ((4,2), "down"): 0, ((4,2), "left"): 0, ((4,2), "right"): 0, ((4,2), "stay"): 0,
            ((4,3), "up"): 0, ((4,3), "down"): 0, ((4,3), "left"): 0, ((4,3), "right"): 0, ((4,3), "stay"): 0,
            ((4,4), "up"): 0, ((4,4), "down"): 0, ((4,4), "left"): 0, ((4,4), "right"): 0, ((4,4), "stay"): 1,
            }
temp = 0
gamma = 0.95
iteration = 0
delta_list = []
while True:
	delta = 0
	for state in states:
		for action in actions:
			successors = get_successor(state, action)
			if successors != None:
				temp = q_values[(state, action)]
				q_values[(state, action)] = 0
				for successor in successors:
					q_values_successor = []
					for key in q_values:
						if key[0] == successor:
							q_values_successor.append(q_values[key])
					q_values[(state, action)] = q_values[(state, action)] + transition(state, action, successor)*(reward(state, action, successor) + gamma*max(q_values_successor))
				delta = max(delta, abs(temp-q_values[(state, action)]))
	delta_list.append(delta)
	iteration = iteration + 1
	if delta < 0.01:
		break
print('Q(s0, "up") = %f' %(q_values[(1,1), "up"]))
print('Q(s0, "right") = %f' %q_values[(1,1), "right"])
print('Q(s0, "stay") = %f' %q_values[(1,1), "stay"])
print(delta_list)
# print(q_values)
plt.plot(range(1, iteration + 1), delta_list)
plt.xlabel("Iteration")
plt.ylabel("Delta")
plt.xticks(np.arange(1, iteration+1, 1))
plt.yticks(np.arange(0, delta_list[0]+0.1, 0.1))
plt.show()



