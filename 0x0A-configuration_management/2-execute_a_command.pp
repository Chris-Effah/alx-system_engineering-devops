# a script to kill a process

exec { 'kill_killmenow':
  command     => 'pkill4 killmenow',
  path        => '/usr/bin:/usr/local/bin',
  refreshonly => true,
}
