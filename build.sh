if [ ! -f "env/bin/python" ]; then
	python3 -m venv env
	./env/bin/pip install -r requirements.txt
fi

./env/bin/pelican ./content -o ./output -s pelicanconf.py
