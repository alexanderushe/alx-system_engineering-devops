# install flask using Puppet

package { 'install_flask':
  ensure   => '2.1.0',
  provider => 'gem',
}
