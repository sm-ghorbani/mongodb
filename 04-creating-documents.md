## insert a document:
```js
db.books.insertOne({title:"song of ice", pages:500})
```

> *** you can insert data in a non-existing document and the documents will be created automatically
 
 ## insert many documents at once:
 ```js
db.books.insertMany([{obj1}, {obj2}])
```
