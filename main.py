#Energy Consumption and prediction project
"""Dataset Description for household_power_consumption.txt
This dataset contains measurements of electric power consumption in a single household over a specific period, recorded at one-minute intervals. The dataset is often used for time-series analysis and energy consumption forecasting. Below is a detailed description of the columns:

Date:
The date when the data was recorded (e.g., 12/01/2007).

Time:
The exact time of the measurement (e.g., 18:45:00).

Global_active_power:
The total amount of power used by the household at that time, measured in kilowatts (kW).

Global_reactive_power:
Power that doesn’t do any useful work but is necessary to maintain the electrical system, also in kilowatts (kW).

Voltage:
The voltage level of the household’s electrical system at the time, measured in volts (V).

Global_intensity:
The amount of current (electricity flow) at the time, measured in amperes (A).

Sub_metering_1:
Energy used by appliances in the kitchen (like a dishwasher or oven), in watt-hours (Wh).

Sub_metering_2:
Energy used by appliances in the laundry room (like a washing machine or dryer), in watt-hours (Wh).

Sub_metering_3:
Energy used by heating and cooling systems (like air conditioners or electric heaters), in watt-hours (Wh).

Use Case:
The dataset is widely used for studying household energy consumption, building predictive models for energy demand, and analyzing the effects of different appliances on overall energy consumption. The data allows for time-series analysis to observe patterns, peak usage times, and anomalies in energy consumption over different periods (daily, weekly, seasonal).

Problem Statement:
Analyze the `household_power_consumption.txt` dataset to identify patterns in electricity usage, predict peak consumption periods, and evaluate the impact of different appliances on overall energy consumption to improve household energy efficiency and reduce costs.

STEP-1 : IMPORTING REQUIRED LIBRARIES AND THE DATASET """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# To ignore the warnings & make code more representable
import warnings
warnings.filterwarnings("ignore")

#Loading the dataset
df = pd.read_csv('E:\\infosys_project\\household_power_consumption.txt',sep=";")

#STEP-2 : DATA EXPLORATION

print(df.shape)
#df.shape functions prints the dimensions of the dataset

print(df.head())
#df.head() function prints the first 5 rows of the dataset. We can specify the number of that we want to print in the paranthesis().

print(df.tail())
#df.tail() function prints the last 5 rows of the dataset. We can specify the number of that we want to print in the paranthesis().

print(df.describe())
#df.describe() function displays all the statistical calculations like mean, minimum, maximum etc..,

print(df.info())
#df.info() function prints the datatype of each column


print(df.describe(include=object))
#df.describe(include='object') is used to generate summary statistics for categorical (object) columns in a Pandas DataFrame.

#STEP-3 : COMBINING COLUMNS
df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H:%M:%S')
df.drop(['Date', 'Time'], axis=1, inplace=True)
#This line removes the original 'Date' and 'Time' columns from the DataFrame, as they are no longer needed once the 'Datetime' column has been created. The inplace=True argument means that the operation modifies the DataFrame directly rather than returning a modified copy.
cols_convert = ['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2']
#This line defines a list of column names that need to be converted to numeric types.
for col in cols_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')
#This loop iterates over each column name in cols_convert and converts the values in those columns to numeric types using pd.to_numeric(). The errors='coerce' argument means that if any value cannot be converted to a number (for instance, if it's a string that can't be interpreted as a number), it will be replaced with NaN (Not a Number).

print(df.describe())
#Now, the new 'Datetime' column will be present as a datetime type, but df.describe() will not provide summary statistics for datetime columns unless you specify include='datetime'.
#The original Date and Time columns will no longer be in the DataFrame.

print(df.info())

#STEP-4 : FINDING AND REPLACING NULL VALUES

print(df.isnull().any())
# prints the columns with null values as false

print(df.isnull().sum() / len(df) * 100)
#Calculating the percentage of null values in each column to know how much amount of data is missing.

null_columns = ['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2','Sub_metering_3']
#This line creates a list named null_columns, which contains the names of columns that are expected to have null (NaN) values.
for col in null_columns:
    df[col].fillna(df[col].mean(), inplace=True)
#This loop iterates over each column name in the null_columns list.

print(df.isnull().sum())
"""Finally all the null values are removed.
This is process of data exploration and data cleaning.
