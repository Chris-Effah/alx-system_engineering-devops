exec { 'fix--for-nginx-ulimit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => '/bin/grep -q "15" /etc/default/nginx', # Ensures the change is needed
  notify  => Exec['nginx-restart'], # Triggers Nginx restart if changes are applied
}

exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true, # Ensures restart only if triggered by other resources
  subscribe   => Exec['fix--for-nginx-ulimit'], # Listens for changes to trigger restart
}
}
