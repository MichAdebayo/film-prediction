sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update


#Installez Python 3.11 et les packages nécessaires
sudo apt install python3.11 python3.11-venv python3.11-distutils

#Venv
python3.11 -m venv .venv_py311

source .venv_py311/bin/activate

pip install --upgrade pip setuptools wheel

#Installer dépendences
pip install -r requirements.txt
