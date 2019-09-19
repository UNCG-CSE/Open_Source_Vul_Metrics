# Open Source Vulnerability Metrics

### Description: 

Mining the [_Software Heritage Graph Dataset_](https://docs.softwareheritage.org/devel/swh-dataset/graph/dataset.html); a very large dataset containing the development history of publicly available software. The dataset links together source code files organized in directories, commits tracking evolution over time, up to full snapshots of version control systems (VCS) repositories. 
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
Members:
* [Seth Goodwin](https://github.com/SethGoodwin)
	* looking through and cleaning `revision.csv`
* [Michael Follari](https://github.com/stonefollari)
	* looking through and cleaning `release.csv`
* [Jaron Dunham](https://github.com/JaronDunham)
	* parsing NVD data into useful and relevant data
* [Gabe Wilmoth](https://github.com/GabeWilmoth)
	* trying to connect NVD with SWHGD 
* [Rohit Gade](https://github.com/rohitreddygade)
	* extracting GitHub hash id from links found on the NVD

***
