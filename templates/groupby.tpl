%setdefault('data', None)
%import config
% if data:
    % for group, metrics in data:
        % target = '&'.join('target=' + m for m in metrics)
        % metrics = ','.join(metrics)
<div class = 'graph-row'>
    <h4><a href = '/metrics/{{metrics}}?title={{group}}'>{{group}}</a></h4>
    <table class = 'graph'>
        <tr>
            <td>
                <img class = 'day' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&title={{group}} - day' />
            </td>
            <td>
                <img class = 'week' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-7d&title={{group}} - week' />
            </td>
        </tr>
    </table>
</div>
    % end
% end
