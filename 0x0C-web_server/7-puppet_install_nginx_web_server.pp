# Install Nginx web server w/ Puppet

exec {'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package {'apache2.2-common':
  ensure  => 'absent',
  require => Exec['apt-get-update'],
}

package { 'nginx':
  ensure  => 'installed',
  require => Package['apache2.2-common'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Hello World!',
  require => Package['nginx'],
}

file_line { 'perform a redirection':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  line    => 'rewrite ^/redirect_me/$ https://github.com/maureen-chepr permanent;',
  after   => 'root /var/www/html;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service {'nginx':
  ensure  => 'running',
  require => File_line['perform a redirection'],
  subscribe => File['/etc/nginx/sites-enabled/default'],
}