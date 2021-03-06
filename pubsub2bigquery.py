import base64
import json

from google.cloud import bigquery, pubsub_v1
import google.cloud as cld


def pubsub2json(data):
    tracks = []
    streamer = data
    raw = json.loads(streamer)
    data = raw
    rows.append(data)
    print(rows)
    write_to_bq(rows)


def write_to_bq(msg):
    client = bigquery.Client().from_service_account_json(r'<YOUR CREDENTIAL FILE>')
    dataset_ref = client.dataset('<YOUR DATASET>')
    table_ref = dataset_ref.table('<YOUR TABLE>')
    table = client.get_table(table_ref)
    errors = client.insert_rows(table, msg)
    if not errors:
        print('Loaded {} row(s) into {}:{}'.format(len(msg), '<YOUR DATASET>',
                                                   '<YOUR TABLE>'))
    else:
        print('Errors while drop to Bigquery:')
        for error in errors:
            print(error)


def PubSub2BQ():
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(
        '<YOUR GCP PROJECT>', '<PUBSUB SUBSCRIPTION>'
    )

    def callback(message):
        print("Received message : {}".format(message.data))
        pubsub2json(message.data)
        message.ack()

    future = subscriber.subscribe(
        subscription_path, callback)
    print("Listening for message on {}..\n".format(subscription_path))

    try:
        future.result()
    except Exception as ex:
        raise
        future.cancelled()
    finally:
        future.cancelled()


def main():
    PubSub2BQ()


if __name__ == '__main__':
    PubSub2BQ()

