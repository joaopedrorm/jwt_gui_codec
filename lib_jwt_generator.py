#!/usr/bin/env python

import json
import jwt
import datetime

def encode_jwt_RS256(body, put_iat_exp, exp_delta, private_key_file_name):
    payload = json.loads(body)
    if put_iat_exp:
        payload['iat'] = datetime.datetime.utcnow()
        payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=exp_delta)
    private_key = open(private_key_file_name,"rb").read()
    return jwt.encode(payload, private_key, algorithm='RS256')

def decode_jwt_RS256(token, public_key_file_name):
    public_key = open(public_key_file_name,"rb").read()
    body = jwt.decode(token, public_key, algorithms='RS256')
    return json.dumps(body, indent=4)

def decode_Jwt_RS256_no_validation(token, public_key_file_name):
    public_key = open(public_key_file_name,"rb").read()
    body = jwt.decode(token, public_key, algorithms='RS256', verify=False)
    return json.dumps(body, indent=4)
