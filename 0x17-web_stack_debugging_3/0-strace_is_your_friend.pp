# replacing the content wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub("class-wp-locale.phpp", "class-wp-locale.php") %>'),
}

# restart apache
exec { 'restart-apache':
  command     => 'initctl restart apache2',
  path        => '/sbin:/usr/sbin:/bin',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
