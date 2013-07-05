%setdefault('matched_metrics', None)
%import config
% if matched_metrics:
% for m in matched_metrics:
<div class = 'graph-row'>
    <div class = 'graph'>
        <h4>{{m}}</h4>
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&&title={{m}} - day' />
        <img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-7d&title={{m}} - week' />
    </div>
</div>
% end
% end
