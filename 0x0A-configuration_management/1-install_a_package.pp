# install flask using pip3
exec {'install_flask2.1.0':
command => '/usr/bin/pip3 install flask==2.1.0',
path    => '/usr/local/bin:/usr/bin:/bin',
}
