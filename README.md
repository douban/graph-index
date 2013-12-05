# Graph Index
index of diamond

 * support regex search
 * some pre-defined dashboard
 * easily hack and a few lines of code

# Screenshot

![Screenshot](https://raw.github.com/douban/graph-index/master/static/image/graph-index.png)
![Screenshot](https://raw.github.com/douban/graph-index/master/static/image/graph-index-server.png)
![Screenshot](https://raw.github.com/douban/graph-index/master/static/image/graph-index-plugin.png)

#Running

```shell
git clone https://github.com/huoxy/graph-index.git
cd graph-index
./graph-index.py
```
# Grammar

`regex` will draw a graph for each metric, for example: `servers.[^\.]+.loadavg.01$`

`plugin:server:regex` will display a graph with all metrics on `hostname`,for example: `plugin:cpu:hostname`

`merge:regex` will merge matched metrics in a single graph, for example: `merge:.*loadavg\.01$`

`group\s*by\s*\-?\d+` will draw multiple graphs group by the `\-?\d+`-th field, for example: `loadavg\.01$ groupby1`
