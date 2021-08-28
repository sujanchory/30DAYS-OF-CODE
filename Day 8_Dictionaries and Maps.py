d=dict()
n=int(input())
for i in range (n):
    a,b=input().split(" ")
    d[a]=b
while True:
  try:
    a=input()
    if a in d.keys():
        print(a+"="+d[a])
    else:
        print("Not found")
  except:
    break
