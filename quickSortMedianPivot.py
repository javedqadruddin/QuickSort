import sys

testArray1 = [5,1,3,4,2]
testArray2 = [6,5,4,3,2,1]
testArray3 = [2,1,3,4,5,6]
testArray4 = [2,1,3,4,5]
testArray5 = [2,1,3,4,5,6]
testArray6 = [2,1,3,4]


class QuickSorter:
	count = 0

	def sort(self, inputList, start, end):
		#print "end at beginning of sort is " + str(end)
		#print "start at beginning of sort is " + str(start)
		if (end - start) <= 1:
			return
		#print "quicksort: " + str(inputList[start:end])


		(pivotIndex, start, end) = self.partition(inputList, start, end)
		#print(inputList)
		#print "pivotIndex is " + str(pivotIndex)

		self.count += (pivotIndex - start) - 1
		#print(str(pivotIndex - start))
		self.sort(inputList, start, pivotIndex-1)
		self.count += (end - pivotIndex)
		#print(str(end - pivotIndex))
		self.sort(inputList, pivotIndex, end)

	def getMedian(self, inputList, start, end):
		endNumber = inputList[end-1]
		startNumber = inputList[start]
		midNumber = inputList[start + ((end-1) - start) / 2]

		#print "median of " + str(endNumber)+ " " + str(startNumber) + " " + str(midNumber)

		if startNumber<endNumber<midNumber or midNumber<endNumber<startNumber:
			return endNumber, end-1
		elif endNumber<startNumber<midNumber or midNumber<startNumber<endNumber:
			return startNumber, start
		else:
			return midNumber, start + ((end-1) - start) / 2


	def partition(self, inputList, start, end):
		pivot, index = self.getMedian(inputList, start, end)
		#print "pivot is " + str(pivot)

		inputList[start], inputList[index] = inputList[index], inputList[start]
		i = start+1
		for j in range(start+1, end):
			#self.count += 1
			if inputList[j] < pivot:
				#swaps two positions in the list
				inputList[j], inputList[i] = inputList[i], inputList[j]
				i += 1

		inputList[start], inputList[i-1] = inputList[i-1], inputList[start]
		#print(inputList)

		return i, start, end

	def getCount(self):
		return self.count

sorter = QuickSorter()

def testSort():
	print(testArray5)
	sort(testArray5,0,len(testArray5))
	print(testArray5)
	print "\n"

	print(testArray2)
	sort(testArray2,0,len(testArray2))
	print(testArray2)
	print "\n"

	print(testArray3)
	sort(testArray3,0,len(testArray3))
	print(testArray3)
	print "\n"

	print(testArray6)
	sort(testArray6,0,len(testArray6))
	print(testArray6)

def testPartition():
	print(testArray2)
	print(partition(testArray2,0,len(testArray2)))
	print(testArray5)
	print(partition(testArray5,0,len(testArray5)))
	print(testArray3)
	print(partition(testArray3,0,len(testArray3)))
	print(testArray6)
	print(partition(testArray6,0,len(testArray6)))

# print testArray1
# print(sorter.getMedian(testArray1, 0,len(testArray1)))


f = open('QuickSort.txt', 'r')
numbers = []
for line in f:
	numbers.append(int(line))

sorter.sort(numbers, 0, len(numbers))
print(numbers)
print sorter.getCount()
