# -*- coding: utf-8 -*-
from pykafka import KafkaClient
from pykafka.common import OffsetType

client = KafkaClient('kfk0:11199')
topic = client.topics['test9']

def show_all_msg():
    consumer = topic.get_simple_consumer(
    # consumer_group="mygroup",
    auto_offset_reset=OffsetType.LATEST
    )
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)

def show_partitions(offset):
    # consumer = topic.get_simple_consumer(partitions)
    consumer = topic.get_simple_consumer(
    consumer_group="mygroup",
    auto_offset_reset=OffsetType.LATEST
)
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)

if __name__ == '__main__':
    show_all_msg()
    # show_partitions(400)
