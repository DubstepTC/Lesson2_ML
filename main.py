import warnings
warnings.simplefilter("ignore")


%matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns

%config InlineBackend.figure_format = 'svg'

from pylab import rcParams
rcParams["figure.figsize"] = 8, 5 

import pandas as pd

df = pd.read_csv("Desktop/video_games_sales.csv").dropna()

# print(df.shape)

# df.info()

df["User_Score"] = df.User_Score.astype("float64")
df["Year_of_Release"] = df.Year_of_Release.astype("int64")
df["User_Count"] = df.User_Count.astype("int64")
df["Critic_Count"] = df.Critic_Count.astype("int64")


# table = [
#     "Name","Platform",
#     "Year_of_Release",  "Genre",
#     "Global_Sales","Critic_Score",
#     "Critic_Count","User_Score","User_Count","Rating",
# ]
# df[table].head()

# df[[x for x in df.columns if "Sales" in x] + ["Year_of_Release"]].groupby( 
#     "Year_of_Release"
# ).sum(). plot();

# df[[x for x in df.columns if "Sales" in x] + ["Year_of_Release"]].groupby( 
#     "Year_of_Release" 
# ).sum().plot(kind="bar", rot=45);

# sns.pairplot(
# df[["Global_Sales", "Critic_Score", "Critic_Count", "User_Score", "User_Count"]]
# );

# sns.distplot(df.Critic_Score);

# sns.jointplot(x="Critic_Score", y="User_Score", data=df, kind="scatter");

# top_platforms = df.Platform.value_counts().sort_values(ascending=False).head(5).index.values
# sns. boxplot(y="Platform", x="Critic_Score", data=df[df.Platform.isin(top_platforms)], orient="h") ;

platform_genre_sales =(
    df. pivot_table(
    index="Platform", columns="Genre", values="Global_Sales", aggfunc=sum
)
.fillna(0)
.applymap(float)
)
sns.heatmap(platform_genre_sales, annot=True, fmt=".1f", linewidths=0.5);
