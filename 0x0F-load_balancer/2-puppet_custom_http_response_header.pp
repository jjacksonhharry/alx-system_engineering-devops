# script that creates a custom HTTP header response with puppet.

# Update the package list:
exec {'update':
  command => '/usr/bin/apt-get update',
}

# Install HAProxy
-> package {'nginx':
  ensure => 'present',
}

# Custom Header Configuration
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

# Restarting Nginx:
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
