import config

class Graph:

    def __init__(self, targets, **kwargs):
        assert(isinstance(targets, list))
        self.targets = targets
        self.graph_args = dict( width = 600, height = 400, \
            _from = '-1d', hideLegend = 'False', )
        self.graph_args.update(kwargs)
        if not self.graph_args.has_key('title'): # self.graph_args['title'] stores the real title
            self.graph_args['title'] = ','.join(self.targets)
        self.origin_title = self.graph_args['title'] # self.origin_title origin title passed by kwargs

    @property
    def base_url(self):
        return config.graphite_url + '/render/?%s' % \
            ('&'.join('target=%s' % t for t in self.targets))

    def full_url(self, **graph_args):
        self.graph_args.update(graph_args)
        if graph_args.has_key('_from'):
            self.graph_args['from'] = graph_args['_from']
            del self.graph_args['_from']
        return self.base_url + '&' + '&'.join('%s=%s' % (k, v) \
                for k, v in self.graph_args.items())

    @property
    def day_url(self):
        return self.full_url(title = self.origin_title + ' - day')

    @property
    def week_url(self):
        return self.full_url(title = self.origin_title + ' - week',  _from = '-7d')

    @property
    def month_url(self):
        return self.full_url(title = self.origin_title + ' - month',  _from = '-30d')

    @property
    def year_url(self):
        return self.full_url(title = self.origin_title + ' - year', _from = '-365d')

    @property
    def shift_url(self, shift = '7d'):
        assert(len(self.targets) == 1)
        return self.full_url() + '&target=alias(dashed(timeShift(%s,"%s")),"%s ago")' % \
            (self.targets[0], shift, shift)
        
    def tune_height(self, plugin):
        for k, v in config.graph_height.items():
            if k in plugin:
                self.graph_args['height'] = v
