# kakfa_streaming_project
A data engineering project using Apache Kafka, Confluent Platform, Python, kSQLDB, MySQL and Tableau

## Project Outline

This project aims to mimick a real-life data engineering project by ingesting real-time flight data at Boston Logan International Airport from a REST API, 
conducting some transformations in kSQLDB and loading results into a data mart in mySQL for downstream analysis using Tableau. 

The inspiration is to create a stream processing service whereby the data is transformed in real time for further processing. The end product is a real-time dashboard where, for example, the marketing 
branch of a tourism company can see the most popular flight destinations in and out of Boston, which airlines are most popular, and so on.

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

## Next Steps

I had also experimented launching this whole project on the cloud using an Amazon EC2 instance. However, the free tier t2.micro instance is unequipped to handle Confluent Platform due to 
its limited resources and thus a bigger machine would be required to carry out this task.


