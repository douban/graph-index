import config

class Graph:
    def __init__(self, **kwargs):
        assert(kwargs.has_key('targets'))
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.base_url = config.graphite_url + '/render/?%s' % \
            ('&'.join('target=%s' % t for t in self.targets))
        self.graph_args = {
            'width' : 600,
            'height' : 400,
            'from' : '-1d',
            'hideLegend' : 'False',
        }

    @property
    def full_url(self, **graph_args):
        self.graph_args.update(graph_args)
        return self.base_url + '&' + '&'.join('%s=%s' % (k, v) \
                for k, v in self.graph_args.items())
        
