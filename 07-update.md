## update
### update operators
Name|Description
----|-----------
$currentDate|Sets the value of a field to current date, either as a Date or a Timestamp.
$inc|Increments the value of the field by the specified amount.
$min|Only updates the field if the specified value is less than the existing field value.
$max|Only updates the field if the specified value is greater than the existing field value.
$mul|Multiplies the value of the field by the specified amount.
$rename|Renames a field.
$set|Sets the value of a field in a document.
$setOnInsert|Sets the value of a field if an update results in an insert of a document. Has no effect on update operations that modify existing documents.
$unset|Removes the specified field from a document.

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
### example
```js
db.empDetails.updateOne(
	{First_Name: 'Radhika'},
	{$inc: { Age: 2}}
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