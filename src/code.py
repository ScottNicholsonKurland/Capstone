'''Predicting Austin Growth and Gentrification.


In this project, we will evaluate the performance and predictive power of a model that has been trained and tested on data collected from Austin. A model trained on this data that is seen as a good fit could then be used to predict Austin growth and gentrification.

The dataset for this project originates from Zillow Research and the Austin Open Data Portal. The data was collected from 2010-2016 and each of the entries represent aggregated data of a dozen features for homes - residential real estate - from Austin.

For the purposes of this project, the following preprocessing steps have been made to the dataset:'''


import numpy as np
import pandas as pd
from sklearn.cross_validation import ShuffleSplit
import visuals as vs
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


data = pd.read_csv('housing.csv')
prices = data['growth']
features = data.drop('growth', axis = 1)
    
print "Austin housing dataset has {} data points with {} variables each.".format(*data.shape)

'''
Data Exploration
In this section, we will take a look at the Austin housing data.

Since my goal is a model to predict the growth of Austin - new development, upzoning, densification et cetera - we have separated the dataset into features and the target variable. The features, 'RM', 'LSTAT', and 'PTRATIO', give us quantitative information about each data point. The target variable, 'growth', will be the variable we seek to predict. These are stored in features and growth, respectively.'''


minimum_price = np.min(prices)
maximum_price = np.max(prices)
mean_price = np.mean(prices)
median_price = np.median(prices)
std_price = np.std(prices)

print "Statistics for Austin housing dataset:\n"
print "Minimum price: ${:,.2f}".format(minimum_price)
print "Maximum price: ${:,.2f}".format(maximum_price)
print "Mean price: ${:,.2f}".format(mean_price)
print "Median price ${:,.2f}".format(median_price)
print "Standard deviation of prices: ${:,.2f}".format(std_price)


''''RM' is the average number of rooms among homes in the neighborhood.
'LSTAT' is the percentage of homeowners in the neighborhood considered "lower class" (working poor).
'PTRATIO' is the ratio of students to teachers in primary and secondary schools in the neighborhood.
Without building a model, let's try to figure out if an increase in the value of a feature would lead to an increase in the value of 'growth' or a decrease in the value of 'growth'.

'RM': An increase in the value of this feature will lead to an increase in the value of 'growth'. This is because for you'd expect a home with a higher number of rooms to be more expensive that a home with lower number of rooms.
'LSTAT': An increase in the value of this feature will lead to a decrease in the value of 'growth'. A lower class homeowner might not be able to afford expensive houses, so you'd expect them to leave in a cheaper home. A higher percentage of such people could correlate to cheaper homes in an area, and thus, a lower 'growth' value.
'PTRATIO': An increase in the value of this feature will lead to an decrease in the value of 'growth'. A low student to teacher ration is typically associated with better education level of a school, as a teacher is able to focus on individual students better (than if there were more students). So, due to the presence of better quality schools, people might be willing to pay more to live in those areas, to provide their children with better education, and the prices might be higher.
We can build scatter plots to see if our intuition is correct.'''


for var in features.columns:
    sns.regplot(data[var],prices)
    plt.show()



'''All three scatter plots above confirm our intuition.

Developing a Model
In this section of the project, we will develop the tools and techniques necessary for a model to make a prediction. Being able to make accurate evaluations of each model's performance through the use of these tools and techniques helps to greatly reinforce the confidence in your predictions.

Implementation: Define a Performance Metric
For this project, we will calculate the coefficient of determination, R2, to quantify our model's performance. The coefficient of determination for a model is a useful statistic in regression analysis, as it often describes how "good" that model is at making predictions.

The values for R2 range from 0 to 1, which captures the percentage of squared correlation between the predicted and actual values of the target variable. A model with an R2 of 0 is no better than a model that always predicts the mean of the target variable, whereas a model with an R2 of 1 perfectly predicts the target variable. Any value between 0 and 1 indicates what percentage of the target variable, using this model, can be explained by the features.

Let's define a function that returns the r2 score for given true and predicted data.'''


from sklearn.metrics import r2_score

def performance_metric(y_true, y_predict):
    """ Calculates and returns the performance score between 
        true and predicted values based on the metric chosen. """
    

    score = r2_score(y_true,y_predict)
    return score


'''Goodness of Fit
As an aside, assume that a dataset contains five data points and a model made the following predictions for the target variable:

True Value	Prediction
3.0	2.5
-0.5	0.0
2.0	2.1
7.0	7.8
4.2	5.3
Let's use the performance_metric function and calculate this model's coefficient of determination.'''


score = performance_metric([3, -0.5, 2, 7, 4.2], [2.5, 0.0, 2.1, 7.8, 5.3])
print "Model has a coefficient of determination, R^2, of {:.3f}.".format(score)

'''Model has a coefficient of determination, R^2, of 0.923.
The above model has a coefficient of determination, R2, of 0.923. Considering that the worse score for R2 is 0, and the best score is 1, a score of 0.923. This means that the model successfully captures more than 90 percent of the variation in the target variable. Though it is important to note that how good the score is, depends on the domain of the problem.

Shuffle and Split Data
Now we'll take the Austin housing dataset and split the data into training and testing subsets. Typically, the data is also shuffled into a random order when creating the training and testing subsets to remove any bias in the ordering of the dataset.'''


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features,prices,test_size=0.2,random_state=100)


'''Analyzing Model Performance
In this third section of the project, we'll take a look at several models' learning and testing performances on various subsets of training data. Additionally, we'll investigate the Decision Tree algorithm with an increasing 'max_depth' parameter on the full training set to observe how model complexity affects performance.

Learning Curves
The following code cell produces four graphs for a decision tree model with different maximum depths. Each graph visualizes the learning curves of the model for both training and testing as the size of the training set is increased. The shaded region of a learning curve denotes the uncertainty of that curve (measured as the standard deviation). The model is scored on both the training and testing sets using R2, the coefficient of determination.

_Note: The section uses helper functions supplied for the purposes of this project and available in the 'visuals' module.'''

# Produce learning curves for varying training set sizes and maximum depths
vs.ModelLearning(features, prices)

'''Looking at the learning curve for the model with max_depth = 3,

The score of the training curve decreases as more training points are added. This happens because with fewer training points, the model can modify its parameters to better approximate the targets; but as the number of training points increases, perfectly fitting them becomes more difficult, and the training score goes down.
The score of the training curve increases as more training points are added, but there's a slight dip after adding more than 350 training points. The score starts lower because the model has not yet learned enough to predict test points. As the model receives more training points, and hence, more information, it is better suited to predict unseen data.
The training and testing curve seem to be converging to a score of 0.8. This usually happens when the model has stretched its limits of extracting information from the training data even though more training points are being added. So the score stabilizes.
Therefore, having more training points might not benefit the model (with max_depth of 3).

Complexity Curves
The following code cell produces a graph for a decision tree model that has been trained and validated on the training data using different maximum depths. The graph produces two complexity curves — one for training and one for validation. Similar to the learning curves, the shaded regions of both the complexity curves denote the uncertainty in those curves, and the model is scored on both the training and validation sets using the performance_metric function.'''

vs.ModelComplexity(X_train, y_train)

'''Bias-Variance Trade off
Model trained with max_depth of 1: The model suffers from high bias at this depth. Looking at the graph, we can see that both training and validation scores are low, and similar. We can say that the model is over-simplified and is not capturing the underlying relationships present in the data for both training and validation datasets.

Model trained with max_depth of 10: The model suffers from high variance at this depth, and is over fitting on the training data. In the graph, we can see that the training score at this depth is almost equal to 1.0, while the validation score is lower, at around 0.7. The curves also seem to be diverging away from each other at this point.

In my opinion, a maximum depth of 3 results in a model that best generalizes to unseen data. That depth is the sweet spot for model complexity, as our model performs similarly on training and validation data, while the overall score for both is still relatively high between 0.7 and 0.8. A depth lower than that gives us poor training and validation score, while a higher depth over fits on the testing data, leading to a lower validation score.

Evaluating Model Performance
In this final section of the project, we will construct a model and make a prediction on the client's feature set using an optimized model from fit_model.

We'll be using Grid Search and Cross Validation techniques in this section.

Grid Search
The grid search technique is a systematic way of going through different combinations of parameter values while cross validating the results to determine the parameter combination which gives the best performance based on a scoring technique.

In order to optimize a learning algorithm, we can apply grid search by specifying the parameters, and the possible values of those parameters. The grid search then returns the best parameter values for our model, after fitting the supplied data. This takes out the guess-work involved in seeking out the optimal parameter values for a classifier.

Cross-Validation
The k-fold cross validation training technique is a way of splitting the dataset into k partitions of equal size, and then running k separate learning experiments on the training data. In each of the experiments, we chose a training set of the size of k-1 partitions, train our model on that partition, and evaluate the results on the remaining test data. The results/scores for the k experiments are then averaged out.

This technique is beneficial when using grid search to optimize a model because it allows us to look for parameter settings that perform well for different test sets. If we had a single testing set, it's easy to tune a model to perform well for that specific test set (and result in over fitting on the test set in this case), while cross validation allows us to generalize the results.

Fitting a Model
Now we'll bring everything together and train a model using the decision tree algorithm. To ensure that we are producing an optimized model, we will train the model using the grid search technique to optimize the 'max_depth' parameter for the decision tree. The 'max_depth' parameter can be thought of as how many questions the decision tree algorithm is allowed to ask about the data before making a prediction.'''


from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import make_scorer
from sklearn.grid_search import GridSearchCV

def fit_model(X, y):
    """ Performs grid search over the 'max_depth' parameter for a 
        decision tree regressor trained on the input data [X, y]. """
    
    # Create cross-validation sets from the training data
    cv_sets = ShuffleSplit(X.shape[0], n_iter = 10, test_size = 0.20, random_state = 0)

    # TODO: Create a decision tree regressor object
    regressor = DecisionTreeRegressor()

    # TODO: Create a dictionary for the parameter 'max_depth' with a range from 1 to 8
    params = {'max_depth': range(1,9)}

    # TODO: Transform 'performance_metric' into a scoring function using 'make_scorer' 
    scoring_fnc = make_scorer(performance_metric)

    # TODO: Create the grid search object
    grid = GridSearchCV(regressor,params,scoring_fnc,cv=cv_sets)

    # Fit the grid search object to the data to compute the optimal model
    grid = grid.fit(X, y)

    # Return the optimal model after fitting the data
    return grid.best_estimator_
'''Making Predictions
Once a model has been trained on a set of data, it can be used to make predictions on new sets of data. In the case of a decision tree regressor, the model has learned what the best questions to ask about the input data are, and can respond with a prediction for the target variable.

Optimal Model'''

# Fit the training data to the model using grid search
reg = fit_model(X_train, y_train)

# Produce the value for 'max_depth'
print "Parameter 'max_depth' is {} for the optimal model.".format(reg.get_params()['max_depth'])

'''Parameter 'max_depth' is 4 for the optimal model.
Answer: The optimal model has a max depth of 4, which is close enough to the previous guess of 3 earlier. Going back to the complexity graph, the model might perform better on the test set with a max depth of 4, but since the difference is minimal (which can also be due to noise), it might make sense to chose the simpler model.

Predicting Selling Prices
Imagine that you were a real estate agent in the Boston area looking to use this model to help price homes owned by your clients that they wish to sell. You have collected the following information from three of your clients:

Feature	Client 1	Client 2	Client 3
Total number of rooms in home	5 rooms	4 rooms	8 rooms
Neighborhood poverty level (as %)	17%	32%	3%
Student-teacher ratio of nearby schools	15-to-1	22-to-1	12-to-1
Let's see what prices our model will predict for these clients, and if they seem reasonable given the features.'''

# Produce a matrix for client data
client_data = [[5, 17, 15], # Client 1
               [4, 32, 22], # Client 2
               [8, 3, 12]]  # Client 3

# Show predictions
for i, price in enumerate(reg.predict(client_data)):
    print "Predicted selling price for Client {}'s home: ${:,.2f}".format(i+1, price)

'''Predicted selling price for Client 1's home: $401,333.33
Predicted selling price for Client 2's home: $240,947.37
Predicted selling price for Client 3's home: $893,700.00
The prices seem reasonable given the features of the homes. We can see that the highest priced home has the most rooms, lowest neighborhood poverty level, and the lowest student-teacher ratio, all of which make intuitive sense as discussed in Question 1. On the contrary, the home with the lowest number of rooms, highest neighborhood poverty level, and highest student-teacher ratio is priced the lowest in our predictions.

This finishes our project. We have built a decision tree regressor that performs reasonably well given the 3 features. But should the model should be used in a real-world setting? It probably shouldn't because:

The data collected in 1978 is not really relevant today due to rising population levels and changing population density of different areas.
The features present in the data that we built our model on are not likely be sufficient to describe a home. Examples of interesting features to look at may be proximity to city center, or neighborhood crime rate.
The data collected in an urban city will not be applicable in a rural city, because the people might value different aspects of a home depending on whether they live in an urban city or a rural area. For example, a person living in a rural city might value number of rooms in a home over the proximity to the city.'''
