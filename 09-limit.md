## limit
> To limit the records in MongoDB, you need to use limit() method. The method accepts one number type argument, which is the number of documents that you want to be displayed.
### syntax
```js
db.COLLECTION_NAME.find().limit(NUMBER)
```
### example
```js
db.mycol.find({},{"title":1,_id:0}).limit(2)
```
## skip
> Apart from limit() method, there is one more method skip() which also accepts number type argument and is used to skip the number of documents

### syntax
```js
db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)
```
### example
```js
db.mycol.find({},{"title":1,_id:0}).limit(1).skip(1)
{"title":"NoSQL Overview"}
```
## count
> returns the number of the document matching the filter
### syntax
```js
db.COLLECTION_NAME.find().count()
```
### example
```js
db.mycol.find({},{"title":1,_id:0}).count()
```