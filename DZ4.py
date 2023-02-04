d1={'key':'hello'}
d2={'k1':{"k2":'hello'}}
d3={'k1':[{'nest_key':['deep',['hello']]}]}
mylist = [1,1,1,1,1,1,2,2,2,2,3,3,3,3]
print (d1['key'])
print (d2['k1']['k2'])
print (d3['k1'][0]['nest_key'][1][0])
print (set(mylist))