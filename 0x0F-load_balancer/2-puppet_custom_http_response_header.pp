# does some stuff
class http_header::nginx {
  package { 'nginx':
    ensure => installed,
  }
}

class http_header::nginx_config {
  file { '/etc/nginx/conf.d/custom_headers.conf':
    content => "add_header X-Served-By $hostname;\n",
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
  }
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}

class http_header {
  include http_header::nginx
  include http_header::nginx_config
}
