#!/bin/bash

while IFS= read -r -d '' -u 9
do
    echo "$REPLY"
    jupyter trust "$REPLY"
done 9< <( find /assignments -type f -exec printf '%s\0' {} + )