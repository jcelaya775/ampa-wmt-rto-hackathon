# AmPA/WMT RTO Hackathon Project Template

_This template is to help get participants started in working with the data for the American Pets Alive!, Walmart, Return to Owner Hackathon._


#### [<TODO>External References](www.google.com)

### Key Contacts
 - Technical Lead: Kevin Horecka (kevin.horecka@walmart.com)
 - Organizer: Desmond Thomas (desmond.thomas@walmart.com)
 - Organizer: Aishwarya Srikanth (aishwarya.srikanth@walmart.com)
 - Data Owner: Tom Kremer (tom.kremer@americanpetsalive.org)

### License and Legal

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />Data related to this work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

<a rel="license" href="https://opensource.org/licenses/GPL-3.0"><span class="ls-label ls-icon-gpl3" title="Latest General Public License version 3.0"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNzEiIGhlaWdodD0iMjQiPjxkZWZzPjxmaWx0ZXIgaWQ9ImRhcmtyZWFkZXItaW1hZ2UtZmlsdGVyIj48ZmVDb2xvck1hdHJpeCB0eXBlPSJtYXRyaXgiIHZhbHVlcz0iMC4yNDkgLTAuNjE0IC0wLjY3MiAwLjAwMCAxLjAzNSAtMC42NDYgMC4yODggLTAuNjY0IDAuMDAwIDEuMDIwIC0wLjYzNiAtMC42MDkgMC4yNTAgMC4wMDAgMC45OTQgMC4wMDAgMC4wMDAgMC4wMDAgMS4wMDAgMC4wMDAiIC8+PC9maWx0ZXI+PC9kZWZzPjxpbWFnZSB3aWR0aD0iNzEiIGhlaWdodD0iMjQiIGZpbHRlcj0idXJsKCNkYXJrcmVhZGVyLWltYWdlLWZpbHRlcikiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2UvcG5nO2Jhc2U2NCxpVkJPUncwS0dnb0FBQUFOU1VoRVVnQUFBRWNBQUFBWUNBWUFBQUNvYU9BOUFBQUFCbUpMUjBRQS93RC9BUCtndmFlVEFBQUR6a2xFUVZSWWhlV1lYV3hVUlJUSGZ6TjdWN1JDdElZUURVU2pSdGl3MEFyN1lPeVdLdkxna3g4SVJFMkVCMS9VR0xVSkNRbEVFMnNVTWNpSEw4YUdHSTJhSmtZYUUySTFQaFZLKzRCaXBIVnZXSnJLa3dTTldGQkxhYnU3TXo3TUxsa3ZNM3NuL1lndS9KUGQzSm4vT1dmTy9kLzVPUGNLcmdIMHBWWStJT0d3ZzFaU3lmdGJoZ2UvaXhKeWJ0UDY3NkZCU25pdmhza0JtekJ3RFlnemtHcmFERFRiV1gxT0p0UU9sKzlWTGM3eFRLWUI5RnN1WGd2eGVrc1lqcnI0cTFxY2lZdUZkbUN4Z3g0OGV6TDFRUzEvTWZzcC9UL1FtMDdmbWl6SllXQ0JoZFpLcXpWdHA4S0JXakdDdVVsdGR0R2JUczhQcEV4Rys0dEtGZGFHNFpqTkp5Z2x0b08yQ1lPRzdqaGhvRTZXVmJJa3VrU0IwZWd2V1pKZjJPejdsemVuQmZwRlI3aXhoSkx0UHVQV2hUZ3VhTFI5VzFCcUo1QndlTzFzR1I0ODR4Ty9yc1VSaUN2RTZWdmV0QTU0MU9FeTNKalFlM3pqMTdVNFVXaVFVdW5kYmw1dlRZZmhsRys4QUxnT2VCSllEVFJZYklyQUNQQXhjTDZxZngzd0VMRFFFZnRYNEV2Z1JMbjlNSEFmOEladmNoNzQxOHdaV0xieWFXQ1Z3N1puVFQ3M0ZlWitud0h1QmVaWjdDYUJIUENaQkQ0Qk9vRTAwR2o1M1Fac0JmcXJnajBMZkFzODZQQnBCRFlBM3dOdFpaOW1ZS1B2WFh2aXNqakhNNWtHTGRqbHNKc1VSZjFLK2JvTGVCZTR5NUgzM2NCdW9DY0ExZ09iZ0VNMWtsZ0FIQUR1QlBMQUU4RDd3TXN4eVg4RFBBNzB4ZGpOR0pmR3AxNFNzTVJCNzh1TzVIN0dQTnh6UUF2bVBseFlEZnhRV1Ziak1XUC9EVHhWMVU0Q2x6eHlEZ0RsWVRjdGFHMW1UdS9TekVLaHA3WTd6TTRVRXFyeUNqRUpQTzhST3JqOFowRVBSclFvT2pETEMyQUxadDl4b1JGVHVyL3FrY3kwSUlRUko1Q0YxNENiSEdiYlhJVmlGZllEcmVWckNkd0RmTzBTNTBldUZLNGRXRlRWUG9WWk5pNU1ZRVFlaVVsc1JqaWFhbDRxVUMvWU9BRkhzdm1mdWp6QzlBTm55OWMzQW84QmkxM2kySjcyYzVIMk1lQWRqNEhuRUVJSTlOdVlaUjVGaVlUeXFvU0JnNUgyNTBCT0FtUEE3VEhPZHdBM0FIOTVEbWJER0hBTDloZkJDaVR3SnZDcFgwaWRCcjNlVHVtUHNtRjRJdExiZ0praEcySUNMd0ZVQU93RlBzU3N1NkxEK0diTTFKdkpxZE9OS1FsR01SdThEZk13WmIvdmtiL0kwZitIS2lWdEg3SEdNV1hMUWVCUDdJZUZ4T3hmblpVNllRV1F3djBKNDNlTU1KVmdiY0FGWUNndSt3aXVCOVlDOHgxOEVWTWIvVkxkMlo5YWNRakVJNzZEQ01UR2JINm91NFpKRTdDc0JuK2E4bEVPcGlMTStRN085R2ZRQkxVMzhSbERJenBhYXdzRDVxSEdQdGk2K0o3akNRMWlWMnQrcUdPMkF0YUhPSnJmRUp5MmNnS041cGdRZEdaUERzMXFKZjRQTWNJQ0ZnU2dkcEFBQUFBQVNVVk9SSzVDWUlJPSIgLz48L3N2Zz4="/></span></a><br />Software and/or code related to this work is licensed under a <a rel="license" href="https://opensource.org/licenses/GPL-3.0">GNU General Public License version 3</a>.


### Problem Statements

See "APA RTO Hackathon 2022.docx" or "APA RTO Hackathon 2022.pdf" for problem statements and instructions.

### Recommended Base Environment
-----------
 - [Anaconda Python](https://www.anaconda.com/products/distribution)
 - Python 3.9+


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

<TODO>

### Recommended Packages
------------

For python users, some recommended packages can be found in requirements.txt and installed via:


    pip install -r requirements.txt
