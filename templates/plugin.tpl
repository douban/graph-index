%setdefault('data', None)
%import config
% if data:
    % target = '&'.join('target=' + m for m in data)
<div class = 'graph-row'>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'day-graph' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&&title={{plugin}} - day' />
            </td>
            <td>
                <img src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-7d&title={{plugin}} - week' />
            </td>
        </tr>
        <tr>
            <td>
                <img src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-30d&title={{plugin}} - month' />
            </td>
            <td>
                <img src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-365d&title={{plugin}} - year' />
            </td>
        </tr>
    </table>
</div>
% end
