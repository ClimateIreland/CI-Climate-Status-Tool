CI-Climate-Status-Tool
=========================================================
Climate Ireland's Climate Status Tool is a standalone [Python Dash](https://dash.plotly.com/) application for exploring the 50 Essential Climate Variables (ECVs) detailed in the [Climate Status Report Ireland 2020](https://www.epa.ie/publications/research/climate-change/research-386-the-status-of-irelands-climate-2020).

The application can be accessed [here](http://www.climateireland.ie/#!/tools/statusReport2020), where it is integrated into the main Climate Ireland website as an iFrame. 

The tool is a step towards digital first climate status reporting, that can be updated annually and used to both analyse and share the findings of the data.

## Data (Currently) Not Included
The data collected and used in the Climate Status Report Ireland 2020 was sourced from a number of organisations. Most of the source organisations do have open access data policies, however formal agreements have yet to be arranged to share the processed datasets. Therefore, the underlying data is not included in this repo but may be requested by contacting the report authors.

## Getting Started

Clone the repo (Or download and `unzip` the repo from the [github repo](https://github.com/ClimateIreland/CI-Climate-Status-Tool)):
```bash
# This is currently a private repo, contact the CI dev team for access
git clone https://github.com/ClimateIreland/CI-Climate-Status-Tool 
```

Install its dependencies in a virtual environment in the following way:

```bash
cd CI-Climate-Status-Tool
python3 -m venv ./
source bin/activate  # Windows: \venv\scripts\activate
pip install -r requirements.txt
```

Download and create a symbolic link to the data:
 - Download the data from teams Climate Ireland > CI Status Report > Data
 - Alternatively you can create a link directly to the folder if your machine is linked to the Climate Ireland OneDrive
 
 ```bash
ln -s <path_to_folder>/ ./data
# i.e. ln -s ~/ClimateIreland/status_tool_data ./data
```

Run the app:
```bash
python dash_app/app.py
```

The application will then be running at http://127.0.0.1:8050/ (Check your terminal in case of different port number). If the charts display a X instead of the expected data check that the correct data path is being used.

## Running with Docker

If you have have Docker and Docker-Compose installed you can run the tool as a container.

Set the data path as an env variable:
```bash
export STATUS_TOOL_DATA=<path_to_data>
```

Run with docker-compose:
```bash
docker-compose up # or run in background with docker-compose up -d
```

Run with docker:
```bash
docker build --no-cache -t climate_core .
docker run -it -p 8080:8080 --mount source=$STATUS_TOOL_DATA,target=/home/data --name climate_status_tool climate_status_tool
```
The app will be running on localhost:8080


The application will be running at http://0.0.0.0:8080/statusTool


## Key files

- ./dash_app/app.py: Starts the application and routes the requests
- ./dash_app/charts.py: Functions for developing each individual chart
- ./dash_app/page_builder.py: Functions to develop ECV page html
- ./dash_app/settings.py: Settings for chapter info and chart styling
- ./dash_app/pages/*: Folder containing all chapter html templates. Each chapter has its own page and can easily be updated via variables, rather than accessing the html
- ./dash_app/assets/*: Contains additional css, js and images. CSS files in the folder root will be automatically applied to the application
- ./data/*: Contains the data used for charts. Needs to be set as a symbolic link to actual data
- ./Dockerfile: For running status tool with docker
- ./docker-compose.yml: For running status tool with docker-compose

## Further Development
- Secure open access data agreements with data providers.
- Host all processed data (maps and time-series) as open access CSV files on cloud storage (i.e. AWS S3).
- Include data download feature for each chart provided.