#!/bin/bash

find . -name *.pyc -delete
echo
echo "----------------------------------------------------------------------"
echo "Running Unit Specs"
echo "----------------------------------------------------------------------"
echo

TEST_PATH="specs"

if [ -z "$1"  ]; then
    FORMATTER="progress"
elif [ $1 = "doc" ]; then
    FORMATTER="documentation"
fi

mamba -f $FORMATTER `find specs/.  -name *_specs.py | grep -v systems`

MAMBA_RETCODE=$?

exit $MAMBA_RETCODE
