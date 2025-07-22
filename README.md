# ☕ Coffee Sales ETL Pipeline

This project demonstrates a beginner-friendly ETL (Extract, Transform, Load) pipeline for coffee shop sales data.  
It reads raw data from a CSV file, cleans and transforms it using Python (Pandas), and loads the results into a PostgreSQL database.

---

## 🔧 Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- pyarrow (for saving parquet files)

---

## 📁 Project Structure

```
coffee-sales-etl-pipeline/
├── data/
│   ├── raw/              # Raw input data (CSV)
│   └── processed/        # Cleaned output data (Parquet)
│
├── src/
│   ├── extract.py        # Read CSV file
│   ├── transform.py      # Data cleaning + transformation
│   ├── load.py           # Load to PostgreSQL
│   └── etl.py            # Orchestration script
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/coffee-sales-etl-pipeline.git
cd coffee-sales-etl-pipeline
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
.venv\Scripts\activate  # on Windows
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Place your raw CSV inside `data/raw/index_1.csv`

5. Update your PostgreSQL credentials in `etl.py`

6. Run the ETL pipeline:

```bash
python src/etl.py
```

---

## ✅ What It Does

- **Extract**:
  - Reads a CSV from `data/raw/`

- **Transform**:
  - Drops rows with missing `card`
  - Converts datetime column
  - Extracts hour into a new column
  - Adds binary column `is_cash`

- **Load**:
  - Saves to Parquet in `data/processed/`
  - Loads cleaned data into PostgreSQL (`coffee_sales` table)

---

## 🙌 Author

Isa Zeynalov – Data Analytics Engineer
Let’s connect on [LinkedIn](https://www.linkedin.com/in/isa-zeynalov-56a8a31a9/)

