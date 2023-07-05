
import pandas

# todo: create read cvs
data = pandas.read_csv("/Squirrel_Data.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel)
print(cinnamon_squirrel)
print(black_squirrel)

# todo: dict
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

#todo: create dataframe from scratch
data1 = pandas.DataFrame(data_dict)
data1.to_csv("squirrel_count.csv")


