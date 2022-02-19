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

Useful python libraries:
[collections](https://docs.python.org/3/library/collections.html): useful subclasses include Counter, defaultdict
[bisect](https://docs.python.org/3/library/bisect.html): the bisect module provides super handy functions that does binary search for us.

->To make sure that the results of this method are memoized. In Python, we can use lru_cache
