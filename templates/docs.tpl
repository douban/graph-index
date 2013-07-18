<div class = 'row'>
    <div id = 'docs' class = 'span8'>
        <h2>Grammar</h2>
        <ul>
            <li><span class = 'grammar'>&lt;regex&gt;</span><br />
                draw a graph for each matched metric</li>
            <li><span class = 'grammar'>&lt;regex&gt; group by &lt;index&gt;</span><br />
                draw a graph for each <strong>group</strong> group by the index-th field of matched metrics
            <li><span class = 'grammar'>plugin:&lt;plugin_name&gt;:&lt;server_prefix&gt;</span><br />
                draw many groups of a list of servers, and combined metrics of a server in a single graph<br />
                <b>for example:</b> if we have servers: host1, host2, ... hostN, then the server_prefix will be "host"
            <li><span class = 'grammar'>merge:&lt;regex&gt;</span><br />
                draw a single graphs of all the matched metrics
        </ul>
        <h2>Suggested Queries</h2>
        <p>
            add more in suggested_queries.py
        </p>
    </div>
    <div id = 'about'>
            <h1><a href = 'https://github.com/huoxy/graph-index'><strong>fork me</strong></a> @ Github</h1>
            <h2><strong>thanks to:</strong></h2>
            <ul>
                <li>bottle</li>
                <li>bootstrap</li>
                <li>jquery</li>
            </ul>
            <h2><strong>todo:</strong></h2>
            <ul>
                <li>split one graph of a plugin to multiple graphs</li>
                <li>dynamicly update metrics.json and build related data structures</li>
                <li>zoom graph: select a period of time with mouse, then zoom in/out</li>
            </ul>
    </div>
</div>
