
if ! grep -q virtualenvwrapper /home/vagrant/.bashrc; then
    sudo apt-get install -y virtualenvwrapper
    echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> /home/vagrant/.bashrc
    newgrp
    mkvirtualenv .django
    workon .django
    pip install django flask
    deactivate
fi