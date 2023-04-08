# does stuff
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  refreshonly => true,
}

package { 'nginx':
  ensure => installed,
  require => Exec['apt_update'],
}

file { '/var/www/html':
  ensure => directory,
}

exec { 'change_owner':
  command => "chown -R ${::id} /etc/nginx /var/www/html",
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure => present,
  content => "Hello World!\n",
  require => Exec['change_owner'],
}

exec { 'add_header':
  command => "sed -i 's/# server_tokens off;/&\n\tadd_header X-Served-By $hostname;/' /etc/nginx/nginx.conf",
  unless => "grep -q 'add_header X-Served-By' /etc/nginx/nginx.conf",
  require => Package['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Exec['add_header'],
}
