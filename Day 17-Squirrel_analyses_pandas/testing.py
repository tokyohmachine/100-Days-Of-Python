# Squirrel_analyses_pandas
import pandas as pd
import pandas

# Iterate over (column name, Series) pairs.
# s = pd.Series(['A', 'B', 'C'])
# for index, value in s.items():
#  print(f"Index : {index}, Value : {value}")


# dta.items()
df = pd.DataFrame({'species': ['bear', 'bear', 'marsupial'],
                  'population': [1864, 22000, 80000]},
                  index=['panda', 'polar', 'koala'])

data = df.to_csv("catch_species.csv")
# data = df.to_dict()
print(data)

# for label, content in df.items():
#     print(f'label: {label}')
#     print(f'content: {content}', sep='\n')


# Todo: to create a file from scratch
data = pandas.read_csv("original_file")
data_dictionary = {["use specifics elements to create a dict"]}
data1 = pandas.DataFrame(data_dictionary)
data1.to_csv("new_file")