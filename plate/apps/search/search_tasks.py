from eb_sqs.decorators import task


@task(queue_name='search.fifo')
def add_search(data):
    print(f"Search word : {data}")
