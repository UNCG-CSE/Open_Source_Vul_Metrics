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

We aim to successfully cross-reference GitHub commits with software vulnerabilities. In doing so, hopefully we can compute the 
average time it takes from when a vulnerability is discovered to when it is patched and a new software version is released to the public. 
Maybe we can relate repository activity with how quickly a software bug is fixed or with the severity of the vulnerability.

## Seth Goodwin

From the SWHGD, I was looking into revision.csv from the popular-3k-python dataset. It "contains a subset of 3052 popular 
repositories tagged as being written in the Python language, from GitHub, Gitlab, PyPI and Debian" (SWHGD). The file had the 
following headers: id, date, date_offset, committer_date, committer_date_offset, type, directory, message, author, and 
committer. Of those, I was looking specifically at id (the Git SHA-1 hash of the commit), date (the date the commit was 
authored), and message (the commit message and description).

Before looking at the data, my first task was to clean up and decode the data. Some columns had a leading "/x", one column was 
stored as a unix timestamp, and one was in hex. After that I did some digging and found some interesting information. I found 
out which timestamps had the most commits, which years had the most commits, and which months, in the past five years, had 
the most commits.

My main task in looking into revision.csv was to somehow determine which commits (more than five billion) actually fixed a 
software vulnerability. Just to get a general feel, I filtered the commit messages for ones that directly address fixing a 
CVE. I searched for any commit message containing any variation of "F/fix/ed/es CVE" and found only 99... A future task would 
be to find a better criteria to filter the commit messages.

## Jaron Dunham 

My task is to take the National Vulnerability Database files and parse them into something easier to read, these NVD were 
given in JSON form instead of the normal CVS, so figuring out how to access each individual point took a little while. Because 
of the bullet point like format JSON files use (and there being the possiblity of more than one of the same bullet point), 
when extracting the information I have to go to each section, check for how many variables it contains and use that number to 
select the variable. I will continue to look for a better way to extract the information. Another issue is what format exactly 
do I want this information in, once again the bullet point-like format, trying to read the information in a chart seems like 
it would be difficult. The most feasible thing I can think of doing at the moment is splitting them into smaller charts, some 
type of join can be used if items needs to be references. 

## Gabriel Wilmoth

I mainly worked with the NVD National Vulnerability Dataset however, I also worked on the SHGD Software Heritage Graph 
Dataset. With my main task trying to find out how to connect the two datasets in a meaningful way. I've worked on the approach 
of parsing hashes from NVD and throwing the parsed information into a pandas data frame. Then I was able to join my data frame 
of NVD hashes and related information with a data frame of SHGD hashes and related information. The outcome of this merge has 
around 119 hashes in common, which is not a ton. However, we have to take into account that we are still working with a sample 
dataset and the number of connections between the two datasets can grow to a workable sample size. Another task I will be 
taking on is comparing the versions of the vulnerabilities from NVD to the GitHub versions from SHGD. All in all, trying to 
make more connections between the two datasets and find a connection that yields the most usable data or combination of 
connections.

## Rohit Gade

I have taken the task of converting this National Venerability Data set JSON files into a useful format.To do
that I have written a parser that reads specified NVD JSON file and selects parameters (Exp: cveid,
year,commit hash.etc). Since our data sets were huge like a 1 TB, we thought to first take small portion of
the data set and after final analization of it thought to scale it so for this reason parser at this stage 
only extracts the CVE's which has github commit urls. Later if can be modified to commit from other sources 
like git lab and Debian etc.

Next step is to down size the huge SHDS(Software Heritage Dataset), The idea is to use CVE's versions (a 
CVE has 2 versions one when the venerability starting version and venerability ending version) use SHDS data 
set to find the dates when the realized and store the commits in between, then search for the commit between 
the versions to find out which commit actuly fixed the version. Then calculate the date difference from that 
fixed commit to the nearest version realize. This will give a time period for each CVE which is fixed but 
has't be updated which exposes the typical users to a potential risk. This extracted date differences can be 
later analyzed to develop models determine how long might be exposed to a fixed venerability by giving 
certain parameter.  

## Michael Follari

When presented with the SWHGD, I initially explored the option in setting up a local PostgreSQL database to store the data.
After further exploration, it seemed unnneccesary at this point in the project, as we have little to no need of the largest 
parts of the SWHGD. In the future, if it is more convinient I am at a point I can easily import the data into the SQL database.

I turned my attention to the "release.csv" from the SWHGD. This data set contains information about the official releases of
the contained open source software projects. I am hoping that the release.csv will be a good dataset to explore as we are 
hoping to find commits that fix vulnerabilities. I am only working with the popular-3k-python dataset ("a subset of 3052 
popular repositories tagged as being written in the Python language, from GitHub, Gitlab, PyPI and Debian" (SWHGD)), as I am 
mostly exploring posibilities with the data.

I am focusing on correlating the frequencies of commits to the discovery of vulnerabilities. This means I am only concerned 
with commit dates. I have imported, cleaned, and created a frequency dateframe from the dataset. I have made simple graphs 
to get a sense of frequency vs. time. It appears that there are semi-regular spikes in frequency; this could be the result 
of the discovery of a new vulnerability.
I have also imported a select few datasets from NVD. I pulled out the "Published Date" from each vulnerability, and will
compare the date to the frequency of commits.

The goal of this is to connect the two datasets; to see if there is an obvious / clear time correlation between a discovered
vulnerability and change in frequency of releases. This would indicate a response/patch to the vulnerability. If that is the 
case, then we can immediately explore time correlation between the two datasets. If not, we can put more effort into other 
methods of connecting the two datasets.
