from kombu import Exchange, Queue

custom_exchange = Exchange('zengenti-cloud', type='direct')
my_queues = [Queue('zengenti-cloud-high', custom_exchange, routing_key='high'),
             Queue('zengenti-cloud-low', custom_exchange, routing_key='low')]
