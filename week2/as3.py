"""Input Format:

The first line of the input contains a number N representing the number of elements in array A.
The second line of the input contains N numbers separated by a space. (after the last elements, there is no space)

Output Format:

Print the resultant array elements separated by a space. (no space after the last element)

Example:

Input:
4
2 5 3 1

Output:
3 8 8 3
"""


n = int(input())
a=list(map(int,input().split()))
for i in range(n-1):
  print(a[i]+a[-i-1],end=" ")
print(a[0]+a[-1],end="")

