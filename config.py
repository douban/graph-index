graphite_url = 'http://graphite.intra.douban.com'
graphite_index_url = graphite_url + '/metrics/index.json'
metrics_file = 'metrics.json'
debug = True
listen_host = '0.0.0.0'
listen_port = 8808
try:
    from local_config import *
except:
    pass
