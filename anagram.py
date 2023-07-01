string=input()
string2=input()
string="".join(string.split())
string2="".join(string2.split())
string=string.upper()
string2=string2.upper()
if sorted(string)==sorted(string2):
   print("anagram string")
else:
   print("not an anagram")

