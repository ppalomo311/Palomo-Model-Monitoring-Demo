# installing older versions of sklearn
export SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True

# configure git client
git config --global user.name ${GIT_USERNAME}
git config --global user.email ${GIT_EMAIL}

# system dependencies
sudo apt-get update
sudo apt-get -y install --no-install-recommends awscli
sudo apt-get install git-lfs

# install requirements.txt
pip install --upgrade pip
python -m pip install --user -r /workspace/.devcontainer/requirements.txt

# install https://github.com/Smarsh/label-studio-data-uploader
# pip install git+https://github.com/Smarsh/label-studio-data-uploader.git
# pip install git+https://github.com/Smarsh/decsurver.git
export GIT_CLONE_PROTECTION_ACTIVE=false && pip install git+https://github.com/Smarsh/conduct_dswb.git