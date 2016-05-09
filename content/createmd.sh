#!/bin/sh

DATE_STR=`date +'%Y-%m-%d'`
TIME=`date +'%Y%m%d%H%M'`
echo "Title:
Date: $DATE_STR
Modified: $DATE_STR
Category:
Tags:
Slug: $TIME
Author: Yushin" > $DATE_STR.md