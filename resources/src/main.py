from utils import download_images, download_image

import csv

trainlinks = []
with open("dataset/train.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        trainlinks.append(row[0])

testlinks = []
with open("dataset/test.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        testlinks.append(row[0])


download_images(trainlinks, "trainImages", allow_multiprocessing=False)
download_images(testlinks, "testImages", allow_multiprocessing=False)
