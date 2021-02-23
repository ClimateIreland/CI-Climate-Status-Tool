Climate Status Report Ireland - Online Version
=========================================================
Online version of the Climate Status Report Ireland 2020. Developed using the [Dash](https://dash.plotly.com/) Python web-dashboard framework.


## Downloading and running the application

Clone the repo (Or download and `unzip` the repo from the [github repo](https://github.com/ClimateIreland/CI-Status-Report-Dash)):
```bash
git clone https://github.com/ClimateIreland/CI-Status-Report-Dash
```

Install its dependencies in a virtual environment in the following way:

```bash
python3 -m venv CI-Status-Report-Dash
cd CI-Status-Report-Dash
source bin/activate  # Windows: \venv\scripts\activate
pip install -r requirements.txt
```

then run the app:
```bash
python app.py
```

The application will then be running at http://127.0.0.1:8050/ (Check your terminal in case of different port number)

## Key files and folders

- ./app.py: Starts the application and routes the requests.
- ./charts.py: Functions for developing each individual chart.
- ./page_builder.py: Functions to develop ECV page html.
- ./pages/*: Folder containing all chapter html templates. Each chapter has its own page and can easily be updated via variables, rather than accessing the html.
- ./data/*: Contains the data used for charts.
- ./assets/*: Contains additional css, js and images. CSS files in the folder root will be automatically applied to the application.
