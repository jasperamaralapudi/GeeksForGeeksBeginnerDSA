#User function Template for python3

class Solution:
    def transpose(self, mat, n):
        # Write Your code here
        for i in range(n):
            for j in range(i,n):
                mat[i][j], mat[j][i]=mat[j][i], mat[i][j]
        return mat

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    ob = Solution()
    ob.transpose(matrix, n)

    for row in matrix:
        print(*row)

    print("~")

# } Driver Code Ends