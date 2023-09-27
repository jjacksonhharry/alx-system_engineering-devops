# Puppet manifest to configure SSH client

# Add configuration lines to the SSH client configuration file
file_line { 'Use the private key':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '     IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Disable password authentication':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}
