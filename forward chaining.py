import heapq
import copy
import math

import sys


class Node:
    def __init__(self, f, g, h, value, parent):
        self.f = f
        self.g = g
        self.h = h
        self.value = value

        self.parent = parent
        self.actions = []

    def __lt__(self, other):
        return self.f < other.f

    def add_action(self, action):
        self.actions.append(action)

    def get_actions(self):
        return self.actions[0]

def take_action(knowledge_base, action):
    """
    Given a 2D array containing a blank at position pos_x, pos_y, take action.
    This function does not check if the action is valid.
    """
    if action == 'Rule1':
        # implement rule 1
        knowledge_base.pop()
        return 1
    elif action == 'Rule2':
        return 2


def solution(knowledge_base, node):
    # check if solution found

    if node.value in knowledge_base:
        #check if node.value is conclusion -> we will have to mark conclusions in KB somehow
        solution_bool = True

    if solution_bool:
        steps = reconstruct_map(node)
        print(steps)
        return exit(0)


def child_in_explored_nodes(explored, child):
    for explored_node in explored:
        same = True
        for row in range(PUZZLE_WIDTH):
            for col in range(PUZZLE_WIDTH):
                if explored_node[row][col] != child[row][col]:
                    same = False
        if same == True:
            return True
    return False

# TODO adapt this to the knwoledge base
def add_to_frontier(explored, frontier, child):
    should_replace_frontier = False
    is_frontiered = False
    for node_in_frontier in frontier:
        if compare_matrices(node_in_frontier[1].matrix, child.matrix):
            is_frontiered = True

        if compare_matrices(node_in_frontier[1].matrix, child.matrix) and node_in_frontier[1].g > child.g:
            should_replace_frontier = True
            frontier.remove(node_in_frontier)
            heapq.heappush(frontier, (child.f, child))

    # if true, add child node in the frontier
    if child_in_explored_nodes(explored,
                               child.matrix) == False and is_frontiered == False and should_replace_frontier == False:
        heapq.heappush(frontier, (child.f, child))



def bayesian(knowledge_base, node):
    # implement bayesian algorithm
    return

# this recontrusts all the steps taken to find the conclusion, so we can print the decision tree at the end
def reconstruct_map(node):
    all_actions = []

    action = node.actions[0]
    all_actions.append(action)
    node = node.parent
    while node.parent != 'None':
        action = node.actions[0]
        all_actions.append(action)
        node = node.parent

    all_actions.reverse()
    steps = len(all_actions)
    return steps


def forward_chaining():
    with open('knowledge_base.txt') as f:
        knowledge_base = f.readlines()
    input_terminal = sys.stdin.readlines()

    actions = ['Rule1', 'Rule2']

    frontier = []
    explored = []

    node = Node(0, 0, 0, '_', input_terminal, 'None')
    heapq.heappush(frontier, (node.f, node))

    count = 0

    while len(frontier) != 0:
        node = heapq.heappop(frontier)[1]
        explored.append(node.matrix)

        solution(knowledge_base, node)

        for action in actions:
            if action == 'Rule1':
                g = node.g + 1
                #pop form Kb the value for the variable node
                value = knowledge_base.pop(node)

                take_action(knowledge_base, 'Rule1')
                h = bayesian()
                f = g + h
                child = Node(f, g, h, value, node)
                child.add_action('Rule1')

                # check explored and frontier with new child
                add_to_frontier(explored, frontier, child)




if __name__ == '__main__':
    forward_chaining()
