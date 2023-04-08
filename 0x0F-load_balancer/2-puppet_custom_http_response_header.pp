# does stuff
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  refreshonly => true,
}

package { 'nginx':
  ensure => installed,
  require => Exec['apt_update'],
}

file { '/var/www':
  ensure => 'directory',
  owner  => $::id,
  group  => $::id,
  mode   => '0755',
}

file { '/var/www/html':
  ensure => 'directory',
  owner  => $::id,
  group  => $::id,
  mode   => '0755',
  require => File['/var/www'],
}

exec { 'change_owner':
  command => "/bin/chown -R ${::id} /etc/nginx /var/www/html",
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure => present,
  content => "Hello World!\n",
  require => Exec['change_owner'],
}

exec { 'add_header':
  command => "/bin/grep -q 'add_header X-Served-By' /etc/nginx/nginx.conf || sudo /bin/sed -i '/# server_tokens off;/ a        add_header X-Served-By $hostname;' /etc/nginx/nginx.conf",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Exec['add_header'],
}
