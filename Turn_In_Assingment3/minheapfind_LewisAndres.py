'''
Please use the code template below to complete your assignment.
Your code must go under pa3 method. 
Do not change any other code. 
The evaluation code uses this templete to run your test cases.
Any changes other than pa1 method would cause the evaluation method 
stop working and you will not get credit for your submission.

name: Lewis Andres
studentID: 026741843
assignment:PA3
Using MINHEAP algo 
'''
import sys

class Solution:
	# function to have top node parent just in case for program
	def parent(self, i): 
		return i/2
	# function to have left side of node binary tree
	def left(self, i):
		return 2*i

	# function to have right side of node binary tree
	def right(self, i):
		return 2*i + 1
	# function to return size of array. Made a function because it was just easier
	def heapSize(self, arr): 
		return len(arr) - 1
	# Heapify function to heapify the binary tree 
	def heapify(self, arr, size, i):
		l = self.left(i)
		r = self.right(i)
		#sets largest to l or i if between size and arr comparison
		if (l < size and arr[l] >arr[i]):
			largest = l
		else: 
			largest = i
		
		if (r < size and arr[r] > arr[largest]):
			largest = r 
		# if largest != i, swap arrays of largest and i and then continue heapify 
		if (largest != i):
			(arr[i], arr[largest]) = (arr[largest], arr[i])  #swap
			#calling heapify function recursion 
			self.heapify(arr, size, largest)
	# Builds heap, max heap from lecture notes 
	def buildHeap(self, arr):
		# save heapsize to len var
		len = self.heapSize(arr)
		# heapify for every node bottom to top
		for i in range((len//2), -1, -1):
			self.heapify(arr, len, i)
		#print("Build heap array: \n" + str(arr))
		return arr
    # sorts the array in descending order
	def heapSort(self, arr):
		size = self.buildHeap(arr)
		len = self.heapSize(arr)
		# in descending order, heapify 
		for i in range(len, -1, -1):
			(arr[i], arr[0]) = (arr[0], arr[i]) 
			len = len - 1 
			self.heapify(arr, i, 0)
		return sys.maxsize
		
		
	# sorts the array using heapsort, then returns k-1 index 
	# checks if k < 0 and array is out of bounds 
	def minHeap(self, arr, k):
		self.heapSort(arr)
		#print("Heapsort array: \n" + str(arr), end=" ")
		if (k < 0): 
			return -1
		try: 
			return arr[k-1]
		except: 
			return -1

	# set retval to self.minHeap 
	def pa3 (self, arr: list[int], k: int )	-> int:
		retval = 0
		#print("Input array: ")
		print(arr, k)	
		#print()
		
		# your code must return a boolean
        # for example return True
		# print("build heap:\n" + str(self.buildHeap(arr)))

		retval = self.minHeap(arr, k)
		#print("\n\nOutput: ", end=" ")
		return retval

# Please make your function call as
# PA3_yourname.py 2,3,4,5 4

if __name__ == '__main__':
	arr = []
	arrtemp = sys.argv[1].split(",")
	for item in arrtemp:
		arr.append(int(item))

	k = int(sys.argv[2])
	obj = Solution()
	ret = obj.pa3(arr, k)
	print(ret)
