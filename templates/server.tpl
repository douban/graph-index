%setdefault('data', None)
%import config
% if data:
    % for p in sorted(data.keys()):
        % target = '&'.join('target=' + m for m in data[p])
<div class = 'graph-row'>
    <h4><a href = '/server/{{server}}/{{p}}'>{{p}}</a></h4>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'day-graph' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&&title={{p}} - day' />
            </td>
            <td>
                <img src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-7d&title={{p}} - week' />
            </td>
        </tr>
    </table>
</div>
    % end
% end
