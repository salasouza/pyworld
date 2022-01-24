library('randomForest')
library('Metrics')

data<-read.csv("train.csv",stringsAsFactors= T)

dim(data)

data$Y<-as.factor(data$Y)

train<-data[1:2000,]
test<-data[2001:3000,]


model_rf<-randomForest(Y~.,data=train)

preds<-predict(object=model_rf,test[,-101])

table(preds)

auc(preds,test$Y)

#

all<-rbind(train,test)

Cluster <- kmeans(all[,-101], 5)

all$cluster<-as.factor(Cluster$cluster)

train<-all[1:2000,]
test<-all[2001:3000,]

model_rf<-randomForest(Y~.,data=train)

preds2<-predict(object=model_rf,test[,-101])

table(preds2)

auc(preds2,test$Y)
