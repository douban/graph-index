graphite_url = 'http://graphite.intra.douban.com'
graphite_index_url = graphite_url + '/metrics/index_all.json'
graph_height = {
    'iostat' : 800,
    'network' : 500,
}
metrics_file = 'metrics.json'
debug = True
listen_host = '0.0.0.0'
listen_port = 8808
try:
    from local_config import *
except:
    pass
