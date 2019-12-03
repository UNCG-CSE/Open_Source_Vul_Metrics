
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
- How long does it take for a software vulnerability to be patached / addressed with a new software release after it's discovery?
- How does the rate of normal activity of an open source project repository relate to the time before addressing software vulnereabilities?
- Do overractive development periods in open source software cause the creation of more software vulnerabilities?
- Can we predict the amount of Releases from the amount of Revisions and Revision Date?


## Seth Goodwin
### Tasks

### Work Done 

## Jaron Dunham 
### Tasks
* Cluster NVD impact vectors to see if scores are accurately represented. (Task adjusted to use SVM Regression instead)
### Work Done
#### [Predicting Base Score using SVM Regression](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/blob/beta/src/NVD/SVM_BaseScorePrediction.ipynb) 
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

In attempting to predict and model the task describe above I ran through the following. First I graphically represented both Revisions and Releases and then compared those graphs. Doing so I determined that there was a statistical relationship between the two datasets. Further work then went into removing outliers and prepping the data to be fit to a model. After prepping the data I was left with 90 rows (which is not a lot). Then, I took the approach of fitting a LinearRegression model to the data having X features of Revisions Count and Revisions Date and Y features of Releases Count. In training and testing the model I finished with a 86 for Mean Squared Error, which is not incredably accurate and would need more data to lower the score.


## Rohit Gade
### Tasks

### Work Done


## Michael Follari
### Tasks

### Work Done 
