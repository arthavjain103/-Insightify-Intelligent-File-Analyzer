# 📊 Insightify: Intelligent File Analyzer

Insightify is a powerful web-based tool for **automated data analysis and intelligent cleaning suggestions**. Upload any CSV or Excel file, and get an instant, visual summary — no coding required. Built for data analysts, students, and teams needing quick insight into raw datasets.

---

# Key Features

- **Upload & Metadata Extraction:**  
  Upload CSV or Excel files and instantly view file name, type, size, and basic stats.

- **Column Insights:**  
  Explore column-wise summaries including data types, number of rows and columns, and null values.

- **Descriptive Statistics:**  
  Automatically compute and display statistical metrics like mean, median, min/max, standard deviation, etc., for numeric columns.

- **Null & Unique Value Detection:**  
  Quickly see how many missing or unique values exist per column to assess data quality.

- **Duplicate & Empty Data Identification:**  
  Spot and highlight duplicate rows, empty columns, and empty rows for easy cleanup.

- **Correlation Matrix with Interactive Heatmap:**  
  Explore relationships between numeric columns using a correlation matrix, visualized both as a table and an interactive heatmap. This makes it easy to spot strong or weak correlations in your data.

- **Outlier Detection:**  
  Automatically detect and count outliers in each numeric column, helping you identify anomalies and potential data entry errors that could affect your analysis.

- **Data Cleaning Suggestions:**  
  Receive smart suggestions like dropping columns, filling missing values, or converting data types — all tailored to your dataset.

- **Interactive Visualizations:**  
  Instantly generate charts like bar graphs and histograms to better understand distributions and value counts.

---

# 🛠️ Tech Stack

| Layer       | Tech                                  |
| ----------- | ------------------------------------- |
| 💻 Frontend | Streamlit (Python)                    |
| 🔌 Backend  | FastAPI (Python)                      |
| 📈 Analysis | Pandas, Seaborn, Matplotlib, OpenPyXL |

---

# 🗂 Project Structure

```bash
smart-file-analyzer/
├── backend/
│   ├── routers/         # FastAPI route handlers
│   ├── services/        #  logic and analysis functions
│   └── main.py          # FastAPI app entry point
├── frontend/
│   └── app.py           # Streamlit frontend application
└── README.md            # Project documentation
```

---

### ⚙️ How It Works

Insightify bridges the gap between raw data and actionable insight with a seamless workflow:

- **📤 Upload Your File**  
  Users upload a CSV or Excel file directly through the Streamlit-based interface. No technical expertise required.

- **🔁 Backend Processing with FastAPI**  
  The file is instantly sent to a FastAPI-powered backend, where it's processed using Pandas and analytical libraries.

- **📊 Smart Data Analysis**  
  The backend analyzes the dataset, calculates key statistics, detects anomalies, and prepares a comprehensive JSON summary.

- **🖥 Visual & Interactive Results**  
  Streamlit renders the analysis in an intuitive dashboard — complete with charts, tables, outlier detection, and smart cleaning suggestions — all ready for user interaction.

---

### 🧪 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Insightify-Intelligent-File-Analyzer.git && cd smart-file-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the backend
uvicorn backend.main:app --reload

# 4. Start the frontend
streamlit run frontend/app.py
```

---



