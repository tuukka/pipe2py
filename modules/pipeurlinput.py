# pipeurlinput.py
#

from pipe2py import util
import urllib2

def pipe_urlinput(context, _INPUT, conf, **kwargs):
    """This source prompts the user for a url and yields it forever.
    
    Keyword arguments:
    context -- pipeline context
    _INPUT -- not used
    conf:
        name -- input parameter name
        default -- default
        prompt -- prompt
    
    Yields (_OUTPUT):
    url
    """
    value = util.get_input(context, conf)
        
    #Ensure url is valid
    value = urllib2.quote(value, safe="%/:=&?~#+!$,;'@()*[]")
        
    while True:
        yield value

