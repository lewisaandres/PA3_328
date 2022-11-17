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
'''
import sys

class Solution:
	def heapSort(self, arr: list): 
		self.buildHeap(arr) 

		for i in range(len(arr), 2): 
			swap(arr[1], arr[i])
			
	def heapSize(arr: list): 
		pass 
	
	def buildHeap(self, arr: list): 
		heapSize = len(arr)

		for i in range(len(arr)/2, 1): 
			self.heapify(arr, i) 

	def partition(self, arr: list, p: list, r: list): 
		x = arr[r] 
		i = p - 1 

		for j in range(p, r): 
			if arr[j] >= x: 
				i = i + 1
				temp = arr[j]
				arr[i] = arr[j]
		temp2 = arr[i+1]
		arr[i+1] = arr[r] 
		arr[r] = temp2 
		return i + 1

	# Used algo from pa3 pdf assigment instructions created by Professor Fahim 
	def kthSmallest(self, l: list, r: list, k: int): 
		if (k > 0 and k <= r - l): 
			q = self.partition(arr, l, r) 
		if (q == k): 
			return arr[q] 
		if (q > k): 
			return self.kthSmallest(arr, l, q - 1, k)
		return self.kthSmallest(arr, q + 1, r, k - q + 1)

	def pa3 (self, arr: list[int], k: int)	-> int:
		return True
		# your code must return a boolean
        # for example return True
		


if __name__ == '__main__':
	arr = sys.argv[1]
	k = sys.argv[2]
	obj = Solution()
	ret = obj.pa3(arr, k)
	print(ret)

