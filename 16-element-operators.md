## exists
### syntax
```js
{ field: { $exists: <boolean> } }
```
> When boolean is true, 
$exists
 matches the documents that contain the field, including documents where the field value is null. If <boolean> is false, the query returns only the documents that do not contain the field

### example
```js
db.inventory.find( { qty: { $exists: true, $nin: [ 5, 15 ] } } )
```

## type
> selects documents where the value of the field is an instance of the specified BSON type(s). Querying by data type is useful when dealing with highly unstructured data where data types are not predictable.

### syntax
```js
{ field: { $type: <BSON type> } }
```
```js
{ field: { $type: [ <BSON type1> , <BSON type2>, ... ] } }
```
### BSON types:

Type|Number|Alias|
----|------|-----|
Double|1|"double"
String|2|"string"
Object|3|"object"
Array|4|"array"
Binary data|5|"binData"
ObjectId|7|"objectId"
Boolean|8|"bool"
Date|9|"date"
Null|10|"null"
Regular Expression|11|"regex"
JavaScript|13|"javascript"
32-bit integer|16|"int"
Timestamp|17|"timestamp"
64-bit integer|18|"long"
Decimal128|19|"decimal"
Min key|-1|"minKey"
Max key|127|"maxKey"

### example
```js
db.grades.find( { "classAverage" : { $type : [ 2 , 1 ] } } );
db.grades.find( { "classAverage" : { $type : [ "string" , "double" ] } } );
```