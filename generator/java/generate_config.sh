#!/bin/sh
sed -e "s,sdkFolder,$2," -e "s,testFolder,$3," $1
