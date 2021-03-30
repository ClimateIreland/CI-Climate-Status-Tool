Climate Status Report Ireland - Online Version
=========================================================
Online version of the Climate Status Report Ireland 2020. Developed using the [Dash](https://dash.plotly.com/) Python web-dashboard framework.

The application is running standalone at [dash.climateireland.ie](http://dash.climateireland.ie/) and wrapped in [int.climateireland.ie](http://int.climateireland.ie/#!/tools/statusReport2020)


## Downloading and running the application

Clone the repo (Or download and `unzip` the repo from the [github repo](https://github.com/ClimateIreland/CI-Status-Report-Dash)):
```bash
git clone https://github.com/ClimateIreland/CI-Status-Report-Dash
cd CI-Status-Report-Dash
```

Create symbolic link to the your local link to OneDrive [Status_Tool folder](https://uccireland-my.sharepoint.com/:f:/g/personal/walther_camaro_ucc_ie/EvDuB5pRGjxFiIva2GNwbcMBhZN4cHrps0owgUdv9J89EQ?e=w87bPT)
```bash
ln -s venv "/Users/dan/OneDrive - University College Cork/Status_Tool" data
# Windows: mklink /D data "/Users/dan/OneDrive - University College Cork/Status_Tool"
```

### Run as Dockerised container
Install Docker and Docker Compose:

- Docker: https://docs.docker.com/engine/installation/
- Docker Compose: https://docs.docker.com/compose/install/

Run containers:
```bash
sh run_docker.sh
# Windows: run_docker.bat
```

Dash will be running on http://0.0.0.0:8080/ 

### Run from venv (for development)
Install its dependencies in a virtual environment:

```bash
python3 -m venv ./
source bin/activate  # Windows: \venv\scripts\activate
pip install -r dash_app/requirements.txt
```

Run the app:
```bash
cd dash_app
python app.py
```

The application will then be running at http://127.0.0.1:8050/ (Check your terminal in case of different port number)

## Key files and folders

- ./app.py: Starts the application and routes the requests.
- ./charts.py: Functions for developing each individual chart.
- ./page_builder.py: Functions to develop ECV page html.
- ./pages/*: Folder containing all chapter html templates. Each chapter has its own page and can easily be updated via variables, rather than accessing the html.
- ./assets/*: Contains additional css, js and images. CSS files in the folder root will be automatically applied to the application.