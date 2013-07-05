<div id = 'index'>
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
