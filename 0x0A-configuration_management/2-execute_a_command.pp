# a script to kill a process

exec { 'pkill':
  command     => 'pkill killmenow',
  path        => '/usr/bin:/usr/local/bin',
  refreshonly => true,
}
