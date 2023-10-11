from fastapi.responses import JSONResponse

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

def error_response(message, meta_data=400, status_code=400, data=None):
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
