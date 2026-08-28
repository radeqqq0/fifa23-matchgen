# fifa23-matchgen
A FIFA 23 random team generator built with Python and Streamlit, based on an old version of [fifamatchcreator.com](https://fifamatchcreator.com)

## Features

- Choose a star rating range for each team
- Choose beetween clubs, national teams or both
- Generate 2 random teams
- Reroll teams without changing the settings

## Data source
The source code of this project is licensed under the MIT License.

Data came from the [FIFA 23 Complete Player Dataset](https://www.kaggle.com/datasets/cashncarry/fifa-23-complete-player-dataset) 
(author: cashncarry, licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)). 
File renamed to `clubs.csv`. League names were normalized by removing division numbers. The MIT License does not apply to this file.

`national.csv` was made by me using data from [fifaindex.com](https://fifaindex.com/pl/druzyny/fifa23?category=men)

## Running locally

1. Clone the repository
```bash
git clone https://github.com/radeqqq0/fifa23-matchgen
cd fifa23-matchgen
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
streamlit run app.py
```