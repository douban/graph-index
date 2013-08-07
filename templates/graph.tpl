% setdefault('data', None)
% import config
% if data:
% for m in data:
<div class = 'graph-row'>
    <h4><a href = '/metric/{{m}}'>{{m}}</a></h4>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'graph day-graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target=alias({{m}},"today")&target=alias(dashed(timeShift({{m}},"7d")),"7 days ago")&title={{m}}&from=-1d&hideLegend=False' />
            </td>
            <td>
                <img class = 'week' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-7d&title={{m}} - week&hideLegend=False' />
            </td>
        </tr>
    </table>
</div>
% end
% end
