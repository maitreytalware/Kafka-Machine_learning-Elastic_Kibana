# Real time data handling with Kafka
##            <font color='gray'> Machine learning in production, with visualisation on real time</font>  
                                                                            - Maitrey Talware
----------------------
## Table of contents

<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ol>
        <li><a href="#ref1">Introduction and Objective</a></li>
         <ul>
             <li><a href="#ref3">Architecture</a></li>
        </ul>
                <li><a href="#ref2">Data</a></li>
        <ul>
         <li><a href="#ref3">Creating data</a></li>
        <li><a href="#ref4"> Structure of Data</a></li>
        </ul>
        <li><a href="#ref2">Kafka</a></li>
        <ul>
         <li><a href="#ref3">Starting the Zookeeper server</a></li>
         <li><a href="#ref3">Starting the Kafka server</a></li>
        </ul>
        <li><a href="#ref2">Cassandra</a></li>
        <ul>
         <li><a href="#ref3">Connecting to Cassandra</a></li>
         <li><a href="#ref3">Putting data into Cassandra</a></li>
        </ul>
        <li><a href="#ref2">ElasticSearch</a></li>
        <ul>
         <li><a href="#ref3">Starting the Elasticsearch</a></li>
         <li><a href="#ref3">Sending data to ElasticSearch</a></li>
        </ul>
                <li><a href="#ref2">Spark</a></li>
        <ul>
         <li><a href="#ref3">SparkML (Machine Learning in production)</a></li>
        </ul>
        <li><a href="#ref2">Kibana</a></li>
        <ul>
         <li><a href="#ref3">Visualisations</a></li>
        </ul>
        <li><a href="#ref7">Results</a></li>
        <li><a href="#ref9">Conclusion section</a></li>
    </ol>
</div>
<br>

# 1. Introduction and Objective
Conventional methods of payment are long forgotten after the emergence of Credit cards. It has been observed that 86% of the millennials use Credit cards for payments, according to a report by FICO ®. But this report has also shown that in US alone, $11 Billion dollars is the damage extent in the year 2017, by means of unauthorized credit card transactions.
Since financial data is generally huge, and we need to find a meaning from the data in order to detect fraud prevention. Hence, this project will witness the conjunction of big data with machine learning in a real-time application, i.e. the transaction source needs to feed live data and we need to further channel it into the respective modules.

With the world accepting credit as a source of funds among all the sections of society, fraud detection becomes critical here. Fraudsters try to illicitly gather users' credit card information using sophisticated techniques. In order to detect out the fraudulent transactions, we use Big data coupled with machine learning.
Therefore, there is a need to automate the ever-increasing demand for fraud detection of valuable credit card transactions pertaining to particular features of the user’s spending interests. The fraud detection system detects transactions that are unusual and filters out the suspected transactions and our machine learning model makes the it a self-learning system as well.

## Architecture Diagram

# 3. Kafka
## <font color='gray'>Install Kafka</font>  
Here's few great articles that I found on internet to install kafka
#### For mac
https://medium.com/@Ankitthakur/apache-kafka-installation-on-mac-using-homebrew-a367cdefd273
#### For Windows
https://dzone.com/articles/running-apache-kafka-on-windows-os

### NOTE 
From here on I will be putting commands for mac, commands for windows can be found from link above, they are almost similar for windows you just need to run .bat files

## <font color='gray'>Starting the zookeeper Server</font>  


```python
zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
```

## <font color='gray'>Starting the Kafka Server</font>  

kafka-server-start /usr/local/etc/kafka/server.properties


```python

```


```python

```
