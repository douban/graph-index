%setdefault('data', None)
%import config
% if data:
    % target = '&'.join('target=' + m for m in data)
<div class = 'graph-row'>
    <div class = 'graph'>
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&&title={{plugin}} - day' />
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-7d&title={{plugin}} - week' />
    </div>
    <div class = 'graph'>
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-30d&title={{plugin}} - month' />
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-365d&title={{plugin}} - year' />
    </div>
</div>
% end
