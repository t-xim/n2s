from sklearn import metrics
import seaborn as sns 

confusion_matrix = metrics.confusion_matrix(y_test, predictions)


# Plotting confusion matrix
plt.figure(figsize=(10,10))
sns.heatmap(confusion_matrix, 
            annot=True, 
            fmt=".3f", 
            linewidths=.5, 
            square = True, 
            cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(metrics.accuracy_score(y_test, predictions))
plt.title(all_sample_title, size = 15);
