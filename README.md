# Titanic Dataset – Task 02: Data Cleaning and Exploratory Data Analysis (EDA)

---

This project focuses on performing **data cleaning** and **exploratory data analysis (EDA)** using the **Titanic dataset**. The goal is to analyze survival patterns and explore relationships between key variables such as age, gender, passenger class, and family size.

---

## Objectives

- Load and inspect the Titanic dataset  
- Handle missing data and transform variables  
- Engineer new features such as `FamilySize` and `IsAlone`  
- Visualize key distributions and survival rates  
- Identify patterns and trends through data visualization  

---

## Workflow Summary

1. Load dataset from Stanford-hosted Titanic CSV  
2. Clean missing values (e.g., impute `Age` with median)  
3. Convert categorical values (`Sex`) to numeric format  
4. Create new features:
    - `FamilySize` = `Siblings/Spouses Aboard` + `Parents/Children Aboard` + 1  
    - `IsAlone` = 1 if `FamilySize == 1`, else 0  
5. Generate summary statistics and survival rates  
6. Visualize:
    - Survival by gender and passenger class  
    - Age distributions and survival by age  
    - Survival by family size  
    - Fare distribution by survival  

---

## Technologies Used

- `Python 3.x`  
- `pandas` – for data manipulation  
- `numpy` – for numerical operations  
- `matplotlib` & `seaborn` – for visualization  
- Google Colab – for interactive execution  

---

## Evaluation

- ✅ Dataset loaded and inspected successfully  
- ✅ Missing values handled appropriately (e.g., median imputation for age)  
- ✅ New insights derived from engineered features (`FamilySize`, `IsAlone`)  
- ✅ Visualizations provide a clear understanding of survival trends  
- ✅ Survival rate analysis segmented by gender, class, and age  

---

## Key Findings

- **Overall survival rate**: ~38.38%  
- **Female survival rate**: ~74.20%  
- **Male survival rate**: ~18.89%  
- **First class survival rate**: ~62.96%  
- **Third class survival rate**: ~24.24%  
- **Alone passenger survival rate**: ~30.20%  
- **Passengers with family survival rate**: ~50.51%  

---

## Notes

- The dataset used is sourced from Stanford's version of the Titanic dataset.  
- Gender was encoded numerically to simplify analysis (`0 = male`, `1 = female`).  
- The project is structured for Google Colab and assumes active internet access to load the dataset.  
- All charts are rendered inline and help illustrate key insights effectively.  
