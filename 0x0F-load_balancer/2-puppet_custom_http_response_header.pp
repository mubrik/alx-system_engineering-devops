# does stuff
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/':
  ensure => 'directory',
  before => Service['nginx']
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => File['/var/www/html/']
}

file { '/etc/nginx/conf.d/custom_headers.conf':
  content => "add_header X-Served-By $hostname;\n",
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}