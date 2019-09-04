## Description
This app responds to webhook notifications from Sqreen by 
checking the signature and redispatching those notifications.
The app that Sqreen is monitoring is itself.

## Setup
You will need to install `pytest`. I'm using version 4.6.4.

## Run
`$ flask run`

## Run Tests
`$ pytest`

To test routes, you can use curl. Here's an example that posts json
data to the `/notify` route:
```$ curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:5000/notify```