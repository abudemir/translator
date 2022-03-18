import json
import logging
import boto3

from src.output_formatter import get_success_output, get_error_output

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(event, _):
    logger.info("Echo invocable")
    args = json.loads(event)["body"]

    try:
        tl = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
        logger.info("Translation client creation is a success!")
        text=args["text"]
        src_language = args["SourceLanguageCode"]
        target_language = args["TargetLanguageCode"]

        tl_text = tl.translate_text(Text=text, 
            SourceLanguageCode=src_language, TargetLanguageCode=target_language)
        logger.info("Translation complete for one single text")

        response = {"TranslatedText":tl_text,"SourceLanguageCode":src_language,"TargetLanguageCode":target_language}
        
        return get_success_output(status_code=200, body=json.dumps(response))
    except KeyError:    
        return get_error_output(400,"Missing Arguments","Invalid Request Error")
    except:
        return get_error_output(500, "Dummy error message", "Internal Server Error")
