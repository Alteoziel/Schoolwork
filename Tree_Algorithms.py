from Algo_and_Struts_06_i_tree_node import TreeNode

def numberOfLeaves(n :TreeNode) -> int:
    if n == None:
        return 0
    if n.is_leaf() == True:
        return 1
    left = numberOfLeaves(n.left_child)
    right = numberOfLeaves(n.right_child)
    return left+right
	
def numberOfNodesWithASingleChild(n :TreeNode)  -> int:
    if n == None:
        return 0
    if n.has_any_child() == False:
        return 0
    if n.left_child == None and n.right_child != None:
        return 1
    if n.right_child == None and n.left_child != None:
        return 1
    left = numberOfNodesWithASingleChild(n.left_child)
    right = numberOfNodesWithASingleChild(n.right_child)
    sum = left+right
    return sum

l = []
def numberOfNodesWithTwoChildren(n :TreeNode)  -> int:
    if n is None:
        return 0

    # Count 1 if THIS node has two children, otherwise 0
    this_node = 1 if (n.left_child is not None and n.right_child is not None) else 0

    # Always recurse on both sides
    left = numberOfNodesWithTwoChildren(n.left_child)
    right = numberOfNodesWithTwoChildren(n.right_child)

    return this_node + left + right

"""
    if n == None:
        return 0
    if n.has_any_child() == False:
        return 0
    if n.has_children() == True:
        return 1
    left = numberOfNodesWithTwoChildren(n.left_child)
    right = numberOfNodesWithTwoChildren(n.right_child)
    sum = left+right
    return sum
"""
	
def numberOfNodesWithEvenDataItems(n :TreeNode)  -> int:
	return -1

def sumOfAllItems(n :TreeNode)  -> int:
	return -1

def printRuntimes():
    #TODO type in the runtimes on these lines: i.e. log(n), n, n log(n), n*n, etc
    print("Big O runtime of numberOfLeaves is: ???")
    print("Big O runtime of numberOfNodesWithOneNonNullChild is: ???")
    print("Big O runtime of numberOfNodesWithTwoNonNullChildren is: ???")
    print("Big O runtime of numberOfNodesWithEvenDataItems is: ???")
    print("Big O runtime of sumOfAllItems is: ???")
		
