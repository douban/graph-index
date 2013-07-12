%import config
% if m:
<div class = 'graph-row'>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'day' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&&title={{m}} - day' />
            </td>
            <td>
                <img class = 'week' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-7d&title={{m}} - week' />
            </td>
        </tr>
        <tr>
            <td>
                <img class = 'month' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-30d&title={{m}} - month' />
            </td>
            <td>
                <img class = 'year' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-365d&title={{m}} - year' />
            </td>
        </tr>
    </table>
</div>
% end
