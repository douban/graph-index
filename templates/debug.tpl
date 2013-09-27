<h2>plugins: {{plugins_num}}, metrics: {{metrics_num}}</h2>
<h2>details</h2>
% for plugin in sorted(plugins.keys()):
<ul>{{plugin}}
    <ul>
    % for path in sorted(plugins[plugin]):
        <li>{{path}}</li>
    % end
    </ul>
</ul>
% end
