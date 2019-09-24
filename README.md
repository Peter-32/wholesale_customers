wholesale_customers
==============================

This project aims to recommend products to our top customers to increase revenue significantly.

The data tells us which items and similar and which items the customer has a liking for.  Together, this information will give us sales recommendations.

I found the data online on this website: https://archive.ics.uci.edu/ml/datasets/wholesale+customers

## Formal

- T: Recommending categories to top customers when spend for one category is relatively slow
- P: I won't use a performance score, but the model will be interpretable and accurate
- E: Category similarity and user affinity

A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E

## Assumptions

Customers are often purchasing the other categories from another wholesale distributor.  We want to become their new wholesale distributor for that category, or even recommend they sell more of a category.

We should focus recommending only for customers that make up 80% of the unit sales across categories.

We should only recommend categories to a customer if the normalized recommendation score deviates far from the percentage currently being purchased for the category.  This normalization method will become clear once we get the recommendation scores.

This could be solved manually quite easily.  Sort by each group descending, check the percentages of each, and take note of the categories that look like a promising recommendation.  Based on a high level view of the data, I expect about 200 of 450 customers to make up 80% of the unit sales.

Treat horeca and retail customers separately.

## Select Data

#### What Data Do We Have Available?

We have channel, category, and amount.  We should use these.

#### What Data Is Not Available That You Wish Was Available?

None

#### What Data Should Be Excluded?

I don't want to use the region column.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
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
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
