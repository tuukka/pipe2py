# pipefetch.py
#

import feedparser
from pipe2py import util

def pipe_fetch(context, _INPUT, conf, **kwargs):
    """This source fetches and parses one or more feeds to yield the feed entries.
    
    Keyword arguments:
    context -- pipeline context       
    _INPUT -- not used
    conf:
        URL -- url
    
    Yields (_OUTPUT):
    feed entries
    """
    url = conf['URL']
    
    if not isinstance(url, list):
        url = [url]
    
    for item in url:
        value = util.get_value(item, item, **kwargs)
        
        if not '://' in value:
            value = 'http://' + value
        
        if context.verbose:
            print "pipe_fetch loading:", value
        d = feedparser.parse(value.encode('utf-8'))
        
        for entry in d['entries']:
            if 'updated_parsed' in entry:
                entry['pubDate'] = entry['updated_parsed']  #map from universal feedparser's normalised names
                entry['y:published'] = entry['updated_parsed']  #yahoo's own version
            if 'author' in entry:
                entry['dc:creator'] = entry['author']
            if 'author_detail' in entry:
                if 'href' in entry['author_detail']:
                    entry['author.uri'] = entry['author_detail']['href']
                if 'name' in entry['author_detail']:
                    entry['author.name'] = entry['author_detail']['name']
            #todo more!?
            if 'title' in entry:
                entry['y:title'] = entry['title']  #yahoo's own versions
            if 'id' in entry:
                entry['y:id'] = entry['id']  #yahoo's own versions
            #todo more!?
            yield entry

