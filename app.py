from flask import Flask, request, json
import pandas as pd
from azure.storage.blob import BlockBlobService

app = Flask(__name__)
storage_key = "UkI6p0qbJs1oYRVn0KA8x5hQiRCfs+JJXF51+gSuT4f8NRdN1jytovwHnzQIS4ajjYWZxJgaSqpQ+AStnG1I5A=="
storage_account_name = "speechspeed"
connection_string = "DefaultEndpointsProtocol=https;AccountName=speechspeed;AccountKey=UkI6p0qbJs1oYRVn0KA8x5hQiRCfs+JJXF51+gSuT4f8NRdN1jytovwHnzQIS4ajjYWZxJgaSqpQ+AStnG1I5A==;EndpointSuffix=core.windows.net"
container_name = "data"


@app.route('/', methods=['post'])
def hello_world():
    data = json.loads(request.data)
    csv = pd.read_csv('data.csv')
    csv.loc[-1] = [data['email'], data['selected_video'], data['selected_speed']]
    output = csv.to_csv(encoding="utf-8")
    blobService = BlockBlobService(account_name=storage_account_name, account_key=storage_key)
    blobService.create_blob_from_text(container_name, 'data.csv', output)
    return {'status_code': 200, 'msg': 'done'}


if __name__ == '__main__':
    app.run()
