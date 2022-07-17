#!/bin/bash


git clone https://github.com/apache/openwhisk.git
cd openwhisk
./gradlew core:standalone:bootRun