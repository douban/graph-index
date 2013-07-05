%import config
% if m:
<div class = 'graph-row'>
    <div class = 'graph'>
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&&title={{m}} - day' />
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-7d&title={{m}} - week' />
    </div>
</div>
<div class = 'graph-row'>
    <div class = 'graph'>
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-30d&title={{m}} - month' />
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-365d&title={{m}} - year' />
    </div>
</div>
% end
