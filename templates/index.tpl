% setdefault('examples', [])
% from urllib import urlencode
<div id = 'sidebar' class = 'well span5'>
    <span class = 'nav-header'>examples</span>
    <ul class = 'nav nav-list'>
    % for query in examples:
        <li><a href = '/regex/?{{urlencode({'search':query})}}'>{{query}}</a></li>
    % end
        <li class = 'divider' />
    </ul>
    <ul class = 'nav nav-list'>
        <li><span class = 'nav-header'>grammar</span></li>
        <li><span class = 'grammar'>&lt;regex&gt;</span></li>
        <li><span class = 'grammar'>&lt;regex&gt; group by &lt;index&gt;</span></li>
        <li><span class = 'grammar'>plugin:&lt;plugin_name&gt;:&lt;server_prefix&gt;</span></li>
        <li><span class = 'grammar'>merge:&lt;regex&gt;</span></li>
        <li class = 'divider' />
    </ul>
    <ul class = 'nav nav-list'>
        <li>
            <span class = 'nav-header'>help</span>
            <p>
                goto <a href = '/debug'><strong>/debug</strong></a> to see more details about each plugin 
            </p>
        </li>
        <li class = 'divider' />
        <li><a href = 'https://github.com/huoxy/graph-index'>fork me</a></li>
    </ul>
</div>
<div id = 'index' class = 'span10'>
    <div class = 'row'>
        <div class = 'float-left'>
            <ul>
            % for server in sorted(diamond.keys()):
                <li><a href = '/server/{{server}}'>{{server}}</a>
                    <div class = 'plugins'>
                    % for plugin in sorted(diamond[server].keys()):
                        <span class = 'plugin'><a href = '{{'server/' + server + '/' + plugin}}'>{{plugin}}</a></span>
                    % end
                    </div>
                </li>
            % end
            </ul>
        </div>
    </div>
</div>
