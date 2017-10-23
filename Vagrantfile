# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "dokku.me"
  config.vm.network "private_network", ip: "192.168.20.160"


  config.vm.provision "shell", inline: <<-SHELL
    wget https://raw.githubusercontent.com/dokku/dokku/v0.10.5/bootstrap.sh
    sudo DOKKU_TAG=v0.10.5 bash bootstrap.sh
  SHELL
end
