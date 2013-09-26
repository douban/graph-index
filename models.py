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
        self.title = self.graph_args['title'] # self.title origin title passed by kwargs
        self.base_url = config.graphite_url + '/render/?%s' % \
            ('&'.join('target=%s' % t for t in self.targets))
        self.detail_url = None
        self.day_graph_need_shift = False
        self.auto_refresh = False

    def full_url(self, **kwargs):
        graph_args = self.graph_args.copy()
        graph_args.update(kwargs)
        if graph_args.has_key('_from'):
            graph_args['from'] = graph_args['_from']
            del graph_args['_from']
        graph_args['height'] += len(self.targets) > 10 and len(self.targets) * 12 or 0
        return self.base_url + '&' + '&'.join('%s=%s' % (k, v) \
                for k, v in graph_args.items())

    @property
    def day_url(self):
        return self.full_url(title = self.title + ' - day')

    @property
    def week_url(self):
        return self.full_url(title = self.title + ' - week',  _from = '-7d')

    @property
    def month_url(self):
        return self.full_url(title = self.title + ' - month',  _from = '-30d')

    @property
    def year_url(self):
        return self.full_url(title = self.title + ' - year', _from = '-365d')

    @property
    def shift_url(self, shift = '7d'):
        assert(len(self.targets) == 1)
        return self.full_url() + '&target=alias(dashed(timeShift(%s,"%s")),"%s ago")' % \
            (self.targets[0], shift, shift)
        
