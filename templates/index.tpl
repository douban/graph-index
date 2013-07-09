<div id = 'index'>
    <div class = 'row'>
        <div class = 'row alert alert-info span4'>
            more details of each plugin in  <a href = '/debug'><strong>/debug</strong></a>
        </div>
    </div>
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
