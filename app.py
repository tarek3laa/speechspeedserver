from flask import Flask, request, json
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['post'])
def hello_world():
    data = json.loads(request.data)
    csv = pd.read_csv('data.csv')
    csv.loc[-1] = [data['email'], data['selected_video'], data['selected_speed']]
    csv.to_csv('data.csv', index=False)
    return {'status_code': 200}


if __name__ == '__main__':
    app.run()
