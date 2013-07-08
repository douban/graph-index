%setdefault('data', None)
% if data:
    % for plugin in sorted(data.keys()):
        <ul>{{plugin}}
            <ul>
            % for path in sorted(data[plugin]):
                <li>{{path}}</li>
            % end
            </ul>
        </ul>
    % end
% end
