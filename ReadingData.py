#Author: Brandon Hansen, csBrandonHansen@gmail.com
#Tools/Libraries: SQlite, Python, NumPy, MatPlotLib
#Dataset: This sample SQlite data set was taken from --> http://2016.padjo.org/tutorials/sqlite-data-starterpacks/

#This project was created by using data manipulation and visualization. The projects sole purpose was to query data from
#a table and use that data to create a visualization to find the county that has the best SAT takers in the state of California
#during a testing season. The data is slightly outdated, the new SAT test is out of 1600 and the data is based off of the
#old grading SAT criteria, which was out of 2440. An application of the visualization provided by this project could be
#parents trying to find the best school system for their children in the state of California.

import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import random
import datetime
import time
import collections
import operator


# The read_in_data and print_noncombined_data are both functions that were used to originally
# manipulate the original data that was inside of the SQlite table.
# Both of these functions were essentially used to just analyze
# the data and look at it and analyze it

def read_in_data():
    connection = sqlite3.connect('C:\\Users\\brans\\Documents\\Programming\PyCharm\\untitled\\cdeschools.sqlite')
    cursor = connection.cursor()

    for row in cursor.execute(
            'SELECT DISTINCT cname, AvgScrRead, AvgScrMath, AvgScrWrite FROM satscores WHERE AvgScrRead AND cname IS NOT NULL;'):
        print(row)

    connection.close()


def print_noncombined_data():
    read_in_data()


# After I analyzed the data, I had the SQlite table open and started to query specific points in the dataset
# that I needed to get the average SAT score by specific County.
# I query'ed The reading scores, math scores, and writing scores from distinct county within California.
# I will leave an example below of my query and how I obtained the data.

# QUERY EXAMPLE -->
# --Average Reading Score From Each County
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE cname = 'Alameda'
# --                                                AND AvgScrRead IS NOT NULL;
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE cname = 'Amador'
# --                                                AND AvgScrRead IS NOT NULL;
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE cname = 'Butte'
# --                                                AND AvgScrRead IS NOT NULL;
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE AvgScrRead IS NOT NULL
# --                                                AND cname = 'Calaveras';
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE cname = 'Colusa'
# --                                                AND AvgScrRead IS NOT NULL;
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE AvgScrRead IS NOT NULL
# --                                                AND cname = 'Contra Costa';
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE cname = 'Del Norte'
# --                                                AND AvgScrRead IS NOT NULL;
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE cname = 'El Dorando'
# --                                                AND AvgScrRead IS NOT NULL;
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE cname = 'Fresno'
# --                                                AND AvgScrRead IS NOT NULL;
# -- SELECT ROUND(AVG(AvgScrRead)) FROM satscores WHERE cname = 'Glenn'
# --                                                AND AvgScrRead IS NOT NULL;

# This is how I essentially got my needed data from the dataset. I did this for every single distinct county
# for each score, changing the score type from the query got me all of my data. There might have been an easier way to
# Obtain the data but I found that this was the easiest way for me. I might have been able to use a UNION or left join
# to combine columns together and get the data more elegantly.


# After I query'ed all of the data I put each score inside of a specific variable name that I will later use in a
# method that will get me my average SAT score from each county.
# This data below is getting me Average Reading Score from each county.
# There was a small bug in the dataset, there was null values for one of the counties. It did not impact the final result
Alameda_average_reading = 482
Amador_average_reading = 523
Butte_average_reading = 510
Calaveras_average_reading = 530
Colusa_average_reading = 466
Contra_Costa_average_reading = 488
Del_Norte_average_reading = 478
El_Dorado_average_reading = 537
Fresno_average_reading = 441
Glenn_average_reading = 471
Humboldt_average_reading = 532
Imperial_average_reading = 460
Inyo_average_reading = 493
Kern_average_reading = 459
Kings_average_reading = 447
Lake_average_reading = 484
Lassen_average_reading = 489
Los_Angeles_average_reading = 451
Madera_average_reading = 475
Marin_average_reading = 536
Mariposa_average_reading = 534
Mendocino_average_reading = 512
Merced_average_reading = 441
Modoc_average_reading = 502
Mono_average_reading = 487
Monterey_average_reading = 477
Napa_average_reading = 488
Nevada_average_reading = 548
Orange_average_reading = 511
Placer_average_reading = 528
Plumas_average_reading = 516
Riverside_average_reading = 464
Sacramento_average_reading = 480
San_Benito_average_reading = 485
San_Bernardino_average_reading = 465
San_Diego_average_reading = 497
San_Francisco_average_reading = 460
San_Joaquin_average_reading = 474
San_Luis_Obispo_average_reading = 534
San_Mateo_average_reading = 521
Santa_Barbara_average_reading = 502
Santa_Clara_average_reading = 527
Santa_Cruz_average_reading = 538
Shasta_average_reading = 523
Sierra_average_reading = 9999999999999  # No data for this county, was not provided in the data set.
Siskiyou_average_reading = 513
Solano_average_reading = 495
Sonoma_average_reading = 509
Stanislaus_average_reading = 477
Sutter_average_reading = 488
Tehama_average_reading = 477
Trinity_average_reading = 499
Tulare_average_reading = 448
Tuolumne_average_reading = 517
Ventura_average_reading = 513
Yolo_average_reading = 502
Yuba_average_reading = 474

# Math Scores, bascially the same thing that I did above but just with the Average Math Scores.
Alameda_average_math = 498
Amador_average_math = 511
Butte_average_math = 504
Calaveras_average_math = 526
Colusa_average_math = 459
Contra_Costa_average_math = 494
Del_Norte_average_math = 509
El_Dorado_average_math = 539
Fresno_average_math = 442
Glenn_average_math = 473
Humboldt_average_math = 513
Imperial_average_math = 463
Inyo_average_math = 502
Kern_average_math = 465
Kings_average_math = 442
Lake_average_math = 474
Lassen_average_math = 503
Los_Angeles_average_math = 456
Madera_average_math = 462
Marin_average_math = 539
Mariposa_average_math = 550
Mendocino_average_math = 496
Merced_average_math = 442
Modoc_average_math = 504
Mono_average_math = 478
Monterey_average_math = 467
Napa_average_math = 473
Nevada_average_math = 535
Orange_average_math = 529
Placer_average_math = 528
Plumas_average_math = 531
Riverside_average_math = 466
Sacramento_average_math = 486
San_Benito_average_math = 486
San_Bernardino_average_math = 469
San_Diego_average_math = 499
San_Francisco_average_math = 485
San_Joaquin_average_math = 474
San_Luis_Obispo_average_math = 529
San_Mateo_average_math = 540
Santa_Barbara_average_math = 510
Santa_Clara_average_math = 549
Santa_Cruz_average_math = 524
Shasta_average_math = 530
Sierra_average_math = 999999999999  # No data for this county, was not provided in the data set.
Siskiyou_average_math = 506
Solano_average_math = 502
Sonoma_average_math = 516
Stanislaus_average_math = 476
Sutter_average_math = 490
Tehama_average_math = 482
Trinity_average_math = 490
Tulare_average_math = 449
Tuolumne_average_math = 506
Ventura_average_math = 520
Yolo_average_math = 500
Yuba_average_math = 481

# Writing Scores, same thing as above.
Alameda_average_writing = 482
Amador_average_writing = 503
Butte_average_writing = 486
Calaveras_average_writing = 513
Colusa_average_writing = 453
Contra_Costa_average_writing = 487
Del_Norte_average_writing = 466
El_Dorado_average_writing = 516
Fresno_average_writing = 435
Glenn_average_writing = 471
Humboldt_average_writing = 505
Imperial_average_writing = 449
Inyo_average_writing = 474
Kern_average_writing = 449
Kings_average_writing = 436
Lake_average_writing = 475
Lassen_average_writing = 482
Los_Angeles_average_writing = 449
Madera_average_writing = 459
Marin_average_writing = 534
Mariposa_average_writing = 513
Mendocino_average_writing = 490
Merced_average_writing = 439
Modoc_average_writing = 487
Mono_average_writing = 484
Monterey_average_writing = 465
Napa_average_writing = 482
Nevada_average_writing = 526
Orange_average_writing = 508
Placer_average_writing = 513
Plumas_average_writing = 496
Riverside_average_writing = 456
Sacramento_average_writing = 470
San_Benito_average_writing = 477
San_Bernardino_average_writing = 456
San_Diego_average_writing = 484
San_Francisco_average_writing = 453
San_Joaquin_average_writing = 467
San_Luis_Obispo_average_writing = 512
San_Mateo_average_writing = 518
Santa_Barbara_average_writing = 493
Santa_Clara_average_writing = 527
Santa_Cruz_average_writing = 523
Shasta_average_writing = 505
Sierra_average_writing = 99999999999999999  # No data for this county, was not provided in the data set.
Siskiyou_average_writing = 487
Solano_average_writing = 485
Sonoma_average_writing = 505
Stanislaus_average_writing = 467
Sutter_average_writing = 467
Tehama_average_writing = 454
Trinity_average_writing = 464
Tulare_average_writing = 444
Tuolumne_average_writing = 502
Ventura_average_writing = 505
Yolo_average_writing = 490
Yuba_average_writing = 463


# This function helped me get the data that I truly wanted from all of the querys that I did.
# This method simply just adds the average reading, math, and writing scores from each county and prints out what the
# average is. Basically just pieced the above data together.
def get_sat_score(reading, math, writing, county):
    score = reading + math + writing
    return print(county + " Average SAT Score is " + str(score))


# The code below is really "Brute Forced" but I made the decision to go along with it just in case I ever wanted to come
# back and work on this data set. The following 60 or so lines simply prints out the exact average SAT score from each
# county. If there was an update in the data, lets say a new dataset came out on SAT scores in California for the 2020
# testing season. I could get the new data that I need so easily by just changing some variable definitions.
Alameda = get_sat_score(Alameda_average_writing, Alameda_average_math, Alameda_average_reading, "Alameda")
Amador = get_sat_score(Amador_average_math, Amador_average_reading, Amador_average_writing, "Amador")
Butte = get_sat_score(Butte_average_writing, Butte_average_math, Butte_average_reading, "Butte")
Calaveras = get_sat_score(Calaveras_average_math, Calaveras_average_writing, Calaveras_average_reading, "Calaveras")
Colusa = get_sat_score(Colusa_average_math, Colusa_average_reading, Colusa_average_writing, "Colusa")
ContraCosta = get_sat_score(Contra_Costa_average_math, Contra_Costa_average_writing, Contra_Costa_average_reading,
                            "Contra Costa")
DelNorte = get_sat_score(Del_Norte_average_reading, Del_Norte_average_math, Del_Norte_average_writing, "Del Norte")
ElDorado = get_sat_score(El_Dorado_average_math, El_Dorado_average_writing, El_Dorado_average_writing, "El Dorado")
Fresno = get_sat_score(Fresno_average_math, Fresno_average_reading, Fresno_average_writing, "Fresno")
Glenn = get_sat_score(Glenn_average_math, Glenn_average_reading, Glenn_average_writing, "Glenn")
Humboldt = get_sat_score(Humboldt_average_math, Humboldt_average_reading, Humboldt_average_writing, "Humboldt")
Imperial = get_sat_score(Imperial_average_math, Imperial_average_reading, Imperial_average_writing, "Imperial")
Inyo = get_sat_score(Inyo_average_math, Inyo_average_reading, Inyo_average_writing, "Inyo")
Kern = get_sat_score(Kern_average_math, Kern_average_reading, Kern_average_writing, "Kern")
Kings = get_sat_score(Kings_average_math, Kings_average_reading, Kings_average_writing, "Kings")
Lake = get_sat_score(Lake_average_math, Lake_average_reading, Lake_average_writing, "Lake")
Lassen = get_sat_score(Lassen_average_math, Lassen_average_reading, Lassen_average_writing, "Lassen")
LosAngeles = get_sat_score(Los_Angeles_average_math, Los_Angeles_average_writing, Los_Angeles_average_reading,
                           "Los Angeles")
Madera = get_sat_score(Madera_average_math, Madera_average_reading, Madera_average_writing, "Madera")
Marin = get_sat_score(Marin_average_math, Marin_average_reading, Marin_average_writing, "Marin")
Mariposa = get_sat_score(Mariposa_average_math, Mariposa_average_reading, Mariposa_average_writing, "Mariposa")
Mendocino = get_sat_score(Mendocino_average_math, Mendocino_average_writing, Mendocino_average_reading, "Mendocinio")
Merced = get_sat_score(Merced_average_math, Merced_average_writing, Merced_average_reading, "Merced")
Modoc = get_sat_score(Modoc_average_math, Modoc_average_reading, Modoc_average_writing, "Modoc")
Mono = get_sat_score(Mono_average_math, Mono_average_reading, Mono_average_writing, "Mono")
Monterey = get_sat_score(Monterey_average_math, Monterey_average_reading, Monterey_average_writing, "Monterey")
Napa = get_sat_score(Napa_average_math, Napa_average_reading, Napa_average_writing, "Napa")
Nevada = get_sat_score(Nevada_average_math, Nevada_average_reading, Nevada_average_writing, "Nevada")
Orange = get_sat_score(Orange_average_math, Orange_average_writing, Orange_average_reading, "Orange")
Placer = get_sat_score(Placer_average_math, Placer_average_reading, Placer_average_writing, "Placer")
Plumas = get_sat_score(Plumas_average_math, Plumas_average_reading, Plumas_average_writing, "Plumas")
Riverside = get_sat_score(Riverside_average_math, Riverside_average_reading, Riverside_average_writing, "Riverside")
Sacramento = get_sat_score(Sacramento_average_math, Sacramento_average_reading, Sacramento_average_writing,
                           "Sacramento")
SanBenito = get_sat_score(San_Benito_average_math, San_Benito_average_reading, San_Benito_average_writing, "San Benito")
SanBernardino = get_sat_score(San_Bernardino_average_math, San_Bernardino_average_reading,
                              San_Bernardino_average_writing, "San Bernardino")
SanDiego = get_sat_score(San_Diego_average_math, San_Diego_average_reading, San_Diego_average_writing, "San Diego")
SanFrancisco = get_sat_score(San_Francisco_average_math, San_Francisco_average_reading, San_Francisco_average_writing,
                             "San Francisco")
SanJoaquin = get_sat_score(San_Joaquin_average_math, San_Joaquin_average_reading, San_Joaquin_average_writing,
                           "San Joaquin")
SanLuisObispo = get_sat_score(San_Luis_Obispo_average_math, San_Luis_Obispo_average_reading,
                              San_Luis_Obispo_average_writing, "San Luis Obispo")
SanMateo = get_sat_score(San_Mateo_average_math, San_Mateo_average_reading, San_Mateo_average_writing, "San Mateo")
SantaBarbara = get_sat_score(Santa_Barbara_average_math, Santa_Barbara_average_reading, Santa_Barbara_average_writing,
                             "Santa Barbara")
SantaClara = get_sat_score(Santa_Clara_average_math, Santa_Clara_average_reading, Santa_Clara_average_writing,
                           "Santa Clara")
SantaCruz = get_sat_score(Santa_Cruz_average_math, Santa_Cruz_average_reading, Santa_Cruz_average_writing, "Santa Cruz")
Shasta = get_sat_score(Shasta_average_math, Shasta_average_reading, Shasta_average_writing, "Shasta")
Sierra = "DATA NOT FOUND!!!"
Siskiyou = get_sat_score(Siskiyou_average_math, Siskiyou_average_reading, Siskiyou_average_writing, "Siskiyou")
Solano = get_sat_score(Solano_average_math, Solano_average_reading, Solano_average_writing, "Solano")
Sonoma = get_sat_score(Sonoma_average_math, Sonoma_average_reading, Sonoma_average_writing, "Sonoma")
Stanislaus = get_sat_score(Stanislaus_average_math, Stanislaus_average_reading, Stanislaus_average_writing,
                           "Stanislaus")
Sutter = get_sat_score(Sutter_average_math, Sutter_average_reading, Sutter_average_writing, "Sutter")
Tehama = get_sat_score(Tehama_average_math, Tehama_average_reading, Tehama_average_writing, "Tehama")
Trinity = get_sat_score(Trinity_average_math, Trinity_average_reading, Trinity_average_writing, "Trinity")
Tulare = get_sat_score(Tulare_average_math, Tulare_average_reading, Tulare_average_writing, "Tulare")
Tuolumne = get_sat_score(Tuolumne_average_math, Tuolumne_average_reading, Tuolumne_average_writing, "Tuolumne")
Ventura = get_sat_score(Ventura_average_math, Ventura_average_reading, Ventura_average_writing, "Ventura")
Yolo = get_sat_score(Yolo_average_math, Yolo_average_reading, Yolo_average_writing, "Yolo")
Yuba = get_sat_score(Yuba_average_math, Yuba_average_reading, Yuba_average_writing, "Yuba")

# I put the counties in a list and changed the names to the counties to their abbreviations for the eventual data vizualization
county = ['ALA', 'AMA', 'BUT', 'CAL', 'COL', 'CC', 'DN', 'ED', 'FRE',
          'GLE', 'HUM', 'IMP', 'INY', 'KER', 'KIN', 'LAK', 'LAS', 'LA', 'MAD', 'MRN',
          'MPA', 'MEN', 'MER', 'MOD', 'MNO', 'MON', 'NAP', 'NEV', 'ORA', 'PLA',
          'PLU', 'RIV', 'SAC', 'SBT', 'SBD', 'SD', 'SF',
          'SJ', 'SLO', 'SM', 'SB', 'SCL', 'SCR', 'SHA',
          'SIS', 'SOL', 'SON', 'STA', 'SUT', 'TEH', 'TRI', 'TUL', 'TUO', 'VEN',
          'YOL', 'YUB']

# I also put the scores in a list.
scores = [1462, 1537, 1500, 1569, 1378, 1469, 1453, 1571, 1318, 1415, 1550, 1372, 1469, 1373, 1325, 1433, 1474, 1356,
          1396, 1609, 1597, 1498, 1322, 1493, 1449, 1409, 1443, 1609, 1548, 1569, 1543, 1386, 1436, 1448, 1390, 1480,
          1398, 1415, 1575, 1579, 1505, 1603, 1585, 1558, 1506, 1482, 1530, 1420, 1445, 1413, 1453, 1341, 1525, 1538,
          1492, 1418]

# Since I have the counties and scores in a list, all I did here was just match the corresponding county with the appropriate score
# and put both different kinds of values in a dictionary. I could have graphed the data vizualization without  using a dictionary,
# but I thought it might be better given how large the data-set was.
county_and_scores = {"ALA": 1462, "AMA": 1537, "BUT": 1500, "CAL": 1569, "COL": 1378, "CC": 1469, "DN": 1453,
                     "ED": 1571, "FRE": 1318, "GLE": 1415, "HUM": 1550, "IMP": 1372, "INY": 1469, "KER": 1373,
                     "KIN": 1325, "LAK": 1433, "LAS": 1474, "LA": 1356, "MAD": 1396, "MRN": 1609, "MPA": 1597,
                     "MEN": 1498, "MER": 1322, "MOD": 1493, "MNO": 1449, "MON": 1409, "NAP": 1443, "NEV": 1609,
                     "ORA": 1548, "PLA": 1569, "PLU": 1543, "RIV": 1386, "SAC": 1436, "SBT": 1448, "SBD": 1390,
                     "SD": 1480, "SF": 1398, "SJ": 1415, "SLO": 1575, "SM": 1579, "SB": 1505, "SCL": 1603, "SCR": 1585,
                     "SHA": 1558, "SIS": 1506, "SOL": 1482, "SON": 1530, "STA": 1420, "SUT": 1445, "TEH": 1413,
                     "TRI": 1453, "TUL": 1341, "TUO": 1525, "VEN": 1538, "YOL": 1492, "YUB": 1418}

# This line of code sorts the dictionary by ascneding value so that we will be able to clearly see what county has the best
# SAT test takers.
sorted_county_and_scores = dict(sorted(county_and_scores.items(), key=operator.itemgetter(1)))

# keys/values
keys = sorted_county_and_scores.keys()
values = sorted_county_and_scores.values()

plt.title("AVG SAT Score By County In California, (SCORE/2440)")  # title
plt.xticks(rotation=75)  # x tick label rotations 75 degrees.
plt.xticks(fontsize=5)  # font size
plt.bar(keys, values, )  # keys will be x axis, values will be y axis. Bar graph
plt.savefig("sample.png", dpi=10026)  # 1920x1080, saving as a pdf file.
plt.show()  # print graph

# I could have made a more involved and complex graph, but I believe that creating a data vizulation, less is more.
# the main purpose of this graph is to find the county that has the highest average SAT score, and thats what the graph does
# clearly and concise
