# Open Source Vulnerability Metrics

### Description:

Mining the [Software Heritage Graph Dataset](https://docs.softwareheritage.org/devel/swh-dataset/graph/dataset.html) a very large dataset containing the development history of publicly available software. The dataset links together source code files organized in directories, commits tracking evolution over time, up to full snapshots of version control systems (VCS) repositories.
* Includes a full dataset at 1.2TB and two "teaser" datasets: **popular-4k** at 27GB and **popular-3k-python** at 5.3 GB.
	* The popular-4k teaser contains a subset of 4000 popular repositories from GitHub, Gitlab, PyPI and Debian.
	* The popular-3k-python teaser contains a subset of 3052 popular repositories tagged as being written in the Python language, from GitHub, Gitlab, PyPI and Debian.

Our major goal is trying to cross-reference known software vulnerabilities found on the [National Vulneraibiltiy Database](https://nvd.nist.gov/) with commits found in the _Software Heritage Graph Dataset_. In doing so, hopefully we can answer some of the following questions: <br/>
* How long is there between when a software bug is discovered and when it is patched?
* How long is there between a fix and a new software release?
* Is there a relationship between project activity and vulnerability severity?
***

### Team Abracadata  
Instructor: [Dr. Somya Mohanty](https://github.com/somyamohanty) <br/>
Mentor: [Dr. Steven Tate](https://www.uncg.edu/cmp/faculty/srtate/) <br/>
#### Members and Tasks:
* [Seth Goodwin](https://github.com/SethGoodwin)
	* cleaning and understanding `revision.csv`, from popular-3k-python dataset
		* determine if any irregularities/anomalies in the data
		* looking into commit messages, trying to find commits that fix CVE's
		* link commit ids (ones that fix CVE's) with NVD
  	* determine how long it takes the NVD to report on software vulnerabilities
		* how responsive is the NVD?
		* basic statistical analysis (mean, standard deviation, etc.) of data
		* distribution modeling
		* hypothesis testing
	* building machine learning model to predict software vulnerability base scores
		* using **CVSS v3** metrics, train multiple linear regression model (70/30 training/testing split)
		* evaluate model accuracy using root mean squared error and r-squared value
* [Michael Follari](https://github.com/stonefollari)
	* looking through and cleaning `release.csv`, from popular-3k-python dataset
		* explore time dependence between `release.csv` and NVD
* [Jaron Dunham](https://github.com/JaronDunham)
	* parsing NVD JSON files into CSV files
		* extracting the nested information within NVD
	* Comparing Frequency of Commits (SWHGD) to Base Score (NVD)
		* attempted to see if the rising or lowering of the base score affected the frequency of commits 
	* Attempting to predict Base Score using variables from CVSS v2 metrics
* [Gabe Wilmoth](https://github.com/GabeWilmoth)
	* Trying to connect NVD with SWHGD
	* Look into Relationship between Releases and New Vulnerabilities
	* Predict count of Releases from count of Revisions and Date of Revisions
		* Looking at the amount of Revisions per week, can we accurately predict the amount of Releases in the following week(s) to come?
* [Rohit Gade](https://github.com/rohitreddygade)
	* extracting GitHub hash id from links found on the NVD
	* Create a dataset from NVD and SHDS to analize who long is there between when a software bug is discovered and when it is patched?
	* Develop a model to predict the patch duration.

***
