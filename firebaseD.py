from firebase import firebase
import json as simplejson
firebase = firebase.FirebaseApplication('https://blistering-fire-6119.firebaseio.com',None)
result  = firebase.get('/users',None)
print result
 
location_1 = 'Avaliable'
location_2 = 'Not avaliable'
name = {'Morningside_dr':location_1, "123st":location_2}
#data = json.dumps(name)
#URL = 'https://blistering-fire-6119.firebaseio.com/users'
#print firebase.get(URL)
a = firebase.patch('/status',name) 
#post = firebase_.post('/users',name)

#print post
 

