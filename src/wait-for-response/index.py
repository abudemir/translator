import json
import logging

from src.output_formatter import get_success_output, get_error_output

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


"""
Write your code here.
"""
def handler(event, context):
    logger.info("Context enabled Echo invocable")
    try:
        body = json.loads(event)['body']
        context = json.loads(event).get('context', {})
        flow_execution_id = context.get('flow_execution_id', None)
        if not flow_execution_id:
            return get_error_output(400, "Flow Execution ID (flow_execution_id) not specified in context")
        return get_success_output(200, body)
    except:
        return get_error_output(500, "Dummy error message", "Internal Server Error")
