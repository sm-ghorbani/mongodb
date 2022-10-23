## create a collection:
```
db.createCollection(name, options)
```
### options:
|Field |Type|Description|
|-----|--------|---------
|capped|Boolean|(Optional) If true, enables a capped collection. Capped collection is a fixed size collection that automatically overwrites its oldest entries when it reaches its maximum size. If you specify true, you need to specify size parameter also.
|autoIndexId  |Boolean      |(Optional) If true, automatically create index on _id field.s Default value is false.
|size|number|(Optional) Specifies a maximum size in bytes for a capped collection. If capped is true, then you need to specify this field also.
|max|number|(Optional) Specifies the maximum number of documents allowed in the capped collection.|

## drop collection:
```
db.collectionName.dropCollection()
```