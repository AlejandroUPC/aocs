#!/bin/bash

YEAR=$1
DAY=$2 

echo "Doing year $YEAR day $DAY folder structure"
for i in 1 2
do
    BASE_PATH="aocs/$YEAR"
    mkdir -p $BASE_PATH/day_$DAY/$i/
    touch $BASE_PATH/day_$DAY/$i/day_$DAY"_"$i.py
    touch $BASE_PATH/day_$DAY/$i/test_day_$DAY"_"$i.py
done
