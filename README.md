# OpenSCAP Results

This project processes OpenSCAP results from the Compliance Operator running on OpenShift.  The Compliance Operator uses OpenSCAP to schedule and run scans.  Getting the results out and turning them into HTML reports can be a bit tricky.  This project attempts to make that easier.


## Prerequisite
This tool assumes you have a few things already installed.

1. OpenShift v4.6+
2. [OpenShift Command Line Tool](https://github.com/openshift/oc)
3. [OpenShift Compliance Command Line Tool](https://github.com/openshift/oc-compliance)
4. Docker or Podman


## Running
Let's say you've already run a scan and now want to pull down and process the results; the steps are below. As an example, these steps are also all in `run.sh`, but just make sure to change your compliance suite name before running it.

1. Make a directory to store your results
```shell
mkdir resultsdir
```

2. Figure out which results you want
```shell
oc get compliancesuites
```

You'll get results like:

```shell
NAME        PHASE   RESULT
rhcos4-e8   DONE    COMPLIANT
```

3. Fetch raw ARF results for the compliance suite
```shell
# assuming rhcos4-e8 compliance suite
# assuming we want our results dumped to the resultsdir
oc compliance fetch-raw compliancesuite rhcos4-e8 -o resultsdir
```

4. Process the raw files
```shell
# assuming the results are stored in the resultsdir, currently no way to override this
# will output HTML and XML results in reportsdir, currently no way to override this
docker run --rm -p 8000:8000 -v $(pwd):/openscap -it quay.io/jkeam/openscap
```

## Roadmap
1. Be able to change the reports directory
2. Be able to change the results directory
