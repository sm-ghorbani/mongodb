## createIndex
> To create an index, you need to use createIndex() method of MongoDB.
### syntax
```js
db.COLLECTION_NAME.createIndex({KEY:1})
```
### example
```js
db.mycol.createIndex({"title":1})
```

### options
|Parameter|	Type|	Description|
----------|-----|---------------|
background|	Boolean|	Builds the index in the background so that building an index does not block other database activities. Specify true to build in the background. The default value is false.
unique|	Boolean|	Creates a unique index so that the collection will not accept insertion of documents where the index key or keys match an existing value in the index. Specify true to create a unique index. The default value is false.
name|	string|	The name of the index. If unspecified, MongoDB generates an index name by concatenating the names of the indexed fields and the sort order.
sparse	Boolean	If true, the index only references documents with the specified field. These indexes use less space but behave differently in some situations (particularly sorts). The default value is false.
expireAfterSeconds|	integer|	Specifies a value, in seconds, as a TTL to control how long MongoDB retains documents in this collection.
weights|	document|	The weight is a number ranging from 1 to 99,999 and denotes the significance of the field relative to the other indexed fields in terms of the score.
default_language|	string|	For a text index, the language that determines the list of stop words and the rules for the stemmer and tokenizer. The default value is English.
language_override|	string|	For a text index, specify the name of the field in the document that contains, the language to override the default language. The default value is language.

## dropIndex
> You can drop a particular index using the dropIndex() method of MongoDB.

### syntax
```js
db.COLLECTION_NAME.dropIndex({KEY:1})
dropIndex("name_of_the_index")
```
### example
```js
db.mycol.dropIndex({"title":1})
```
## getIndexes
> This method returns the description of all the indexes int the collection.
### syntax
```js
db.COLLECTION_NAME.getIndexes()
```
### example
```js
db.mycol.getIndexes()
```
