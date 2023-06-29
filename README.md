# kakfa_streaming_project
A data engineering project using Apache Kafka, Confluent Platform, Python, kSQLDB, MySQL and Tableau.

Project video below:

https://youtu.be/Ts06yH69lSU 


## Project Outline

![image](https://github.com/jpa203/kakfa_streaming_project/assets/104007355/4d4bc9ef-b50b-448b-afc2-5f475a5447bb)


This project aims to mimick a real-life data engineering project by ingesting real-time flight data at Boston Logan International Airport from a REST API, 
conducting some transformations in kSQLDB and loading results into a data mart in mySQL for downstream analysis using Tableau. 

The inspiration is to create a stream processing service whereby the data is transformed in real time for further processing. The end product is a real-time dashboard where, for example, the marketing 
branch of a tourism company can see the most popular flight destinations in and out of Boston, which airlines are most popular, and so on.

At one point, this project was to exist totally on a cloud platform - but doing so would result in going beyond Amazon's free tier luxuries. Hence, this was scrapped, but for the sake of practice - an S3 bucket acted as a consumer of the data to act as a pseudo data lake.

## About Apache Kafka

Apache Kafka runs on the publisher/subscriber messaging architecture (referred to as Producers/Consumers in Kafka) characterized by the sender (publisher) of a piece of data (message) not speificallt directing it to a receiver. 

Instead, the publisher classifies the message somehow, and the receiver (subscriber) subscribes to receive certain classes of messages.

Pub/sub systems often have a broker, a central point where message are published, to facilitate this.

Unlike traditional pub/sub systems, Apache Kafka solves the problem of coordinating several pub/sub systems but centralizing efforts into a distributed streaming platform with durable, in-order record read and scaling capabilities.

Data is processed in Kafka as a message - an array of bytes - with optional metadata, known as a the key, for partition purposes. Messages are written into Kafka in batches, all of whic are being produced to the same topic and partition. 

In Kafka, a schema can be imposed on the message - whether it be JSON, XML, - but the preference among most developers is Apache Avro for its strong data typing and schema evolution, with both backward and forward compatibility. 

In Confluent, schemas as stored in the Schema Registry, which allows for a decoupled approach to reading and writing messagaes whereby schemas can be inferred without coordination between publisher and subscriber - thus permitting a continuous and seamless streaming process.

Kafka categorizes its data in topics - similar to a table in relational databases or a keyspace in Apache Cassandra - which are broken down into partitions. Messages are written to a topic in an append-only fashion, and are read in order from beginning to end. 

After data is ingested into a Kafka topic, it may be partitioned dependent on a key. This is done to introduce a level of fault tolerance and scalability. When it is ready to be consumed, a client will subscribe to one or more topics and read the messages in the order in which they were produced. 

A consumer can keep track of which message it has already consumed by keeping track of the offset of messages - another bit of metadata, much like a serial key in postgres. 

A single Kafka server is called a broker. Kafka brokers are designed to operate as part of a cluster. Within a cluster of brokers, one broker will also function as the cluster controller (elected automatically from the live members of the cluster). The controller is responsible for administrative operations, incuding assigning partitions to brokers and monitoring for broker failures. A partition is owned by a single broker in the cluster, and that broker is called the leader of the partition. A partition may be assigned mto multiple brokers, which will result in the partition being replicated.

A key feature of Apache Kafka is that of retention, which is the durable storage of message for some period of time or until the topic reaches a certain size in bytes. 

As mentinoed previously, one of the main benefits of Kafka is its ability to scale out. This is done by having multiple clusters, which allows for the segregation of types of data, isolation for security requirements and multiple datacenters for disaster recovery. 

## About kSQLDB

This project made use of the ksqlDB - a lightweight, databaes system purposefully built for event streaming.

You can use ksqlDB to build event streaming applications from Apache Kafka topics by using only SQL statements and queries. ksqlDB is built on Kafka Streams, so a ksqlDB application communicates with a Kafka cluster like any other Kafka Streams application.

![image](https://github.com/jpa203/Apache-Kafka-ksqlDB-MySQL-Tableau/assets/104007355/ddffcfa3-b9fa-45dc-86d6-557212f0dd78)

Streams, i.e. materialized views, were used to aggregate and filter data before feeding it into a denormalized table in MySQL.

The result from the generated Kafka Streams application is a persistent query that writes continuously to its output topic until the query is terminated.


## Stream Processing

A data stream is an abstraction representing an unbounded dataset. Unbounded means infinite and ever growing. We can look at a stream of credit card transactions, stock trades, emails sent, moves in a game, or in this case, flights landing in Boston.

An event stream is ordered (events happen sequentially) which is what helps distingusih between a database table (note ORDER BY) and an event stream. 

Other features of event streams:
  * event streams are immutable (WORM)
  * event streams are replayable - required to correct efforts, try new methods of analysis or perform audits.

## Key Takeaways

I worked on this project before realizing the full benefit of working in a virtual environment or Docker container. 

## Next Steps

I had also experimented launching this whole project on the cloud using an Amazon EC2 instance. However, the free tier t2.micro instance is unequipped to handle Confluent Platform due to  its limited resources and thus a bigger machine would be required to carry out this task.


