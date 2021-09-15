CI-Climate-Status-Tool
=========================================================
Climate Ireland's Climate Status Tool is a standalone [Python Dash](https://dash.plotly.com/) application for exploring the 50 Essential Climate Variables (ECVs) detailed in the Climate Status Report Ireland 2020.

The application can be accessed [here](http://www.climateireland.ie/#!/tools/statusReport2020), where it is integrated into the main Climate Ireland website as an iFrame.

The tool currently reads data from both the original Excel files provided by the report authors, and also from CSV files produced from the original Excel files. The CSV files were produced to reduce load time from the Excel files and processing for the charts. Jupyter notebooks are included detailing how the CSVs were generated. The CSV files begin to standardise the naming convention across all variables.

The tool is a step towards a digital first climate status reporting, that can be updated annually and used to both analyse and share the findings of the data.

## Downloading and running the application

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

The application will be running at http://0.0.0.0:8080/statusTool




## Key files and folders

- ./dash_app/app.py: Starts the application and routes the requests
- ./dash_app/charts.py: Functions for developing each individual chart
- ./dash_app/page_builder.py: Functions to develop ECV page html
- ./dash_app/settings.py: Settings for chapter info and chart styling
- ./dash_app/pages/*: Folder containing all chapter html templates. Each chapter has its own page and can easily be updated via variables, rather than accessing the html
- ./dash_app/assets/*: Contains additional css, js and images. CSS files in the folder root will be automatically applied to the application
- ./data/*: Contains the data used for charts
- ./notebooks/copy_core_data.ipynb: Notebook for copying status report data, excluding specific file type associated with large files
- ./notebooks/list_data_files.ipynb: Notebook for listing the available files and data within the data folder structure
- ./notebooks/<chapter>.ipynb: Notebook for tidying chapter data and initial chart development
- ./ecv_naming_convention.csv: An attempt at standardising naming conventions across variables. Not all generated CSVs follow the convention, but should be followed in future developments.
- ./data_files_list.csv: Output from script listing available data files in data folders
- ./requirements.txt: Python packages required to run app
- ./Dockerfile: For running status tool with docker
- ./docker-compose.yml: For running status tool with docker-compose

## Future Development
- Read all chart data from CSV generated from original Excel data. CSV files should follow naming convention
- Allow for data files to be downloaded from application
- Include end-point to serve individual charts for displaying in other locations 
- All map data to read CSV files rather txt files
- Restructure data folder, removing unnecessary files, leaving only CSV files
- Create database from CSV files
- Read all chart data from database rather than CSV files
- Heat maps should have year on x axis