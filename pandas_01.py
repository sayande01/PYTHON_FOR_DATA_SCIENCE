import pandas as pd
import numpy as np

# data = {"Name": ["Sayan", "Soumya", "Sanjib"],
#         "Age": [25, 26, 28],
#         "Salary": [45000, 25000, 35000]}
#
# df = pd.DataFrame(data)
# print(df)

# data_xl = pd.read_csv("D:/Python excel/employees.csv")
# print(data_xl)

# data_excel = pd.read_excel("D:/Python excel/Employee Sample Data.xlsx")
# print(data_excel.head(10))
# print(data_excel.tail(10))
# print(data_excel.info())
# print(data_excel.describe())
# print(data_excel.isnull())

# data_emp = pd.read_excel("D:/Python excel/Emp.xlsx")
# # print(data_emp)
# print(data_emp["SALARY"].duplicated().sum())
# print(data_emp.drop_duplicates(["EMPID"]))


# ==================================================================================

data_emp2 = pd.read_excel("D:/Python excel/Emp.xlsx")
# print(data_emp2)

# print(data_emp2.isnull().sum())
# print(data_emp2.dropna())  #drop null values

# print(data_emp2.replace(np.nan, "NA"))  # replace blank with "NA
# data_emp2["SALARY"] = data_emp2["SALARY"].replace(np.nan, 99999)  # replace blank salary with value 99999
# print(data_emp2)

# m = (data_emp2["SALARY"].mean())
# data_emp2["SALARY"] = (data_emp2["SALARY"].replace(np.nan, m))  # replacing none with mean val
# print(data_emp2)

# print(data_emp2.fillna(method= "bfill"))  #Backward fill
# print(data_emp2.fillna(method= "ffill"))  #Forward fill

# =========================
# Column Transformation
# =========================

# data_emp2.loc[data_emp2["SALARY"] >= 45000, "Level"] = "Top"
# data_emp2.loc[data_emp2["SALARY"] < 45000, "Level"] = "Intermediate"
#
# data_emp2.loc[data_emp2["AGE"] >= 30, "Exp"] = "Experienced"
# data_emp2.loc[data_emp2["AGE"] < 30, "Exp"] = "Fresher"
# # print(data_emp2)
#
# data_emp2["DEPT"] = data_emp2["Level"] + " " + data_emp2["Exp"]
# print(data_emp2)

# ==============================================================
# Group By

# data_excel = pd.read_excel("D:/Python excel/Employee Sample Data.xlsx")
# # print(data_excel)
#
# gp = data_excel.groupby(["Department", "Gender"]).agg({"Gender": "count"})
# # print(gp)
#
# gp1 = data_excel.groupby(["Country", "Gender"]).agg({"Annual Salary" : "max","Age" : "min"})
# print(gp1)


# ====================================================================

# Merge Join Concatenate

data1 = {"Emp ID": ["E01", "E02", "E03", "E04", "E05", "E06"],
         "Names": ["Chris", "Nolan", "Tom", "Mathew", "Thomas", "Oliver"],
         "Age": ["34", "56", "45", "39", "49", "32"]}

data2 = {"Emp ID": ["E01", "E02", "E03", "E04", "E05", "E06"],
         "Salary": [45000, 55000, 65000, 48000, 57000, 61000]}

data3 = {"Emp ID": ["E07", "E08", "E09", "E10", "E11", "E12"],
         "Names": ["Kevin", "Sam", "Jack", "Douglas", "Smith", "Bruce"],
         "Age": ["38", "52", "49", "41", "55", "33"]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# print(df1)
# print()
# print(df2)


# print(pd.merge(left=df1, right=df2, on="Emp ID", how="inner"))  # emp id key


# print(pd.concat([df1, df3]))  # Concatenation

# df4 = df1.copy()

# print(df4)

# df4.loc[0, "Names"] = "Nick"  # modify elements via index
# df4.loc[1, "Age"] = 29
# df4.loc[2, "Emp ID"] = "E99"
# #
# # print(df4)
#
# print(df1.compare(df4))  # highlights the changed parts

# ==========================================================================

# Pivoting and Melting

# df = pd.DataFrame({'fff': ['one', 'one', 'one', 'two', 'two',
#                            'two'],
#                    'bbb': ['P', 'Q', 'R', 'P', 'Q', 'R'],
#                    'baa': [2, 3, 4, 5, 6, 7],
#                    'zzz': ['h', 'i', 'j', 'k', 'l', 'm']})
#
# print(df)
# print()
# print(df.pivot(index='fff', columns='bbb', values='baa'))

# output
# bbb  P  Q  R
# fff
# one  2  3  4
# two  5  6  7

# df = pd.DataFrame({'P': {0: 'p', 1: 'q', 2: 'r'},
#                    'Q': {0: 1, 1: 3, 2: 5},
#                    'R': {0: 2, 1: 4, 2: 6}})
#
# # print(df.melt(id_vars=['P'], value_vars=['Q', 'R']))
#
# print(df.melt(id_vars=['P'], value_vars=['Q'],
#         var_name='myVarname', value_name='myValname'))
