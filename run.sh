#!/bin/bash

oscap xccdf generate report $1 > ${2:-index.html}
