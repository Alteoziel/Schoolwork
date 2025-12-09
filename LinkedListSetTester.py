from LinkedList import LinkedList
from Node import Node
from LinkedListSet import LinkedListSet


with open("Partial_Book.txt") as f:
    book = f.read()
    words = book.split()

setA = LinkedListSet()
setB = LinkedListSet()
setC = LinkedListSet()

for i in range(0,len(words)):
    if len(words[i]) <= 5:
        setA.add(words[i])
    if len(words[i]) >= 5:
           setB.add(words[i])
    if len(words[i]) == 5:
        setC.add(words[i])

print("Set A size: ",setA.size())
print("Set B size: ",setB.size())
print("Set C size: ",setC.size())

Link = LinkedListSet()

UnionAB = Link.union(setA,setB)
UnionAC = Link.union(setA,setC)
UnionBC = Link.union(setB,setC)
print("UnionAB ",UnionAB)
print("UnionAC ",UnionAC)
print("UnionBC ",UnionBC)


IntersectAB = Link.intersection(setA,setB)
IntersectAC = Link.intersection(setA,setC)
IntersectBC = Link.intersection(setB,setC)
print("IntersectAB ",IntersectAB)
print("IntersectAC ",IntersectAC)
print("IntersectBC ",IntersectBC)

DifferenceAB = Link.difference(setA,setB)
DifferenceAC = Link.difference(setA,setC)
DifferenceBC = Link.difference(setB,setC)
DifferenceBA = Link.difference(setB,setA)
DifferenceCA = Link.difference(setC,setA)
DifferenceCB = Link.difference(setC,setB)
print("DifferenceAB ",DifferenceAB)
print("DifferenceAC ",DifferenceAC)
print("DifferenceBC ",DifferenceBC)
print("DifferenceBA ",DifferenceBA)
print("DifferenceCA ",DifferenceCA)
print("DifferenceCB ",DifferenceCB)


print("UnionAB Size:",UnionAB.size())
print("UnionAC Size:",UnionAC.size())
print("UnionBC Size:",UnionBC.size())

print("IntersectAB Size:",IntersectAB.size())
print("IntersectAC Size:",IntersectAC.size())
print("IntersectBC Size:",IntersectBC.size())

print("DifferenceAB Size:",DifferenceAB.size())
print("DifferenceAC Size:",DifferenceAC.size())
print("DifferenceBC Size:",DifferenceBC.size())
print("DifferenceBA Size:",DifferenceBA.size())
print("DifferenceCA Size:",DifferenceCA.size())
print("DifferenceCB Size:",DifferenceCB.size())
