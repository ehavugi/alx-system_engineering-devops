#Fix 500 server error. change .phpp to .php
exec{'edit_file':
    command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
    onlyif  => '/usr/bin/pgrep -r /var/www/html/wp-settings.php',
    path    => [ '/usr/bin', '/bin/', '/usr/sbin'],
}
