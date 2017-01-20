If using anaconda -> disable to use default system-python2 (for now zappa dosent work with conda)
You need to be autheticated on aws-cli (create and apropriate IAM for that)

```bash
aws configure
virtualenv zappaenv
source zappaenv/bin/activate
pip install -r requirements.txt
```

run zappa deployment (follow trough interactive procedure)

```bash
zappa init
```

To create a aws-event-trigger edit the zappa_settings.js file:
(change the arn:aws:s3 bucket name to a bucket you own and have access to)
```js
{
    "dev": {
        "app_function": "s3trigger.trigger", 
        "s3_bucket": "zappa-ybyne0ei9",

    "events": [{
            "function": "s3trigger.trigger",
            "event_source": {
                  "arn":  "arn:aws:s3:::i008",
                  "events": [
                    "s3:ObjectCreated:*" // Supported event types: http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#supported-notification-event-types
                  ]
               }
            }]

    }
}

```

the function you trigger using Lambda has to accept the event and context (or *args, **kwargs) for that matter.

```python
def trigger(event, context):
    print(event)
    print(context)

```



```bash
zappa deploy
```

```bash
zappa undeploy
```

```bash
zappa update
```


