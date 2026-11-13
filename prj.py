import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Student_Data ={
    "Student_id":[101,102,103,104,105,106,107,108,109,110],
    "Name":["Arun","Priya","Ravi","Diviya","Karthik","Meena","Suresh","Anitha","Vijay","Lakshmi"],
    "Department":["Computer Science","Computer Science","Information Technology","Information Technology","Computer Science","Information Technology","Computer Science","Information Technology","Computer Science","Information Technology"],
    "Python":[85,92,68,76,88,95,72,81,64,90],
    "Mathematics":[78,89,70,82,91,87,75,79,66,94],
    "Statistic":[80,94,65,78,86,92,70,84,62,88]
}
df = pd.DataFrame(Student_Data)
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df)
df["Total"] = df[["Python","Mathematics","Statistic"]].sum(axis=1)
print(df[["Name","Total"]])
df["Average"] = df[["Python","Mathematics","Statistic"]].mean(axis=1).round(2)
print(df[["Name","Total","Average"]])
# conditional statement
def Calculate_Grade(avg):
    if avg >= 90:
        return"A+"
    elif avg >=80:
        return"A"
    elif avg >=70:
        return"B"
    elif avg >=60:
        return"C"
    else:
        return"D"
df["Grade"] = df["Average"].apply(Calculate_Grade)
print(df[["Name","Average","Grade"]])
ranked_student = df.sort_values(by="Average",ascending=False)
print(ranked_student[["Name","Average","Grade"]])
top_student = df.loc[df["Average"].idxmax()]
print("Top Student:",top_student["Name"])
print("Average:",top_student["Average"])
print("Grade:",top_student["Grade"])
lowest_student = df.loc[df["Average"].idxmin()]
print("Lowest Student:",lowest_student["Name"])
print("Average:",lowest_student["Average"])
print("Grade:",lowest_student["Grade"])
#using numpys
python_marks = df["Python"].to_numpy()
print("Mean:",np.mean(python_marks))
print("Median:",np.median(python_marks))
print("Maximum:",np.max(python_marks))
print("Minimum:",np.min(python_marks))
print("Standard deviation:",np.std(python_marks))
mathematics_marks = df["Mathematics"].to_numpy()
print("Mean:",np.mean(mathematics_marks))
print("Maximum:",np.max(mathematics_marks))
print("Minimum:",np.min(mathematics_marks))
print("Standard deviation:",np.std(python_marks))
statistic_marks = df["Statistic"].to_numpy()
print("Mean:",np.mean(statistic_marks))
print("Maximum:",np.max(statistic_marks))
print("Minimum:",np.min(statistic_marks))
print("Standard deviation:",np.std(statistic_marks))

#outlier

print("\nPython Mark of Outlier\n",)
Q1 = np.percentile(python_marks,25)
Q2 = np.percentile(python_marks,50)
Q3 = np.percentile(python_marks,75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR
outlier = python_marks[(python_marks < lower_limit)|(python_marks > upper_limit)]
print("Q1:",Q1)
print("Q2:",Q2)
print("Q3:",Q3)
print("IQR:",IQR)
print("Lower Limit",lower_limit)
print("Upper Limit",upper_limit)
print("Outlier",outlier)
print("\nMathematics Mark of Outlier\n")
Q1 = np.percentile(mathematics_marks,25)
Q2 = np.percentile(mathematics_marks,50)
Q3 = np.percentile(mathematics_marks,75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR
outlier = mathematics_marks[(mathematics_marks < lower_limit)|(mathematics_marks > upper_limit)]
print("Q1:",Q1)
print("Q2:",Q2)
print("Q3:",Q3)
print("IQR:",IQR)
print("Lower Limit",lower_limit)
print("Upper Limit",upper_limit)
print("Outlier",outlier)
print("\nStatistic Mark of Outlier\n")
Q1 = np.percentile(statistic_marks,25)
Q2 = np.percentile(statistic_marks,50)
Q3 = np.percentile(statistic_marks,75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR
outlier = statistic_marks[(statistic_marks< lower_limit)|(statistic_marks > upper_limit)]
print("Q1:",Q1)
print("Q2:",Q2)
print("Q3:",Q3)
print("IQR:",IQR)
print("Lower Limit",lower_limit)
print("Upper Limit",upper_limit)
print("Outlier",outlier)

python_total = df["Python"].sum()
mathematics_total = df["Mathematics"].sum()
statistic_total = df["Statistic"].sum()
subjects = ["Python","Mathematics","Statistic"]
marks = [python_total,mathematics_total,statistic_total]
plt.pie(marks,labels = subjects,autopct ="%1.1f%%")
plt.title("Subject-wise total marks distribution")
plt.show()

df["Average"] = df[["Python","Mathematics","Statistic"]].mean(axis=1)
plt.bar(df["Name"],df["Average"])
plt.title("Average Mark of Student")
plt.xlabel("Student Name")
plt.ylabel("Python Marks")
plt.xticks(rotation=45)
plt.show()