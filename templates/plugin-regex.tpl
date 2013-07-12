%setdefault('data', None)
%import config
% if data:
    % for s in sorted(data.keys()):
        % target = '&'.join('target=' + m for m in data[s])
<div class = 'graph-row'>
    <h4><a href = '/server/{{s}}/{{plugin}}'>{{s}} / {{plugin}}</a></h4>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'day' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&&title={{s}} -{{plugin}} - day' />
            </td>
            <td>
                <img class = 'week' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-7d&title={{s}} - {{plugin}} - week' />
            </td>
        </tr>
    </table>
</div>
    % end
% end
