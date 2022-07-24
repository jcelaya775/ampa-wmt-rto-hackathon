Team Alpha RTO Hackathon DS Project
==============================

Description:

This project aims to analyze the animal and shelter data provided by the hackathon organizer. We achieved the following ovjectives:
(1) train and test both supervised and unsupervised models (linear regression, decision tree) to predict animal location
(2) develop an interactive dashboard to visualize trends in animal behavior and understand city patterns


### Project Structure
------------


```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │                     predictions
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│
├── web-app            <- Contains the files for the web app
│   └── app.py         <- Main server
│   └── requirements.txt <- Contains required python modules
│   └── deployement_model <- AI model for deployment
│   └── models         <- Contains all of the AI models
│   └── scripts        <- Frontend scripts
│   └── scss           <- Sass files
│   └── static         <- Contains
|        ├── css       <- Styling
|        ├── img       <- Images
|        ├── vendor    <- Libraries
│   └── templates      <- Frontend files
│   └── utils          <- Helper functions
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`

```

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
