% for graph in graphs:
% server, plugin = graph.graph_args['title'].split()
<div class = 'graph-row'>
    <h4><a href = '/server/{{server}}/{{plugin}}'>details</a></h4>
    <table class = 'graph'>
        <tr>
            <td> <img class = 'day' src = '{{graph.day_url}}' /> </td>
            <td> <img class = 'week' src = '{{graph.week_url}}' /> </td>
        </tr>
    </table>
</div>
% end
