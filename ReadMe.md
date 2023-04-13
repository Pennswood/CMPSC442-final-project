# HuB-AI: Smart Planner

## rbes-fitbit data branch

## CONTENTS OF THIS FILE

* Introductions
* Requirements
* Maintainers
* References

## INTRODUCTION

The purpose of this branch is to extract certain required data from Merged.xlsx to be used in the Octapy system in the Smart Planner.

Merged.xlsx is a combination of two files - sleepDay_merged.csv and dailyActivity_merged.csv, that contains data needed for our Octapy system. Other data from Fitbit database such as heartrate_seconds_merged.csv, minuteSleep_merged, etc. will not be used this time as the Fitbit database obtained from Kaggle is not consistent and not all database set contains same amount of users as other database set. Thus, we have decided to only use dataset with unit daily to ensure data compatibility when extracting them.

test.py enables the user to fetch certain data needed by referring to Id and date from user input. Id is is required to identify the user that will be used their data from and date is to ensure correct data is fetched since each user Id has multiple row of data of different day. 

## REQUIREMENTS

* Merged.xlsx
* python.py
* pandas module

## ISSUES

Date format - the date format in the csv file is different compared to what is written in the excel file. Still finding way to fix this

## MAINTAINERS

Current Maintainers:

* Noor Syafiqah Ahmad Sanusi: nxa5282@psu.edu
* Ahmad Alif Asyraf Abu Bakar: aja 6302@psu.edu

## REFERENCES

Below is the websites I used as references for this assignment:

* https://note.nkmk.me/en/python-pandas-multiple-conditions/
* https://www.geeksforgeeks.org/python-pandas-dataframe-at/
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html 
