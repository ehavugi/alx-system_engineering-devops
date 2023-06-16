#Fix Open Files limits for user holberton
exec{'holberton':
    command => "sed -i 's/holberton/#holberton/' /etc/security/limits.conf",
    path    => [ '/usr/bin', '/bin/', '/usr/sbin'],
}