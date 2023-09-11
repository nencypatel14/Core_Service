import json
import logging
from fastapi.responses import JSONResponse
from os import path

def success_response(data, message="success", meta_code=200, **extra):
    res = {
        "data": data,
        "meta": {
            "message": message,
            "code": meta_code,
            **extra
        }
    }
    return res

def error_response(message, meta_data=400, status_code=200, data=None):
    if data is None:
        data = dict()
    res = {
        "data": data,
        "meta": {
            "message": message,
            "code": meta_data,
        }
    }
    return JSONResponse(
        res,
        status_code=status_code
    )