import json
import logging

from src.output_formatter import get_success_output, get_error_output

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



def handler(event, _):
    logger.info("Echo invocable")
    args = json.loads(event)["body"]
    try:
        request_id=args["request_id"]
        return get_success_output_nonblocking(status_code=200, request_id=request_id,body=json.dumps(args))
    except KeyError:
        return get_error_output(400,"Missing Arguments","Invalid Request Error")
    except:
        return get_error_output(500, "Dummy error message", "Internal Server Error")
