# Install Nginx web server using Puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

exec { 'configure-nginx-redirect':
  command     => "sed -i 's@listen 80 default_server;@listen 80 default_server;\\n\\tlocation /redirect_me {\\n\\t\\treturn 301 https://github.com/maureen-chepr;\\n\\t}@' /etc/nginx/sites-available/default",
  path        => '/usr/bin',
  refreshonly => true,
  notify      => Service['nginx'],
}
