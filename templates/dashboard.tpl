%setdefault('plugins', [])
%from urllib import urlencode
% for p in plugins:
    <h1 class = 'dashboard-url'><a href = '/regex/?{{urlencode({'search':p+':'+'.*'})}}'>{{p}}</a></h1>
% 
