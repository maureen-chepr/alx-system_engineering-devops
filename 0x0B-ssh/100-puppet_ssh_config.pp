# 100-puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "Host*
              IdentityFile ~/.ssh/school
              PasswordAuthentication no",
}
