""" Run the public API """
import api.flask_app as api

if __name__ == '__main__':
    api.rest_api.run(host='0.0.0.0', threaded=True, port=8090, debug=True)