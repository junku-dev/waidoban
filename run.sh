curr=$(pwd)
dir=venv/
target="${curr}/${dir}"

if [ ! -d "$target" ]; then
    mkdir venv
    python3 -m venv venv/
fi

source venv/bin/activate
python3 main.py