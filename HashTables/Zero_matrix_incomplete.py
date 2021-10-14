'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Do it in place so no additional memory is required

This is incomplete and will try to revisit when ever possible
'''
def zero_matrix(in_matrix):
    m=len(in_matrix)
    n=len(in_matrix[0])

    #we can note
