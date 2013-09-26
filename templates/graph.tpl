<div class = 'graph-row'>
    <table class = 'graph'>
        <tr>
            <td> <img class = '{{graph.auto_refresh and "day" or ""}}' src = '{{graph.day_graph_need_shift and graph.shift_url or graph.day_url}}' /> </td>
            <td> <img class = 'week' src = '{{graph.week_url}}' /> </td>
        </tr>
        <tr>
            <td> <img class = 'month' src = '{{graph.month_url}}' /> </td>
            <td> <img class = 'year' src = '{{graph.year_url}}' /> </td>
        </tr>
    </table>
</div>
