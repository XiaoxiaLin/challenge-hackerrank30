class Difference:
    def __init__(self, a):
        self.__elements = a


    def computeDifference(self):
    	self.maximumDifference=max(a)-min(a)



# End of Difference class

_ = input()
print ("\nThere are %s elements in the array"%_)
a = [int(e) for e in input().split(" ")]
d = Difference(a)
d.computeDifference()

print("The maximum absolute difference between any 2 elements in the array is: ",  d.maximumDifference)
