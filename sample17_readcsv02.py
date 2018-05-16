import pandas as pd
import statistics as st
 
df = pd.read_csv("sample15_csvFile.csv", header=None)

print(df)

print(st.median(df))
print(st.mode(df))
print(st.mean(df))
print(st.pvarience(df))

