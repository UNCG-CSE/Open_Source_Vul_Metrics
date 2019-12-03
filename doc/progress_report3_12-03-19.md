
## Introduction

For our project, we are working with data from Software Heritage and the National Vulnerability
Database (NVD). From Software Heritage, we are looking at the Software Heritage Graph Dataset. It is a public collection of open source software that
includes source code files and a graph that retraces the history of software development. "The dataset captures the state of
the Software Heritage archive on September 25th 2018, spanning a full mirror of Github and GitLab.com, the Debian
distribution, Gitorious, Google Code, and the PyPI repository. Quantitatively it corresponds to 5 billion unique file contents
and 1.1 billion unique commits, harvested from more than 85 million software origins" (Pietri et al. The Software Heritage
Graph Dataset: Public software development under one roof).

From the NVD, we are looking at software vulnerability information for all published CVE vulnerabilities since 2002. For each
CVE entry, the NVD provides a description of the vulnerability, affected software, impact ratings, and references to
advisories, solutions, and tools.


## Main Goals

We aim to explore the effects of software vulnerabilities on open source software, and vice versa.
With these datasets we hope to cross-reference GitHub (or other VCS) commits with software vulnerabilities themselves, as a direct connection between the two datasets is not clearly defined.
We intend to explore the interesting statistics between the vulnerabilities and software, including:
- How long does it take for a software vulnerability to be patched / addressed with a new software release after it's discovery?
- How does the rate of normal activity of an open source project repository relate to the time before addressing software vulnerabilities?
- Do overractive development periods in open source software cause the creation of more software vulnerabilities?
- Can we predict the amount of Releases from the amount of Revisions and Revision Date?
- How accurately can we predict vulnerability base scores using CVSS v2 and CVSS v3 metrics?
  - Which is more accurate? CVSS v2 or CVSS v3?


## Seth Goodwin
### Tasks
* Predict software vulnerability base scores using CVSS v3 metrics

### Work Done
#### [Predicting Vulnerability Base Scores with Multiple Regression]()
(10 hours)
* Question Asked:
  * Can we accurately predict software vulnerability base scores using CVSS v3 metrics?

First, I looked into one of the NVD's `.json` files to figure out which data and which columns were relevant to
my task. After determining which information was relevant, I read in all the NVD `.json` files and extracted the appropriate columns. The column `baseScore` was the dependent variable so I stored it in a dataframe on its own. Then I encoded each of the columns, which contained the features. The resulting dataframe contained 115818 rows / observations and 11 columns / features. The next step was to split the data up into training and testing data. I used `train_test_split` to select 70% of the data as training data and 30% of the data as testing data. I used a linear regression estimator and trained the model using the training data. Now that the model was trained, I could use it to make predictions. The root mean squared error was about 1.13 and the r-squared value was about 0.704. The root mean squared error value tells us that the model's predicted values, on average, will be no more than 1.13 units above or below the actual value. The r-squared value tells us that about 70.4% of of the data fits the model. One thing that could be done to improve the model's accuracy would be to determine any insignificant columns / features, if any, and remove them.

## Jaron Dunham
### Tasks
* Cluster NVD impact vectors to see if scores are accurately represented. (Task adjusted to use SVM Regression instead)
### Work Done
#### [Predicting Base Score using SVM Regression](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/blob/master/src/NVD/SVM_BaseScorePrediction.ipynb)
(8 hours)
* Question Asked:
  * Using the variables within cvssV2, would the base score be accurately predicted

 Attempting to figure out which machine learning algorithm to use was the most difficult task, I knew that since Base Score was an integer value that a regression algorithm would be needed, I ended up using Support Vector Machine (SVM), which helped with the multiple columns id be using for my input. Currently the predicted output I get are at the most 1.5 away from the actual value (inputs from the dataframe were used as an example to check the accuracy of the machine learning algorithm). Currently the algorithm is only reading from a single NVD file (which contains about 8000 rows of data), so using the rest of the files may provide more accurate results

## Gabriel Wilmoth
### Tasks
* Predict amount of Releases from amount of Revisions and Revisions date
### Work Done
#### [Model Creation and Statistics](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/blob/beta/src/Models/Linear%20Regression%20Releases%20from%20Revisions.ipynb)
(12 hours)
* Question Asked:
  * Looking at the amount of Revisions per week, can we accurately predict the amount of Releases in the following weeks to come?

In attempting to predict and model the task describe above I ran through the following. First I graphically represented both Revisions and Releases and then compared those graphs. Doing so I determined that there was a statistical relationship between the two datasets. Further work then went into removing outliers and prepping the data to be fit to a model. After prepping the data I was left with 90 rows (which is not a lot). Then, I took the approach of fitting a LinearRegression model to the data having X features of Revisions Count and Revisions Date and Y features of Releases Count. In training and testing the model I finished with a 86 for Mean Squared Error, which is not incredibly accurate and would need more data to lower the score.


## Rohit Gade
### Tasks
* To Predict the number of days to fix a vulnerability, based on number of users or contributors that exits in the the project.
### Work Done
#### [ Notebook Link ](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/blob/beta/src/Models/Users_to_fixs_model.ipynb)
(10 Hours)
* Question Asked:
  * Using the number of contributors in a project, can we predict the number of days it may take to fix a vulnerability in the project?

 The basic idea was to use a regression model to predict the no. of days to fix van (update_time). To first I took just the no. of contributors in a project and its corresponding update_time.So I splinted the dataset in train and test dataset and then to asses which model (Linear Regression or Random Forest Regression ) will perform better I preformed K-fold Crossvalidation with the training dataset with metric as R-square and but both of models performance was not satisfactory but between them Random Forest Regression was a bit better.So I tired to create a regression model based on Random forest Regression as my model but the  performance of the regression on the train and test dataset was very poor which means by model is underfitting the data. So to solve the problem I added some features to the model [ base score,attac_complexit,severity..etc ] to the dataset and again retrained the dataset using the random forest model and able to increase the R-Square value to 59.8. Which can be interpreted as the there is 60 present correlation between the  independent variables and the dependent variables in the model.
## Michael Follari
### Tasks
* Explore the differences in commit message content for release commits and revision commits.
* Find the most common words associated with release and revision commit messages.
* Create classification model to predict if a given message is likely to belong to a release or revision commit.
### Work Done
#### [Commit Message Language Processing / Modeling](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/blob/beta/src/3k-python/commit_NLP.ipynb)
(12 Hours)
* Question:
  * Is there a difference between the content of commit messages between release and revision commits? How do they differ?

 To explore the differences between the commit messages, I needed to first import the data. I was having trouble importing all 2GB of the revision data. I ran into Memory Errors and Kernel crashes. After utilizing many workarounds, I discovered I was running a 32-bit version of Python; this was the problem. Once imported from their respective csv files, `realease.csv` and `revision.csv`, I labeled the data as `"release"` and `"revision"`, respectively. The datasets were combined. Now, in order to begin training a classification model, I tokenized the dataset. I utilized sklearn's `TfidfVectorizer` function. Once tokenized, the data was split into testing and training data, using `train_test_split`. The model was trained using `RandomForestClassification`. After training, the confusion matrix and classification report were found. This method was generally straightforward, but involved some reformatting and refactoring of my code for subtle improvements. The confusion matrix showed that revisions were very easy to classify. Releases were classified with less accuracy, although not terrible. This may be due to the fact that there were roughly 10x more revision datapoints than releases; due to the nature of the ratios of these two datasets. The confusion matrix has high (near one) precision, recall, and f1-score for both release and revision. In addition to training a classification model, I wanted to explore the most common words in each commit message. I simply combined the token matrix and the vocabulary created by the tokenizer. Once combined, the lists can be vied to see the most common words, with their weighting. The most common word for release and revision were, unsurprisingly, `"release"` and `"update"`, respectively. The rest of the most common words follow this trend, generally. They are all words that you would imagine clearly indicate a release versus a patch.
