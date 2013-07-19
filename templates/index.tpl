% setdefault('suggested_queries', [])
% from urllib import urlencode
<div id = 'sidebar' class = 'well span4'>
    <span class = 'nav-header'>suggested queries</span>
    <ul class = 'nav nav-list'>
    % for q in suggested_queries:
        <li><a href = '/regex/?{{urlencode({'search':q})}}'>{{q}}</a></li>
    % end
        <li class = 'divider' />
    </ul>
    <ul class = 'nav nav-list'>
        <li>
            <span class = 'nav-header'>help</span>
            <p>
                goto <a href = '/debug'><strong>/debug</strong></a> to see more details about each plugin 
            </p>
        </li>
    </ul>
</div>
<div id = 'index' class = 'span10'>
    <div class = 'row'>
        <div class = 'float-left'>
            <ul>
            % for s in sorted(diamond.keys()):
                <li><a href = '/server/{{s}}'>{{s}}</a>
                    <div class = 'plugins'>
                    % for p in sorted(diamond[s].keys()):
                        <span class = 'plugin'><a href = '{{'server/' + s + '/' + p}}'>{{p}}</a></span>
                    % end
                    </div>
                </li>
            % end
            </ul>
        </div>
    </div>
</div>
