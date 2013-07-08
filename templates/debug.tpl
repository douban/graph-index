%setdefault('data', None)
% if data:
    % for p in sorted(data.keys()):
        <ul>{{p}}
            <ul>
            % for path in sorted(data[p]):
                <li>{{path}}</li>
            % end
            </ul>
        </ul>
    % end
% end
