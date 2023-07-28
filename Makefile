run:
	python3 ./src/Start.py

setup:
	pip3 install -r requirements.txt
	sudo dnf install python-tk 
	pip3 install customtkinter
	pip3 install datetime
	pip3 install turtle
	pip3 install pandas
	pip3 install re
	mkdir time_track_data

clean:
	rem -rf __pycache__
