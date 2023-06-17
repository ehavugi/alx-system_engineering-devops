#Fix Open Files limits for user holberton
exec{'holberton':
    command => "sed -i 's/www-data/#www-data/' /etc/security/limits.conf",
    path    => [ '/usr/bin', '/bin/', '/usr/sbin'],
}
