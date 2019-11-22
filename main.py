#!/usr/bin/env python3

#
#
# RestAPI 
#
#

import os
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

var1 = os.environ['env_var1']
var2 = os.environ['env_var2']
mysql_username = os.environ['mysql_username']
mysql_password = os.environ['mysql_password']
mysql_host = os.environ['mysql_host']

# Routes
@app.route('/', methods=['GET'])
def get_root_page():
    return jsonify({'message': 'You reached a public page!', 
                    'var1': var1,
                    'var2': var2,
                    'mysql': {
                            'mysql_username': mysql_username,
                            'mysql_password': mysql_password,
                            'mysql_host': mysql_host,
                            }
                    })


# Initialize main app
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080', debug=True)
