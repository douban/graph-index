% setdefault('errors', [])
<div id = 'error' class = 'alert alert-error span4'>
    <ul>
    % for e in errors:
        <li>{{e}}</li>
    % end
    </ul>
</div>
