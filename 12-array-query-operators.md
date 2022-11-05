## all
> The $all operator selects the documents where the value of a field is an array that contains all the specified elements.

### syntax
```js
db.COLLECTION_NAME.find({ <field>: { $all: [ <value1> ,<value2> ... ] } })
```
### example
```js
db.articles.find( { tags: { $all: [ [ "ssl", "security" ] ] } } )
```

## size
> The $size operator selects the documents where the value of a field is an array that has the specified size.

### syntax
```js
db.COLLECTION_NAME.find({ <field>: { $size: number } })
```
### example
```js
db.articles.find( { tags: { $size: 2 } } )
```