# The Eye

![Image of The Eye](https://news.cgtn.com/news/2020-07-14/Sauron-5G-and-the-Five-Black-Eyes-S7i9xRgjgA/img/6e8874393dd546f5a50c8f4f3aa727d9/6e8874393dd546f5a50c8f4f3aa727d9.png)

Coding Challenge for Consumer Affairs


## Context

**The Eye** is an information gathering api that accepts post requests from within the organization. It is built on a Django framework, Running a postgresQL Database, and a Django REST Framework.  It only has one POST endpopint `https://wwww.TheyEye.com/gather`. Upon seccessful reciept of event it will transmit a response to the client

The clients transmit event objects serialized as JSON data. These JSON objects have a semi regular structure. Each object will have a session_id, category, name, a data payload that can be further nested JSON data and a timestamp. The payload structure is not the same across client applications. The client is responsable for the generation of all this information. 

Once information has been gathered it is available to query through the PostgreSQL client GUI.


## Future improvements
* Native gui for querying data rather than working with Postgres Client
* Futher destructuring data payload for more detailed queries.
    * Restructure tables for more robust storage (add additional validations)
    * Create separate payload table to 
* Asynchronous Handling of POST requests to increase bandwidth of requests
    * Build out celery worker functions to parce nested json objects with **kwargs attr
* Unit testing
* Integration Testing
