import pandas as pd
from fuzzywuzzy import fuzz
import timeit # can you add code to measure performance


def get_matches(list1, list2):
    return [x for x in list1 if x in list2]


def get_fuzzy_match(list1, list2, treshold):

    matches = []

    for i1 in list1:
        for i2 in list2:
            ratio = fuzz.token_set_ratio(i1, i2) #also we need to try: fuzz.ratio fuzz.partial_ratio fuzz.token_sort_ratio fuzz.token_set_ratio
            if ratio >= treshold:
                matches.append([i1, i2, ratio])#append i2

    return matches


def write_list_to_file(filename, list):
    f = open(filename, "w")

    for item in list:
        f.write("{}\n".format(item))



if __name__ == "__main__":
    # Broken, fix read_csv arguments (http://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options)
    # Also, download the panamapapers: https://offshoreleaks.icij.org/pages/database
    # Download "archive of all files" (.csv files). We only need the files that contain names of companies and individuals. 

    panama_df = pd.read_csv('panama.csv') # $ cat panamafile.csv | cut -d, -f1 >panama.csv
    organizations = panama_df.values #the output looks ugly, but it's ok for now.


    # Public Tenders and Contracts, Open Gov Canada, filename: "Complete file: 2009 to today" download from http://open.canada.ca/data/en/dataset/53753f06-8b28-42d7-89f7-04cd014323b0
    
    canada_df = pd.read_csv('canada.csv') # $ cat canada.csv | cut -d, -f1 >panama.csv
    contractors = canada_df.values #the output looks ugly, but it's ok for now.

    matches = get_fuzzy_match(contractors, organizations, 70)

    write_list_to_file("matches.txt", matches)
