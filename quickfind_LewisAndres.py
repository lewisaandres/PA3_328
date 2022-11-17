'''
Please use the code template below to complete your assignment.
Your code must go under pa3 method. 
Do not change any other code. 
The evaluation code uses this templete to run your test cases.
Any changes other than pa1 method would cause the evaluation method 
stop working and you will not get credit for your submission.

name: Lewis Andres
studentID: 026741843
USING quicksort kthSmallest algo
assignment:PA3
'''
import sys

class Solution:
	# partition function reused from lecture notes and pa2 partition
	# changed i = p - 1 to i = p to start at partition 1
	def partition(self, arr, p, r):
		x = arr[r]
		i = p 
		#swaps if less than the partition split
		for j in range(p, r): 
			if arr[j] <= x:
				#using temp, could use python's way, but kept it the same from pa2
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp 
				i = i + 1
		temp2 = arr[i]
		arr[i] = arr[r]
		arr[r] = temp2
		return i
	# function to call kthSmallest using provided function from notes
	#changed value q to subtract by q-l to see if its equal to k-1(at start of arr[k])
	def kthSmallest(self, arr, l, r, k):
		if (k > 0 and k <= r - l + 1):
			q = self.partition(arr, l, r) 
			if (q-l == k-1):
				return arr[q]
			if (q-l > k-1): 
				return self.kthSmallest(arr, l, q - 1, k)
			return self.kthSmallest(arr, q + 1, r, k - q + l - 1)
		#returns -1 if kthSmallest input out of bounds /array
		return -1


	# def quickSort(self, arr, p, r): 
	# 	if (p < r):
	# 		q = self.partition(arr, p, r)
	# 		self.quickSort(arr, p, q-1)
	# 		self.quickSort(arr, q+1, r)
	# 	print(arr)

	# set retval to self.kthSmallest function 
	def pa3 (self, arr: list[int], k: int )	-> int:
		retval = 0
		print(arr, k)	

		size = len(arr)

		# retval = self.quickFind(arr, size)
		retval = self.kthSmallest(arr, 0, size - 1, k)
		
		# your code must return a boolean
        # for example return True
		
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

