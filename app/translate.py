import requests, uuid, json
from flask import current_app 
from flask_babel import _ 

def translate(text, source_language, dest_language):
    
    if "MS_TRANSLATOR_KEY" not in current_app.config or \
            not current_app.config["MS_TRANSLATOR_KEY"]:
        return _("Error: the translation service is not configured.")
    subscription_key = current_app.config['MS_TRANSLATOR_KEY']
    endpoint = "https://api.cognitive.microsofttranslator.com"
    location = "westus2"
    path = '/translate'
    constructed_url = endpoint + path
    params = {
        'api-version': '3.0',
        'from': source_language,
        'to': dest_language
    }
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        'text': text
    }]

    r = requests.post(constructed_url, params=params, headers=headers, json=body)
    if r.status_code != 200:
        return _("Error: the translation service has failed")
    
    return r.json()[0]["translations"][0]["text"]