## aggregate
> Aggregations operations process data records and return computed results. Aggregation operations group values from multiple documents together, and can perform a variety of operations on the grouped data to return a single result. In SQL count(*) and with group by is an equivalent of MongoDB aggregation.

### syntax
```js
db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)
```

### example
```js
db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : 1}}}])
```
#### $sum
##### description
>> Sums up the defined value from all documents in the collection.
```js
db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : "$likes"}}}])
```

#### $avg
##### description
>> Calculates the average of all given values from all documents in the collection.
```js
db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$avg : "$likes"}}}])
```

#### $min
##### description
>> Gets the minimum of the corresponding values from all documents in the collection.
```js
db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$min : "$likes"}}}])
```

#### $max
##### description
>> Gets the maximum of the corresponding values from all documents in the collection.
```js
db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$max : "$likes"}}}])
```

#### $push
##### description
>> Inserts the value to an array in the resulting document.
```js
db.mycol.aggregate([{$group : {_id : "$by_user", url : {$push: "$url"}}}])
```

#### $addToSet
##### description
>> Inserts the value to an array in the resulting document but does not create duplicates.
```js
db.mycol.aggregate([{$group : {_id : "$by_user", url : {$addToSet : "$url"}}}])
```

#### $first
##### description
>> Gets the first document from the source documents according to the grouping. Typically this makes only sense together with some previously applied “$sort”-stage.	
```js
db.mycol.aggregate([{$group : {_id : "$by_user", first_url : {$first : "$url"}}}])
```

#### $last
##### description
>> Gets the last document from the source documents according to the grouping. Typically this makes only sense together with some previously applied “$sort”-stage.	
```js
db.mycol.aggregate([{$group : {_id : "$by_user", last_url : {$last : "$url"}}}])
```
