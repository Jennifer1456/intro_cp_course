from turtle import hideturtle


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(0, 26):
    ans = letters[i:26] + letters[0:i]
    print(ans)
