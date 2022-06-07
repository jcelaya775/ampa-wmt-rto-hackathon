# AmPA/WMT RTO Hackathon Project Template

_This template is to help get participants started in working with the data for the American Pets Alive!, Walmart, Return to Owner Hackathon._


#### [:TODO: External References](www.google.com)

### Key Contacts
 - Technical Lead: Kevin Horecka (kevin.horecka@walmart.com)
 - Organizer: Desmond Thomas (desmond.thomas@walmart.com)
 - Organizer: Aishwarya Srikanth (aishwarya.srikanth@walmart.com)
 - Data Owner: Tom Kremer (tom.kremer@americanpetsalive.org)

### License and Legal


[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

 Data related to this work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

 Software and/or code related to this work is licensed under a [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0).


### Problem Statements

See [APA RTO Hackathon 2022.docx](APA%20RTO%20Hackathon%202022.docx) or [APA RTO Hackathon 2022.pdf](APA%20RTO%20Hackathon%202022.pdf) for problem statements and instructions.

### Recommended Base Environment
-----------
 - [Anaconda Python](https://www.anaconda.com/products/distribution)
 - Python 3.9+
 
To create the recommended base environment after installing Anaconda, run:
 
 ```
 conda create -n rtohack python==3.9
 ```


### Project Structure
------------

The structure here is only a starting point. You may make whatever changes you deem appropriate. Your README is _very_ important as it is the first-pass the judges will use to determine if your work should proceed to the next round.

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
```

## Judging Criteria

TODO: ...

### Recommended Packages
------------

For python users, some recommended packages can be found in requirements.txt and installed via:


    pip install -r requirements.txt
    pip install -r {{ your_project.repo_name }}/requirements.txt
