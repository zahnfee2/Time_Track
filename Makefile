run:
	python3 time_track.py

setup:
	pip3 install -r requirements.txt
	sudo apt-get install python-tk 

clean:
	rem -rf __pycache__
