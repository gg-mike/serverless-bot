import simple_response

def handler(event, context):
    return simple_response.generate('events :delete');
