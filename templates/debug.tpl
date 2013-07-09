<h2>plugins: {{len(set(reduce(lambda x,y:x+y, [diamond[s].keys() for s in diamond.keys()])))}}, paths: {{len(reduce(lambda x,y:x+y, [p.keys() for p in data.values()]))}}, metrics: {{len(metrics)}}</h2>
<h2>details</h2>
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
