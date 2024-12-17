curr=$(pwd)
file="done.txt"
file_path="${curr}/${file}"

echo "this is a script that will attempt to install all dependencies."
echo "proceed at your own risk."

read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

echo ""

if [ -f "$file_path" ]; then
    echo "init has already been completed..."
    read -p "install again? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
fi

echo ""
echo "installing ghostscript & qpdf..."
sudo apt install ghostscript
sudo apt install qpdf

dir=venv/
target="${curr}/${dir}"
if [ ! -d "$target" ]; then
    echo ""
    echo "creating venv and installing python dependencies..."
    mkdir venv
    python3 -m venv venv/
    source venv/bin/activate
    pip3 install PyPDF2

    deactivate
fi

touch done.txt
chmod +x run.sh
echo ""
echo "complete."
echo "enter './run.sh' or 'python3 main.py' or 'pip3 main.py' in a venv"