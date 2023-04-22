# execute a kill command
exec{'kill_process':
command => '/usr/bin/pkill killmenow',
onlyif  => '/usr/bin/pgrep killmenow',
}
