name= "Harry"
print(name[0:3])

print(name[-4:-1]) #question
print(name[1:4])  #ans: negative k positive banabo. then ultaye boshabo (-4:-1 => 1:4)  .output= arr

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])



# skip value ....

a="0123456789"
print(a[1:7:3])
# i) ekahne first e 1:7 solve= 123456(1 to 6 porjonto jabe). 
# ii)then [1:7:3] er jonno => 1 then 23 skip hoye porer character print hbe . 1, (23)x ,4=print

#output=> a[1:7:3]= 1,4

b="abcdefghijklmnopqrstuvwxyz"
print(b[1:8:2])

'''steps=> 1)1:8= bcdefgh
2):2 skips= b,d,f,h

'''

print(b[1:9:4])
'''steps=> 1)1:9= bcdefghi

2):2 skips= b,f
==> b, (cde), f, (ghi) 

=OUTPUT: BF


__________EXPLAIN:______
jehetu 4 katte bolse ,means 3 ghor skip. jodi 2 katte bole then 1 ghor skip. jodi 5 katte bole then 4 ghor skip.

'''
