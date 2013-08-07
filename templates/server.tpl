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
                <img class = 'day' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&&title={{server}} - {{p}} - day&hideLegend=False' />
            </td>
            <td>
                <img class = 'week' src = '{{config.graphite_url}}/render/?width=600&height=400&{{target}}&from=-7d&title={{server}} - {{p}} - week&hideLegend=False' />
            </td>
        </tr>
    </table>
</div>
    % end
% end
