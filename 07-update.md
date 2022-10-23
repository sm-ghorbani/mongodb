## update
### syntax
```js
db.COLLECTION_NAME.update(SELECTION_CRITERIA, UPDATED_DATA)
```
### example
```js
db.mycol.update({'title':'MongoDB Overview'},{$set:{'title':'New MongoDB Tutorial'}})
```
> By default, MongoDB will update only a single document. To update multiple documents, you need to set a parameter 'multi' to true.
```js
db.mycol.update({'title':'MongoDB Overview'},
   {$set:{'title':'New MongoDB Tutorial'}},{multi:true})
```
## save
> The save() method replaces the existing document with the new document passed in the save() method.


### syntax
```js
db.COLLECTION_NAME.save({_id:ObjectId(),NEW_DATA})
```
### example
```js
db.mycol.save(
   {
      "_id" : ObjectId("507f191e810c19729de860ea"), 
		"title":"Tutorials Point New Topic",
      "by":"Tutorials Point"
   }
)
```
## findOneAndUpdate
### syntax
```js
db.COLLECTION_NAME.findOneAndUpdate(SELECTIOIN_CRITERIA, UPDATED_DATA)
```
### example
```js
db.empDetails.findOneAndUpdate(
	{First_Name: 'Radhika'},
	{ $set: { Age: '30',e_mail: 'radhika_newemail@gmail.com'}}
)
```
## updateOne
### syntax
```js
db.COLLECTION_NAME.updateOne(<filter>, <update>)
```
### example
```js
db.empDetails.updateOne(
	{First_Name: 'Radhika'},
	{ $set: { Age: '30',e_mail: 'radhika_newemail@gmail.com'}}
)
```
## updateMany
### syntax
```js
db.COLLECTION_NAME.updateMany(<filter>, <update>)
```
### example
```js
db.empDetails.updateMany(
	{Age:{ $gt: "25" }},
	{ $set: { Age: '00'}}
)
```