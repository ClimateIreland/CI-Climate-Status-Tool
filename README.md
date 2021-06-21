Climate Status Report Ireland - Online Version
=========================================================
Online version of the Climate Status Report Ireland 2020. Developed using the [Dash](https://dash.plotly.com/) Python web-dashboard framework.

The application is running standalone at [dash.climateireland.ie](http://dash.climateireland.ie/) and wrapped in [int.climateireland.ie](http://int.climateireland.ie/#!/tools/statusReport2020)


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

Set the DATA_PATH:
- Make a copy of env.txt
- Rename the copy env.py
- Set the DATA_PATH to the your local link to OneDrive [Status_Tool folder](https://uccireland-my.sharepoint.com/:f:/g/personal/walther_camaro_ucc_ie/EvDuB5pRGjxFiIva2GNwbcMBhZN4cHrps0owgUdv9J89EQ?e=w87bPT):

```python
import os
# Set the path to your local data repository, don't forget the trailing '/'
os.environ.setdefault("DATA_PATH","/Users/dan/OneDrive - University College Cork/Status_Tool/")
```

Run the app:
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