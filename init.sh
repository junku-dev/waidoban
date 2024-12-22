curr=$(pwd)
file="done.txt"
file_path="${curr}/${file}"

echo "==================================================================================================================="
echo "this is a script that will attempt to install all dependencies."
echo "by continuing you are giving this script permissions to make changes to your machine."
echo "if you wish to see what is being installed and how, open 'init.sh' with your preffered text editor."
echo "proceed at your own risk."
echo ""
echo "supported distros:"
echo "DEBIAN; UBUNTU; MINT; POP; ARCH; FEDORA;"
echo "==================================================================================================================="
echo ""
read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

echo ""

if [ -f "$file_path" ]; then
    echo "init has already been completed..."
    read -p "install again? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
fi

echo "installing dependencies"
sudo apt update && sudo apt upgrade && sudo apt install python3 && sudo apt install python3-pip && sudo apt install ghostscript && sudo apt install qpdf || sudo pacman -Syu && sudo pacman -S python && sudo pacman -S python-pip && sudo pacman -S ghostscript && sudo pacman -S qpdf ||sudo dnf clean all && sudo sudo dnf update -y && sudo dnf groupinstall "Development Tools" -y && sudo dnf install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel -y ||sudo dnf install python3 && sudo sudo dnf install python3-pip && sudo sudo dnf install ghostscript && sudo sudo dnf install qpdf || echo "distro not supported or all dependencies are already installed. if this is a mistake then install manually..." && exit 1

dir=venv/
target="${curr}/${dir}"
if [ ! -d "$target" ]; then
    echo ""
    echo "creating venv and installing python dependencies..."
    mkdir venv
    python3 -m venv venv/ || python -m venv venv/
    source venv/bin/activate
    pip3 install PyPDF2 || pip install PyPDF2

    deactivate
fi

touch done.txt
chmod +x run.sh
echo ""
echo "run.sh is now executable."
echo "complete."
echo "enter './run.sh' or 'python3 main.py' or 'pip3 main.py' in a venv"