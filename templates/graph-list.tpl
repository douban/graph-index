% for graph in graphs:
<div class = 'graph-row'>
    <h4><a href = '{{graph.detail_url}}'>{{graph.detail_name or 'detail'}}</a></h4>
    <table class = 'graph'>
        <tr>
            <td> <img class = 'day' src = '{{graph.day_url}}' /> </td>
            <td> <img class = 'week' src = '{{graph.week_url}}' /> </td>
        </tr>
    </table>
</div>
% end
