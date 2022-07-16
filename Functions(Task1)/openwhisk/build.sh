#!/bin/bash
#####################################################################
## Creates a zip file from a given path of a lambda function. The  ##
## created file can directly be upload to AWS Lambda.              ##
#####################################################################


if [[ $# -eq 0 ]] ; then
    echo 'Error: No path provided'
    echo -e "\nUsage: $0 /path/to/lambda/fucntion \n" 
    exit 1
fi

folderName=$(basename $1)
pwd=$(pwd)

cd $1

createResource () {
    wsk action create $folderName ./cloud_function.py
}

updateResource () {
    wsk action update $folderName ./cloud_function.py
}

deleteResource () {
    wsk action delete $folderName
}

case "$2" in
        "create")
            createResource
            exit
            ;;
        "update")
            updateResource
            exit
            ;;
        "delete")
            deleteResource
            exit
            ;;
    esac

echo $1