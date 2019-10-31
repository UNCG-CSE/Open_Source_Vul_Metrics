
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


## Seth Goodwin

## Jaron Dunham 
### Task
- Complete Algorithm to convert NVD JSON files to CSV
- Determine link between severity during a period of time and frequecy of release
#### NVD JSON
- I originally had an algorith that would search through each part of the JSON file and parse it into CSV, as i said in the first progress report, I was sure that there was a much easier way to do it, so I sent time working on that until I found json_normalize. This pretty much did all that i asked for, the only thing I needed to deal with was the arrays within the file, which remained nested.
#### Severity vs. Frequency of Release 
- I was tasked to see if there was any link between the severity (or base score) from the NVD database, and if the high it was caused for more frequent commits (~5 hours) 
With the graph that I currently have, I do not see anything that would make me think that these two parameters are linked in anyway. The graph that display the entire timeframe also shows that commits ingeneral a more common as time goes on, so that can effect our results. And the graph with a small timeframe show no corelation. Different distributions needs to used to see if there are any corelations that I am missing. 

## Gabriel Wilmoth

## Rohit Gade

## Michael Follari
### Task
- Explore the correlation between vulnerabiliies and releases.
- Formulate appropraite hypothesis to determine if vulnerabilities has some effect on relases.

### Work Done 

##### Releases CSV Exploration
- Exploration, Graphing, Functions to easily explore (4 hour).
I kept my focus on the releases.csv file. The aim was to better understand the releases and determine if time based correlation between relases and NVD could be made. With this, test vulnerabiulity and releases hypothesis.
The releases vary greatly with time; since open source software / version control software has grown greatly in popularity with time. I found that the largest and most consistent spread of time that I could analyze was Jan. 1st 2016 to Jan. 1st 2018.

##### Reading of NVD, Vulnerabilities
- Functions to read, parse, clean, and others to parse NVD data and vulnerabilities (3 hours).
I found all I needed from NVD (Vulnerability Dataset) for my analysis was the publish date and the vulnerability score. I created functions to loop through the csv files and read in just the. Resampled vulnerabilities by week, by `count`.

##### Exploring Vulnerability and Release
- Function creation, parameter variation for best analysis (days) (6 hours)
Created functions to find different statistics of the releases or vulnerabilities. Created functions to look days ahead in the dataset and calculate count of different periods. For each of the weeks with most/least vulnerabilities, explored different time steps in analysis (how many days ahead to look for increased releases), found the number of releases in the following week.

##### Hypothesis Testing
- Plotted histograms, formatted graphs, calculated statistics and correlations of the sets, two sample t-test for hypothesis (7 hours).
I found that there is no correlation and the amount of vulnerability discoveries does not affect the number of releases in the same/following weeks.



