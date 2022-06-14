from kombu import Queue, Exchange

my_queues = [Queue("zengenti-cloud-high", Exchange("zengenti-cloud-high"), routing_key="zengenti-cloud-high"),
             Queue("zengenti-cloud-low", Exchange("zengenti-cloud-high"), routing_key="zengenti-cloud-low")]
