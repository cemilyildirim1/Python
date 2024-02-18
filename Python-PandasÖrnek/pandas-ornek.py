
import pandas as pd

# myseries = pd.Series([1,2,3,4,5])
# print(myseries)
# print(myseries.loc[0])


###########

a = [1,7,2]

myvar = pd.Series(a,index = ["x","y","z"])
print(myvar)

data = {
    "exams ": ["Algorithms","Physic","Math"],
    "duration" : [80,75,64]
}

df = pd.DataFrame(data)
df = pd.DataFrame(data,index = ["day1","day2","day3"])

print(df)
print(df.loc["day2"])


