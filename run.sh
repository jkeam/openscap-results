#!/bin/bash

rm -rf ./resultsdir && mkdir ./resultsdir
oc compliance fetch-raw compliancesuite rhcos4-e8 -o resultsdir
docker run --rm -p 8000:8000 -v $(pwd):/openscap -it quay.io/jkeam/openscap
