%setdefault('plugins', {})
%from urllib import urlencode
% for plugin in sorted(plugins.keys()):
<div class = 'dashboard-box'>
    <h2><span class = 'badge badge-info'>{{plugin}}</span></h2>
    % for prefix in sorted(plugins[plugin].keys()):
    <span class = 'dashboard-url'><a href = '/regex/?{{urlencode({'search':plugin+':'+prefix})}}'>{{plugin}}:{{prefix}}</a></span>
    % end
</div>
% end
