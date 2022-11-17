import simple_response
import numpy

def handler(event, context):
    return simple_response.generate('events :get');
