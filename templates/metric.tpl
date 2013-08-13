%import config
% if targets:
<div class = 'graph-row'>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'day' src = '{{config.graphite_url}}/render/?width=600&height=400&{{targets}}&&title={{title}} - day' />
            </td>
            <td>
                <img class = 'week' src = '{{config.graphite_url}}/render/?width=600&height=400&{{targets}}&from=-7d&title={{title}} - week' />
            </td>
        </tr>
        <tr>
            <td>
                <img class = 'month' src = '{{config.graphite_url}}/render/?width=600&height=400&{{targets}}&from=-30d&title={{title}} - month' />
            </td>
            <td>
                <img class = 'year' src = '{{config.graphite_url}}/render/?width=600&height=400&{{targets}}&from=-365d&title={{title}} - year' />
            </td>
        </tr>
    </table>
</div>
% end
