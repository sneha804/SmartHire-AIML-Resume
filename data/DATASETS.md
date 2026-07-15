# Datasets — what to download and how

All datasets come from **Kaggle** (free account needed). Download them **once** and
place the CSVs directly under `data/raw/`. Never edit the files in `raw/`.

## What to download

| Dataset | Used for | Kaggle search term | Typical file |
|---------|----------|--------------------|--------------|
| **Resume Dataset** (~960 resumes, 25 categories) | Resume classifier (supervised) | `resume dataset` | `UpdatedResumeDataSet.csv` |
| **Naukri Job Listings** (Indian jobs: title, skills, experience, salary) | Job corpus / recommender | `naukri job listings` | `naukri_com-job_sample.csv` |
| **LinkedIn Job Postings 2023–2024** (detailed descriptions) | Job corpus / recommender | `linkedin job postings 2023 2024` | `postings.csv` |
| **Indeed / Job Recommendation** *(optional)* | Extra job variety | `job recommendation dataset` | varies |

> Start with the **Resume Dataset + Naukri** only. That is enough to build the core
> project. Add LinkedIn/Indeed later if you want more job variety.

## How to get them — Option A: Kaggle website (easiest)

1. Create a free account at <https://www.kaggle.com>.
2. Search the term from the table above (e.g. "resume dataset").
3. Open the dataset page → click **Download** (downloads a `.zip`).
4. Unzip it and move the `.csv` file into this project's `data/raw/` folder.
5. Repeat for each dataset you need.

## How to get them — Option B: Kaggle API (command line)

Do this once so you can download by command instead of clicking.

1. Install the client:
   ```
   pip install kaggle
   ```
2. Get your API token: Kaggle → your profile → **Settings** → **API** →
   **Create New Token**. This downloads `kaggle.json`.
3. Put `kaggle.json` where Kaggle expects it:
   - Windows: `C:\Users\<you>\.kaggle\kaggle.json`
   - macOS/Linux: `~/.kaggle/kaggle.json`
4. From the dataset's Kaggle page, copy its slug (the `owner/name` part of the URL),
   then download straight into `data/raw/`:
   ```
   kaggle datasets download -d <owner>/<dataset-name> -p data/raw --unzip
   ```
   Example shape (verify the exact slug on Kaggle — owners change):
   ```
   kaggle datasets download -d gauravduttakiit/resume-dataset -p data/raw --unzip
   ```

## After downloading

1. Confirm the files are in `data/raw/`, for example:
   ```
   data/raw/UpdatedResumeDataSet.csv
   data/raw/naukri_com-job_sample.csv
   ```
2. Open `src/config.py` and set `RESUME_CSV` and `JOBS_CSV` to your actual filenames.
3. Load and inspect them in `notebooks/01_eda.ipynb` (`df.head()`, `df.shape`,
   `df['Category'].value_counts()`).

## Building the job corpus

The recommender searches against **one** combined job table, not the separate files.
In `src/data/preprocess.py`:

1. Load each job dataset.
2. Rename columns so they share a common schema:
   **title, company, location, skills, description, experience**.
3. Keep only those columns, concatenate the datasets into one dataframe, drop
   duplicates and empty rows.
4. Create a single `text` column (e.g. `title + " " + skills + " " + description`)
   and clean it — this `text` column is what gets TF-IDF vectorized.
5. Save the result to `data/interim/` (e.g. `job_corpus.csv`).

> Different sources name columns differently (e.g. `job_title` vs `title`). Inspect
> each file first, then write the rename mapping. Missing columns can be left blank.
