%setdefault('plugins', {})
%from urllib import urlencode
% for plugin in sorted(plugins.keys()):
<div class = 'dashboard-box'>
    % for prefix in sorted(plugins[plugin].keys()):
    <span class = 'dashboard-url'><a href = '/regex/?{{urlencode({'search':plugin+':'+prefix})}}'>{{plugin}}:{{prefix}}</a></span>
    % end
</div>
% end
