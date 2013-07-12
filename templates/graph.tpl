%setdefault('matched_metrics', None)
%import config
% if matched_metrics:
% for m in matched_metrics:
<div class = 'graph-row'>
    <h4><a href = '/metric/{{m}}'>{{m}}</a></h4>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'graph day-graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target=alias({{m}},"today")&target=alias(dashed(timeShift({{m}},"7d")),"7 days ago")&title={{m}}&from=-1d' />
            </td>
            <td>
                <img class = 'week' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-7d&title={{m}} - week' />
            </td>
        </tr>
    </table>
</div>
% end
% end
