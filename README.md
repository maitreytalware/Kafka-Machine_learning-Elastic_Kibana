# Real time data handling with Kafka
##            <font color='gray'> Machine learning in production, with visualisation on real time</font>  
                                                 - Maitrey Talware
-----------------------------

#### *The main aim of this project is to build an scable architecture which has capibility to :-*

1. Handle Real Time Data - __*(Kafka)*__
2. Perform Machine learining on the fly on huge amount of data -  __*(SparkML)*__
3. Store large amount of data data - __*(Cassandra/Elastic)*__
4. Visualize on Real Time - __*(Kibana)*__

----------------------
## Table of contents

<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ol>
        <li><a href="#ref1">Introduction and Objective</a></li>
         <ul>
             <li><a href="#ref3">Architecture</a></li>
             <li><a href="#ref3">Components of Project</a></li>
        </ul>
                <li><a href="#ref2">Data</a></li>
        <ul>
         <li><a href="#ref3">Creating data</a></li>
        <li><a href="#ref4"> Structure of the Data</a></li>
        </ul>
        <li><a href="#ref2">Kafka</a></li>
        <ul>
            <li><a href="#ref3">Installing Kafka</a></li>
         <li><a href="#ref3">Starting the Zookeeper server</a></li>
         <li><a href="#ref3">Starting the Kafka server</a></li>
        </ul>
        <li><a href="#ref2">Cassandra</a></li>
        <ul>
         <li><a href="#ref3">Installing Cassandra</a></li>
         <li><a href="#ref3">Starting Cassandra Server</a></li>
         <li><a href="#ref3">Putting data into Cassandra</a></li>
        </ul>
        <li><a href="#ref2">ElasticSearch</a></li>
        <ul>
         <li><a href="#ref3">Installing ElasticSearch</a></li>
         <li><a href="#ref3">Starting the Elasticsearch Server</a></li>
         <li><a href="#ref3">Sending data to ElasticSearch</a></li>
        </ul>
                <li><a href="#ref2">Spark</a></li>
        <ul>
         <li><a href="#ref3">SparkML (Machine Learning in production)</a></li>
        </ul>
        <li><a href="#ref2">Kibana</a></li>
        <ul>
         <li><a href="#ref3">Installing Kibana</a></li>
         <li><a href="#ref3">Starting the Kibana Server</a></li>  
         <li><a href="#ref3">Visualisations</a></li>
        </ul>
        <li><a href="#ref9">How to Run this Project</a></li>
        <li><a href="#ref9">Conclusion section and Future Scope</a></li>
        <li><a href="#ref9">References</a></li>
    </ol>
</div>
<br>

--------------------
# 1. Introduction and Objective
Conventional methods of payment are long forgotten after the emergence of Credit cards. It has been observed that 86% of the millennials use Credit cards for payments, according to a report by FICO ®. But this report has also shown that in US alone, $11 Billion dollars is the damage extent in the year 2017, by means of unauthorized credit card transactions.
Since financial data is generally huge, and we need to find a meaning from the data in order to detect fraud prevention. Hence, this project will witness the conjunction of big data with machine learning in a real-time application, i.e. the transaction source needs to feed live data and we need to further channel it into the respective modules.

With the world accepting credit as a source of funds among all the sections of society, fraud detection becomes critical here. Fraudsters try to illicitly gather users' credit card information using sophisticated techniques. In order to detect out the fraudulent transactions, we use Big data coupled with machine learning.
Therefore, there is a need to automate the ever-increasing demand for fraud detection of valuable credit card transactions pertaining to particular features of the user’s spending interests. The fraud detection system detects transactions that are unusual and filters out the suspected transactions and our machine learning model makes the it a self-learning system as well.

--------------------
## <font color='gray'>1.1 Architecture Diagram</font> 

<img src="https://botjs2.s3.amazonaws.com/Architecture.png" width="800" height="400">

----------------------

## <font color='gray'>1.2 Components of Project</font> 


### 1. Apache Kafka
Apache Kafka is an open-source stream-processing software platform developed by LinkedIn and donated to the Apache Software Foundation, written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real- time data feeds.
### 2. Apache Spark
Apache Spark is an open-source distributed general-purpose cluster-computing framework. Spark provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.
 7
### 3. Apache Spark ML
Spark.ml is a new package introduced in Spark 1.2, which aims to provide a uniform set of high-level APIs that help users create and tune practical machine learning pipelines.
### 4. Apache Cassandra
Apache Cassandra is a free and open-source, distributed, wide column store, NoSQL database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure. Cassandra offers robust support for clusters spanning multiple data centers, with asynchronous master less replication allowing low latency operations for all clients.
### 5. Elasticsearch
Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.
### 6. Kibana
Kibana is an open source data visualization plugin for Elasticsearch. It provides visualization capabilities on top of the content indexed on an Elasticsearch cluster. Users can create bar, line and scatter plots, or pie charts and maps on top of large volumes of data.

--------------

# 2. Data

## <font color='gray'>2.1 Creating the data</font>  
We have built our own data simulator which is produces up to 80 transactions per second. But our architecture is not limited to this data. We have simulated the data to show how it will work in real world scenario, since getting a real transaction is out of scope.

------------------------

## <font color='gray'>2.2 Structure of the data</font> 
<img src="https://botjs2.s3.amazonaws.com/data-schema.png" width="600" height="600">

------------------------

# 3. Kafka
## <font color='gray'>3.1 Installing Kafka</font>  
Here's few great articles that I found on internet to install kafka
#### For Mac
https://medium.com/@Ankitthakur/apache-kafka-installation-on-mac-using-homebrew-a367cdefd273
#### For Windows
https://dzone.com/articles/running-apache-kafka-on-windows-os

### <font color='Red'>NOTE</font>  
From here on I will be putting commands for mac, commands for windows can be found from link above, they are almost similar for windows you just need to run .bat files

----------------------
## <font color='gray'>3.2 Starting the zookeeper Server</font>  


```python
zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
```

---------------------------
## <font color='gray'>3.3 Starting the Kafka Server</font>  


```python
kafka-server-start /usr/local/etc/kafka/server.properties
```

-----------------------
# 4. Cassandra
## <font color='gray'>4.1 Installing Cassandra</font>  
Here's few great articles that I found on internet to install cassandra
#### For Mac
https://medium.com/@areeves9/cassandras-gossip-on-os-x-single-node-installation-of-apache-cassandra-on-mac-634e6729fad6
#### For Windows



### <font color='red'>NOTE</font>  
From here on I will be putting commands for mac, commands for windows can be found from link above, they are almost similar for windows you just need to run .bat files

-----------------------
## <font color='gray'>4.2 Starting Cassandra Server</font>  


```python
sudo cassandra -f
```

--------------------
## <font color='gray'>4.3 Putting data into Cassandra</font>  


```python

```

---------------
# 5. ElasticSearch
## <font color='gray'>5.1 Installing ElasticSearch</font>  
##### Download and unzip elasticsearch from - https://www.elastic.co/downloads/elasticsearch

-----------------------
## <font color='gray'>5.2 Starting the Elastic Server</font>  
##### Open Terminal and cd to unzipped elasticsearch folder 
#### *For Mac*


```python
bin/elasticsearch
```

#### *For Windows*


```python
bin\elasticsearch.bat
```

---------------
# 6. Spark
## <font color='gray'>5.1 Installing spark</font>  


---------------
# 7. Kibana
## <font color='gray'>7.1 Installing Kibana</font>  
##### Download and unzip elasticsearch from - https://www.elastic.co/downloads/kibana

--------------
## <font color='gray'>7.2 Starting the Kibana Server</font>  
##### Open Terminal and cd to unzipped kibana folder 
#### *For Mac*


```python
bin/kibana 
```

#### *For Windows*


```python
bin\kibana.bat
```

---------------------------
# 8. CONCLUSION AND FUTURE SCOPE
## <font color='gray'>8.1 Conclusion</font>  

Credit Card transactions is one of the emerging ‘preferred-payment’ methods in the whole world, and we need to build fraud-detection that can process, protect and visualize the credit card transaction data.
Our system has managed to accurately classify the transactions based on the data generated from the producer system. The input data has been made robust such that it reduces any kind of data loss. After understanding the real time processing and analysis technologies, data is stored in distributed fashion and is retrieved using in real time using index-based search method. The processing and classification needed an appropriate method for visualization to have an overview of system performance and correct user understanding. Kibana tool has helped to achieve greater understanding using visualizations.

--------------
## <font color='gray'>8.2 Future Scope</font>  


### Maintained Scalability
Existing Architecture stack can accommodate more producers and consumers.
### Code Compatible for running on clusters
Simply changing the IP addresses of Elastic search, Kibana and Cassandra, we can run it on Cluster environment.
### More Data Accomodation
Predictability and ML can be more robust by adding more advanced Features for data.

---------------------------
# 9. References


```python

```
