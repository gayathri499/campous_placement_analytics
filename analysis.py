import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("placement_data.csv")

print(df.head())
print(df.describe())

sns.countplot(x="Placement_Status", data=df)
plt.title("Placement Distribution")
plt.show()

sns.boxplot(x="Placement_Status", y="CGPA", data=df)
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.show()