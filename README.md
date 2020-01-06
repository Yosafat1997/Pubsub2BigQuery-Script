# Pubsub2BigQuery-Script
## A Python script to stream pubsub messages directly to BigQuery

### The Background
I have experienced when my subscription didn't work for a long time period (and i still don't know what happened with it till this day, but
fortunately, the stream works after 1 and half day in trouble).
The reason behind why i must "bypass" the operation to drop pubsub data into BigQuery, due the reason i missing a lot of data. So the mission
is to rescue all the stucked datas from pubsub current subscription to BigQuery before it expired.

### How it work
I have read a interesting article in here: https://medium.com/faun/writing-a-pub-sub-stream-to-bigquery-401b44c86bf about streaming data from
Pubsub subscriber to BigQuery. I modified some of the code. In this case, I dont use any transformation in the decoded JSON, and raw-added
the json into BigQuery. 

### TODO
I still don't know how to run it in cloud. Any help is appreciated. Also, i have some idea to validate the message, in case some null or improper message can cause trouble to the operation (ex: null date). Notice that, you must make sure that your JSON data has same key-value 
format as the target table (otherwise it will fail)

### Notes:
* Make sure you have valid and active GCP Project
* I recomend you to use newest Python version (up to 3.0, due 2.7 is discontinued)
* Make sure you have Google GCP SDK (for windows) and API (for the other)
* Make sure you have Google Cloud Library for Python; pubsub and bigquery 
* Make sure you have active BigQuery Dataset and Table and also active pubsub subscribers
* Pricing is depend on your project. You have your responsibility on pricing.
* This method using Asynchronous insertion, so you will have experienced any data with time information will added randomly and not sequenced.
* This project is free
