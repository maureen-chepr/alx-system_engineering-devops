# using puppet to kill a process

exec { 'killmenow_process':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
  path    => ['/usr/bin'],
}
