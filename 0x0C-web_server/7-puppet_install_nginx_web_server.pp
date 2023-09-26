# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create a custom index.html file with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],  # Make sure Nginx is installed first
}

# Configure a 301 redirect for /redirect_me
file { '/etc/nginx/sites-available/redirect':
  ensure  => 'file',
  content => 'server {
    listen 80;
    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/;
    }

    location / {
        root /var/www/html;
    }
}',
  require => Package['nginx'],  # Make sure Nginx is installed first
}

# Create a symbolic link to enable the redirect configuration
file { '/etc/nginx/sites-enabled/redirect':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/redirect',
  require => File['/etc/nginx/sites-available/redirect'],  # Ensure the file exists before creating a link
}

# Restart Nginx to apply the configuration changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/redirect'],  # Restart when the configuration changes
}
