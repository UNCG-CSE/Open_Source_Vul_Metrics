
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
### Tasks
* More data wrangling and cleaning 
	* Extracting relevent data nested within datasets
* Determine if correlation between vulnerability publish date and commit patch date
* Hypothesis testing to determine delay between vulnerability patch and vulnerability info being 
published

### Work Done - [notebook](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/blob/master/src/statistical_analysis.ipynb)

#### Data Cleaning (~7 hours)
I first had to read in and extract the necessary columns from the nested NVD .JSON data. One 
column containted all the reference urls for each of the vulnerabilities. I had to extract the 
GitHub commit urls, ones that patched a software vulnerability, and then had to get the commit 
date from each page. I've wrote various functions to extract the needed data.

#### Correlation Exploration and Distribution Modeling (~5 hours)
I originally plotted a superimposed histogram comparing hourly commits with monthly 
vulnerability discoveries... this didn't yield much. I then focused on software vulnerabilities 
that have been patched specificallly by a GitHub commit. I then plotted vulnerability publish 
date with commit patch date and this yielded interesting results. I also plotted vulnerabilites 
per month and delay between patch and vulnerability publish date and fit a curve to both. Lastly 
I looked at the correlation between commits and vulnerabilty publish date.

#### Hypothesis Testing (~3 hours)
I plotted histograms and performed a one sample z-test to test my null hypothesis. The resulting p-value was significantly less than the significance level. Therefore I can reject my null hypothesis and lean towards the alternative hypothesis. In other words, the average time it takes the NVD to publish new vulnerability info after a GitHub patch is greater than 4 months.
## Jaron Dunham 
### Tasks
- Complete Algorithm to convert NVD JSON files to CSV
- Determine link between severity during a period of time and frequecy of release

#### NVD JSON
- I originally had an algorith that would search through each part of the JSON file and parse it 
into CSV, as i said in the first progress report, I was sure that there was a much easier way to 
do it, so I sent time working on that until I found json_normalize. This pretty much did all that 
i asked for, the only thing I needed to deal with was the arrays within the file, which remained 
nested.

#### Severity vs. Frequency of Release 
- I was tasked to see if there was any link between the severity (or base score) from the NVD
database, and if the high it was caused for more frequent commits (~5 hours) 
With the graph that I currently have, I do not see anything that would make me think that these 
two parameters are linked in anyway. The graph that display the entire timeframe also shows that 
commits ingeneral a more common as time goes on, so that can effect our results. And the graph 
with a small timeframe show no corelation. Different distributions needs to used to see if there 
are any corelations that I am missing.

## Gabriel Wilmoth
### Tasks
* Download Data and Setup Babbage Server
* Data Cleaning, Exploration, and Connecting 
	* Pulling message data from NVD and try to connect to SHD
* Exploration of Correlation between spike in releases and new vulnerabilities
	* Normalize New Vulnerabilities to fit a normal distribution
	
### Work Done 

##### Downloading Full Dataset and Server Setup
(5 hours)
I downloaded the Full Software Heritage Dataset (SHD) which took about a day and not factored into time. Then the process of working on the Babbage UNCG server to process all this data ensued. I encountered several issues from permissions to timming out when trying to process all of the data. Eventually we settled on using DASK for parallel processing to hopefully speed up the processing of data before we were timed out.

#### [Data Cleaning, Exploration, and Connecting](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/tree/master/data/NVD-to-CSV-Descriptions)
(3 hours)
In trying to connect even more of NVD and SHD I had the idea of comparing NVD descriptions to SHD commit messages. In doing so work had to be done towards parsing out the descriptions from NVD JSONs for 2005-2018. After parsing out the description messages it was then a process of comparing them already parsed SHD commit messages.

#### [Exploration of Correlation between Spike in Releases and New Vulnerabilities](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/blob/master/src/(GW%20Project%20pt.2)%20Correlation%20between%20spike%20in%20releases%20and%20new%20vulnerabilities.ipynb)
(10 hours)
In an attempt to gain further insight into our data and the connection between the two datasets, I was tasked to look into the above relation. The goal was to first gather useful statistics for New Vulnerabilites and fit it to a normal distribution, in doing so I took a look at the about of New Vulnerabilities per week. After that I compared the graphs of Vulnerabilities and Releases and observed some interesting results. I then attempted to normalize Releases for a given time period and was successful. However, I wasn't able to normalize Vulnerabilities for the same time period thus I wasn't able to follow through with Hypothesis Testing. Although, I was able to draw some interesting conclusions and create Null and Alternative Hypotheses.

## Rohit Gade
### Tasks
Analaize Co-relation between Revision and Release [notebook](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/blob/beta/src/3k-python/Rev%20Rel%20Com.ipynb)  (Extraction of Data -1hr,  Research,Ploting and Exploration: 2hr):3hr<br>
Analaysis between Commits ( Vulnerability fixes ) dates and Release dates [notebook](https://github.com/UNCG-CSE/Open_Source_Vul_Metrics/blob/beta/src/NVD/Anaz_Commit_Releases.ipynb) (Extration of Data: 4-5 Hr, Research Applying Distribution and ploting:3hr ) :8Hr<br>
### Work Done
Analaize Co-relation between Revision and Release<br>
- I tried to plot the graphs correspoing to number of release and commits per day along along year.basicly trying to find any corelaiotn between both of then in general. If exist how how it can be related to Vulnerabiliy fixs commits and Relases.<br>
Analaysis between Commits ( Vulnerability fixes ) dates and Release dates<br>
- Main objective was to understand how long do it take for a fix to be released based on the how active does the repo or the opensoruce project is? So first list of vul. were collected from nvd dataset and its correspoing commits and releases data was extracted from SHDS and github.then
tried to fit a distribution model (Norm. Dist.) to the data.But observed thay 1/3rd of the dates was  between the commit and releases were not ralistic. and have to fix why it happend.

## Michael Follari
### Tasks
- Explore the correlation between vulnerabiliies and releases.
- Formulate appropraite hypothesis to determine if vulnerabilities has some effect on releases.

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



