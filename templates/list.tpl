% for graph in graphs:
<div class = 'graph-row'>
    <h4><a href = '/metric/{{graph.targets[0]}}'>{{graph.targets[0]}}</a></h4>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'day' src = '{{graph.shift_url}}' />
            </td>
            <td>
                <img class = 'week' src = '{{graph.week_url}}' />
            </td>
        </tr>
    </table>
</div>
% end
