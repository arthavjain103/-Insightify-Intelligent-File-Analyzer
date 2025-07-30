import pandas as pd
from io import BytesIO


def analyze_file(contents: bytes, filename: str):
    if filename.endswith('.csv'):
        df = pd.read_csv(BytesIO(contents))
    elif filename.endswith('.xlsx'):
        df = pd.read_excel(BytesIO(contents))
    else:
        raise ValueError("Only CSV and XLSX files are supported")

    summary = {
        "filename": filename,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "columns_list": df.columns.tolist(),
        "data_types": df.dtypes.astype(str).to_dict(),
        "nulls_per_column": df.isnull().sum().astype(int).to_dict(),
        "unique_values_per_column": {
            col: int(df[col].nunique()) for col in df.columns
        },
        "sample_rows": df.head().fillna("").astype(str).to_dict(orient='records'),
        "column_stats": df.describe(include='all').fillna("").astype(str).to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "empty_columns": [col for col in df.columns if df[col].isnull().all()],
        "empty_rows": int(df.isnull().all(axis=1).sum()),
        "correlation_matrix": df.corr(numeric_only=True).fillna(0).round(4).to_dict(),
        "outlier_counts": {
            col: int(
                ((df[col] < (df[col].quantile(0.25) - 1.5 * (df[col].quantile(0.75) - df[col].quantile(0.25)))) |
                 (df[col] > (df[col].quantile(0.75) + 1.5 * (df[col].quantile(0.75) - df[col].quantile(0.25)))))
                .sum()
            )
            for col in df.select_dtypes(include='number').columns
        }
    }

    return summary
