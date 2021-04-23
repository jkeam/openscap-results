#!/bin/bash

rm -rf ./resultsdir
mkdir ./resultsdir
oc compliance fetch-raw scansettingbinding nist-moderate -o resultsdir/
