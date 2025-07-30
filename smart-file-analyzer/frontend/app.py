import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("📊 Insightify: Intelligent File Analyzer")

uploaded_file = st.file_uploader("Upload your CSV or Excel File")

if uploaded_file is not None:
    st.success("File Uploaded")
    st.write("Filename:", uploaded_file.name)
    st.write("**File Type:**", uploaded_file.type)
    st.write("**File Size:**", f"{uploaded_file.size / 1024:.2f} KB")

    if st.button(" 🔍 Analyse File"):
        try:
            with st.spinner("Analyzing..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                response = requests.post("http://127.0.0.1:8000/upload-file/", files=files)

                if response.status_code == 200:
                    try:
                        result = response.json()
                        if "summary" in result:
                            summary = result["summary"]
                            st.success("✅ Analysis Complete")

                            st.write("**Rows:**", summary["rows"])
                            st.write("**Columns:**", summary["columns"])
                            st.write("**Column Names:**", summary["columns_list"])

            
                            with st.expander("**🔹 Data Types**"):
                                for col, dtype in summary.get("data_types", {}).items():
                                    st.markdown(f"- {col}: `{dtype}`")

                            with st.expander("**🔹 Null Values per Column**"):
                                st.json(summary["nulls_per_column"])

                            with st.expander("**🔹 Unique Values per Column**"):
                                unique_values = summary.get("unique_values_per_column", {})
                                if unique_values:
                                    for col, values in unique_values.items():
                                        st.markdown(f"- **{col}**: `{values}` unique values")
                                else:
                                    st.info("No unique value data available.")
                            

                            with st.expander("**🔹 Sample Rows**"):
                                st.dataframe(summary["sample_rows"])

                            with st.expander("**🔹 Column Statistics**"):
                                st.json(summary["column_stats"])

                            st.write("**Duplicate Rows:**", summary["duplicate_rows"])
                            st.write("**Empty Columns:**", summary["empty_columns"])
                            st.write("**Empty Rows:**", summary["empty_rows"])

                            with st.expander("**🔹 Correlation Matrix (Interactive Heatmap)**"):
                                corr_matrix = summary.get("correlation_matrix", {})
                                if corr_matrix:
                                    # Convert JSON to DataFrame
                                    df_corr = pd.DataFrame(corr_matrix)
                                    
                                    st.write("📋 Raw Correlation Data:")
                                    st.dataframe(df_corr)

                                    st.write("📊 Heatmap:")
                                    fig, ax = plt.subplots(figsize=(10, 6))
                                    sns.heatmap(df_corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
                                    st.pyplot(fig)
                                else:
                                    st.info("Correlation matrix not available.")


                            with st.expander("**🔹 Outlier Counts per Column**"):
                                st.json(summary["outlier_counts"])
                                
                            with st.expander("🧼 Suggested Cleaning Steps"):
                              suggestions = []
                              null_values = summary.get("nulls_per_column", {})
                              for col, count in null_values.items():
                                    if count > 0:
                                        suggestions.append(f"Consider handling null values in column '{col}'.")
                                        
                              
                              if summary.get("duplicate_rows", 0) > 0:
                                   suggestions.append("Remove duplicate rows.")
                                   
                              empty_cols = summary.get("empty_columns", 0)
                              if empty_cols > 0:
                                    suggestions.append(f"➤ Drop {empty_cols} empty columns – no useful data present.")
                                   
                            outliers = summary.get("outlier_counts", {})
                            for col, count in outliers.items():
                                    if count > 0:
                                        suggestions.append(f"➤ Handle {count} outliers in `{col}` – check for extreme values.")
                                        
                                        
                            if suggestions:
                                for s in suggestions:
                                    st.markdown(s)
                            else:
                                st.success("✅ No major cleaning needed! Your data looks good.")
                                    

                        elif "error" in result:
                            st.error(f"❌ Error from backend: {result['error']}")
                        else:
                            st.error("Unexpected response from backend.")

                    except Exception as parse_error:
                        st.error(f"❌ Failed to parse JSON: {str(parse_error)}")
                        st.write("Raw Response Text:", response.text)
                else:
                    st.error(f"❌ Failed with status code {response.status_code}")
                    st.write("Raw Response Text:", response.text)

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")