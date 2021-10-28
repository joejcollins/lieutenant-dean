"""  """
import os
from flask import Flask, Response, request, jsonify
import tasks as tasks
from tasks import slowly_reverse_string

PATH = './data'
public_api = Flask(__name__)
public_api.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tasks.slowly_reverse_string.s(url=request.json['url']).delay()
        return jsonify({'url': request.json['url']}), 201

    data = os.listdir(PATH) if os.path.exists(PATH) else []
    return jsonify(data) 


@app.route('/<string:slug>', methods=['GET', 'POST'])
def get(slug):
    with open(os.path.join(PATH, slug)) as f:
        return Response(f.read(), mimetype='text')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)