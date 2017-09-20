# ---------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- IMPLEMENTATION OF SOLUTION FOR CAMELS PUZZLE ----------------------------------------------------------------
# ------------------------------- AUTHOR: VIGNESH M. PAGADALA ---------------------------------------------------------------------------------
# --------------------------------FILE: Week1_Camels_Puzzle.py --------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------

import copy
import Week1_BFS_and_DFS as search

def camelSuccessorsf(state):
	st = list(state)
	children = []
	i=0
	while(i<len(st)):
		if(st[i] == ' '):
			index = i
			break
		i += 1
	if index > 0 and st[index - 1] == 'R':
		child = copy.copy(st)
		child[index] = 'R'
		child[index - 1] = ' '
		children.append(tuple(child))

	if index < 8 and st[index + 1] == 'L':
		child = copy.copy(st)
		child[index] = 'L'
		child[index + 1] = ' '
		children.append(tuple(child))
	if index < 8 and st[index + 1] == 'R':
		if index < 7 and st[index + 2] == 'L':
			child = copy.copy(st)
			child[index] = 'L'
			child[index + 2] = ' '
			children.append(tuple(child))
	if index > 0 and st[index - 1] == 'L':
		if index > 1 and st[index - 2] == 'R':
			child = copy.copy(st)
			child[index] = 'R'
			child[index - 2] = ' '
			children.append(tuple(child))
	return children

if __name__ == '__main__':
	camelStartState = ('R','R','R','R', ' ', 'L','L','L','L')
	camelGoalState = ('L', 'L', 'L', 'L', ' ', 'R', 'R', 'R', 'R')
	print("Using BFS:")
	print(search.breadthFirstSearch(camelStartState, camelGoalState, camelSuccessorsf))
	print("Using DFS")
	print(search.depthFirstSearch(camelStartState, camelGoalState, camelSuccessorsf))



