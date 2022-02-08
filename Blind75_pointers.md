# Arrays
* two pointers
```
general syntax
let i and j be two pointers
while i!=j: #some converging condition..
  /*
  some computation
  */
  usually finding max() or min()..
```
* Backtracking
```
N Queens, combination sum->https://leetcode.com/problems/combination-sum/(subset problem), sudoku,..
```

* Duplicates
```
hashtables, sorting
```

* Max subarray
```
Kadane's algorithm - iterative dynamic programming approach
```

* Searching/finding min or max in a sorted Array
```
Binary search: general template::
start = 0
end = len(arr)-1
while(start<=end):
  mid = (start+end)//2
  /*
  some comparison and updation of start and end
  */
return arr[mid]
```
