# election-analysis

## Election Audit Overview
This project, an election audit, delivers the election results of a US Congressional Precinct in Colorado. The Congressional Precinct is made up of three counties and three candidates participated in the race. The accompanying txt file delivers the number of votes cast for each of the three candidates as well as a per county breakdown of voter turnout. The ultimate aim of the project was to produce a script that would automate the results of this, and other similar elections in the future.

Final script delivers:
1. Total number of votes cast
2. List of candidates who received votes along with respective vote tallies and percentage of overall votes cast.
3. List of counties that voted along with turnout by county, and per county percentage of overall turnout.
4. Identifies county with the highest turnout
5. Identifies winner of the election based on popular vote
6. All results printed to accompanying election-analysis.txt file 
7. All results printed to command line

## Resources
- Data Source: election_results.csv
- Software: Python 2.7.16, Visual Studio Code 1.49.3
- Assistance and detailed walk through: Columbia Data Analysis Bootcamp

## Election Audit Results
There were three candidates running in a tri-county US Congressional Precinct in which 369,711 people voted.
Diana DeGette won the election with 73.8% of the vote (272,892 votes.)
Denver county cast the most votes, accounting for 82.8% of all votes (306,055 votes.)

The results, by candidate, were as follows:
- Raymon Anthony Doane: 3.1%, (11,606)
- Charles Casper Stockham: 23.0%, (85,213)
- Diana DeGette: 73.8%, (272,892)

The results, by county, were as follows:
- Jefferson: 10.5%, (38,855)
- Denver: 82.8%, (306,055)
- Arapahoe: 6.7%, (24,801)

## Election Audit Script: Future Use
This script can automate the tabulation of future elections with slight modification. Modifications may include:
- Changing file names to properly identify input and output files. the proper input file (lines 19, 22)
- If the headers of future input files don’t match current inputs: adjust indices referenced in the “for row” loop to find candidate and county names (lines 61, 64)


