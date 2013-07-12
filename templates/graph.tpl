%setdefault('matched_metrics', None)
%import config
% if matched_metrics:
% for m in matched_metrics:
<div class = 'graph-row'>
    <h4><a href = '/metric/{{m}}'>{{m}}</a></h4>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'day' src = '{{config.graphite_url}}/render/?width=600&height=400&target=alias({{m}},"12 hours ago")&target=alias(dashed(timeShift({{m}},"7d")),"7 days ago")&title={{m}}&from=-12h' />
            </td>
            <td>
                <img class = 'week' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-7d&title={{m}} - week' />
            </td>
        </tr>
    </table>
</div>
% end
% end
