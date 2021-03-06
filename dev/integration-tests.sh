#!/bin/bash

find . -name *.pyc -delete
echo
echo "----------------------------------------------------------------------"
echo "Running Integration Specs"
echo "----------------------------------------------------------------------"
echo

TEST_PATH="integration_specs"

if [ -z "$1"  ]; then
    FORMATTER="progress"
elif [ $1 = "doc" ]; then
    FORMATTER="documentation"
fi

mamba -f $FORMATTER `find integration_specs/.  -name "*_specs.py" | grep -v systems`

MAMBA_RETCODE=$?

exit $MAMBA_RETCODE
