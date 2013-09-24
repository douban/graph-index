import config

class Graph:
    def __init__(self, **kwargs):
        assert(kwargs.has_key('targets'))
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.base_url = config.graphite_url + '/render/?%s' % \
            ('&'.join('target=%s' % t for t in self.targets))
