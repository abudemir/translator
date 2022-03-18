import json
import traceback


def get_success_output(status_code, body):
    if type(body) != str:
        body = json.dumps(body)
    return {
        'statusCode': status_code,
        'body': body
    }


def get_error_output(status_code, error_message=None, error_type=None):
    return {
        'statusCode': status_code,
        'body': json.dumps({
            'errorMessage': error_message,
            'errorType': error_type,
            'stackTrace': traceback.format_exc()
        })
    }
