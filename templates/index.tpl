<div id = 'index'>
    <ul>
    % for s in sorted(diamond.keys()):
        <li>{{s}}
            <ul>
            % for p in sorted(diamond[s].keys()):
                <li class = 'plugin'>{{p}}</li>
            % end
            </ul>
        </li>
    % end
    </ul>
</div>
