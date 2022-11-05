## mongo db queries

#### equality:
```js
db.books.find({"by":"tutorials point"})
```
#### less than:
```js
db.books.find({"likes":{$lt:50}})
```

#### less than equal:
```js
db.books.find({"likes":{$lte:50}})
```
#### greater than:
```js
db.book.find({"likes":{$gt:50}})
```

#### greater than equal:
```js
db.books.find({"likes":{$gte:50}})
```
#### not equal:
```js
db.books.find({"likes":{$ne:50}})
```
#### Values in an array	
```js
db.books.find({"name":{$in:["Raj", "Ram", "Raghu"]}})
```
#### Values not in an array	
```js
db.books.find({"name":{$nin:["Raj", "Ram", "Raghu"]}})
```
#### and
```js
db.books.find({ $and: [ {<key1>:<value1>}, { <key2>:<value2>} ] })
```
#### or
```js
db.books.find({ $or: [ {<key1>:<value1>}, { <key2>:<value2>} ] })
```
#### nor
```js
db.books.find(
	{
		$not: [
			{key1: value1}, {key2:value2}
		]
	}
)
