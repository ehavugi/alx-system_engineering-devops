# Set IdentityFile and ensure no password

Exec {
  path => '/bin:/usr/bin:/usr/local/bin',
}

exec { 'set IdentityFile':
  command => '/bin/echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  unless  => '/bin/grep -q "^IdentityFile ~/.ssh/school" /etc/ssh/ssh_config',
}

exec { 'disable password authentication':
command => "sed -i 's/^.*PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/ssh_config",
}


# Ensure the values are set if sed does not match
file { '/root/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
}
