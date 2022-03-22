#Introduction to Programming I

######## Topic#1 ########

# X Cubic
# Write a program which calculates the cube of a given integer x.
# Constaints: 1 <= x <= 100

number = int(input())
print(number**3)

# Rectangle
# Write a program which calculates the area and perimeter of a given rectangle.
# Constaints: 1<=a (length), b (breadth) <= 100

A,B = map(int,input().split())
print(A*B, 2*(A+B))


# Watch
# Write a program which reads an interger S[second] and converts it to h:m:s where h,m,s denote hours, minutes (less than 60) and seconds (less than 60) respectively.
# Constraints: 0<=S[second]<=86400
# Output: Print h,m and s separated by ':'. You do not need to put '0' for a value, which consists of a digit.
S = int(input())
print("%d:%d:%d"%(S/3600,(S%3600)/60,S%60))

