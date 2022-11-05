## sort
> To sort documents in MongoDB, you need to use sort() method. The method accepts a document containing a list of fields along with their sorting order. To specify sorting order 1 and -1 are used. 1 is used for ascending order while -1 is used for descending order.
### syntax
```js
db.COLLECTION_NAME.find().sort({KEY:1})
```
### example
```js
db.mycol.find({},{"title":1,_id:0}).sort({"title":-1})
```