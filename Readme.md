## Process to start
1. Start server using
```bash
python manage.py runserver
```
2. Open second terminal
```bash
python manage.py process_queue --queues search.fifo
```

## Requests
curl --location --request POST 'http://127.0.0.1:8000/search/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "words":["sample","12"]
}'

## Modification

1. Edit eb_sqs/aws/sqs_queue_client.py 
replace
```python
import json
id = json.loads(msg)["id"]
queue.send_message(
    MessageBody=msg,
    DelaySeconds=delay,
    MessageGroupId="sample",1
    MessageDeduplicationId=id
)
```
