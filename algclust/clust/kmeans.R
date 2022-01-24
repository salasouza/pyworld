library(ggplot2)
library(cluster)

df <- read.csv(file='locallake/raw/iris.csv')

head(df)

str(df)

irisCluster <- kmeans(df[,1:4], center=3, nstart=20)
irisCluster


table(irisCluster$cluster, df$variety)

clusplot(df, irisCluster$cluster, color=T, shade=T, labels=0, lines=0)


tot.withinss <- vector(mode="character", length=10)

for (i in 1:10){
  irisCluster <- kmeans(df[,1:4], center=i, nstart=20)
  tot.withinss[i] <- irisCluster$tot.withinss
}


plot(1:10, tot.withinss, type="b", pch=19)

ggplot(df, aes(Petal.Length, Petal.Width)) + geom_point(aes(col=variety), size=4)

install.packages('IRkernel') 
IRkernel::installspec()
IRkernel::installspec(user = FALSE)
