## find method:
```js
db.books.find()
```

> this command is going to bring back first 20 documents. and with "it" command it's going to bring back 20 more

## filter data:
```js
db.books.find({author:"mahdi"})
db.books.findOne({author:"mahdi"})
```
## specify fields you need for find method:
```js
db.books.find({author:"mahdi"}, {name:1, })
```
## prettify the result:
```js
db.books.find().pretty()
```
