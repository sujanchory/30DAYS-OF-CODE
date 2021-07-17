# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
      s=input()
      even=str()
      odd=str()
      for j in range(0,len(s)):
          if j%2==0:
            even+=s[j]
          else:
            odd+=s[j]
      print('{} {}'.format(even,odd))
