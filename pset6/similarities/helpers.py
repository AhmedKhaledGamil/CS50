from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

def __str__(self):
    return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""

    # TODO
    elements = []
    # creating an empty list containting empty lists equal to number of rows
    for i in range(len(a)+1):
        elements.append([])
    #################################################################
    #initializing the [0][0] element as default
    elements[0].append([0,None])
    #################################################################
    # initializing the row values
    for j in range(len(b)):
        elements[0].append([j + 1, Operation.INSERTED])
    #################################################################
    # # initializing the col values
    for k in range(len(a)+1):
        if k == 0:
            continue
        elements[k].append([k, Operation.DELETED])
    #################################################################
    # filling rest of the cells
    for rows in range(len(a)+1):
        if rows == 0:
            continue
        for cols in range(len(b)+1):
            if cols == 0:
                continue
            #print(f"{rows} {cols}")
            deletion_cost = elements[rows - 1][cols][0] + 1
            #print(deletion_cost,end=" ")
            insertion_cost = elements[rows][cols - 1][0] + 1
            #print(insertion_cost,end=" ")
            if a[rows - 1] == b[cols - 1]:
                substitution_cost = elements[rows - 1][cols - 1][0]
                #print(substitution_cost)
            else:
                substitution_cost = elements[rows - 1][cols - 1][0] + 1
                #print(substitution_cost)
            cost = min(deletion_cost,insertion_cost,substitution_cost)
            if cost == deletion_cost:
                elements[rows].append([cost,Operation.DELETED])
            elif cost == insertion_cost:
                elements[rows].append([cost,Operation.INSERTED])
            elif cost == substitution_cost:
                elements[rows].append([cost,Operation.SUBSTITUTED])
    #################################################################
    return elements
