## elemMath
> The $elemMatch
 operator matches documents that contain an array field with at least one element that matches all the specified query criteria.

 ### syntax
 ```js
 { <field>: { $elemMatch: { <query1>, <query2>, ... } } }
 ```

 ### example
 ```js
 db.scores.find(
   { results: { $elemMatch: { $gte: 80, $lt: 85 } } }
)
```

### example with embedded documents
```js
db.survey.find(
   { results: { $elemMatch: { product: "xyz", score: { $gte: 8 } } } }
)
```