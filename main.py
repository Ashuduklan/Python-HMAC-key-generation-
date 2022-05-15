from flask import Flask, jsonify, request
import base64
import json
import hashlib
import hmac
import binascii

app = Flask(__name__)

@app.route('/')
def helloworld():
    return jsonify({"message":"Hello, Successfully executed.","response":"Success"})

#This post request is used to encrypt the request into base64 format.
@app.route('/post/request', methods=['POST'])

def data_post():
    json_data = request.get_json(force=True)
    strng = json.dumps(json_data)
    encrypt = base64.b64encode(strng.encode('utf-8'))
    encrypted_str = str(encrypt, 'utf-8')
    rsponse_data = {
        "message":"Successfully encrypted",
        "response_msg":"SUCCESS",
        "response_code":"001",
        "encrypted_data":encrypted_str
    }

    return jsonify(rsponse_data)


# This methods it used to generate the key without facing an issue. 
@app.route('/generate/key/<string:key>,<string:msg>', methods=["POST"])

def signature(key, msg):
    key = binascii.unhexlify(key)
    msg = msg.encode()
    check_sum = hmac.new(key, msg, hashlib.sha256).hexdigest().upper()
    response_data = {
        "message":"Successfully generated",
        "response_msg":"SUCCESS",
        "response_code":"001",
        "Gnerated_key":check_sum
    }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)