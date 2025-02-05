1. Indexing for faster query performance
    Indexes help MongoDB find data faster instead of looking through all the information. Without indexes, searches have to check everything, which makes it much slower as the amount of data increases.

types of indexing:
* Single-Field Indexes: Used for queries filtering on single field.
* Compound Indexes: Optimized for queries filtering on multiple fields.
* Text Indexes: Enhance text search capabilities.
* TTL Indexes: Automatically remove documents after a specific time.

before : <code>db.users.find({ email: "test-user@mail.com" });</code> <br>
after : <code>db.users.createIndex({ email: 1 });</code>
<hr>
2. Query Optimization Techniques
    poor structure of queries may lead to unnecessary computing, retrieval eventually slowing down the database.

techinques for query optimisation :
* Projection to Return Only Required Fields will Reduce data transfer load
* Avoiding $or Queries When Possible as they prevent index usage in some cases.
* Using Covered Queries that can be resolved using indexes alone, without accessing documents.

before : <code>db.orders.find({ customerId: "12345" });</code> <br>
after : <code>db.orders.createIndex({ customerId: 1 });
db.orders.find({ customerId: "12345" }, { _id: 0, orderDetails: 1 });
</code>
<hr>
3. Data partitioning for scalability
    partitioning data into multiples servers to handle large-scale applications in an more efficient way. It prevents performance degradation caused due to growing datasets.

* enable sharding
<code>sh.enableSharding("DB-Name");</code>
<br>
* create key 
<code>db.orders.createIndex({ orderId: "id" });
</code>
* shard the collection
<code>sh.shardCollection("DB-Name.collection-name", { orderId: "id" });
</code>