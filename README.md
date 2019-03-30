# python-twitter-kafka-producer

A very simple kafka producer written in python that steams tracked keywords

## Run
* install requirements from `requirements.txt`
* start zookeeper & kafka locally (assumes broker @ `127.0.0.1:9092` or `KAFKA_BROKER` environment variable)
* add twitter environment variables to `.bash_profile`
  * `TWITTER_CONSUMER_KEY`
  * `TWITTER_CONSUMER_SECRET`
  * `TWITTER_ACCESS_TOKEN`
  * `TWITTER_ACCESS_SECRET`
* run `python producer.py TOPIC KEYWORD1 KEYWORD2 ... KEYWORDN`
  * example: `python producer.py twitter-topic01 kafka python`
* start a kafka consumer
  * example: `kafkakat -b 127.0.0.1:9092 -t twitter-topic01`
  
## Details
* Messages are posted as JSON:
```JSON
{
  "user": "",
  "message": ""
}
```
