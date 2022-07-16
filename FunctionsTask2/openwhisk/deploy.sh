#!/bin/bash
####################################################################
## Creates all necessary files for the deployment and deploys     ##
## them directly to AWS using terraform.                          ##
##                                                                ##
## It also supports the creation of a typeMappings.json.          ##
####################################################################


helpmenu () {
    echo -e "Usage: $0 [operation] [--help] [--url] [--mapping] \n" 

    echo -e "operation: It can be one of these values create, update, and delete. Default value is create."
    echo -e "Commands:"
    echo -e "\t--help\t\t\tShow this help output."
    echo -e "\t--url\t\t\tPrints out all deployment urls"
    echo -e "\t--mappings\t\tCreates typeMapping.json with the deployment urls"
    echo -e "\t--update\t\tUpdate resources"
    echo -e "\t--delete\t\tDelete resources"
}

showURL () {
    for i in ${!functions[@]}; do
        url="${functions[$i]} = $PROXY_WEB_SERVER/${functions[$i]}"
        echo $url
    done
}

createMappings () {
    python3 createTypeMappings.py
}
op=$1

functionBaseFolder="../functions"
functions=("CountPattern" "Split" "Sum" "Concat" "Modify" "PartialModify")
. ./wsk.config

while [ ! $# -eq 0 ]
do
    case "$1" in
        --help | -h)
            helpmenu
            exit
            ;;
        --url | -u)
            showURL
            exit
            ;;
        --mappings | -m)
            createMappings
            exit
            ;;
    esac
    shift
done

wsk property set --apihost $OPEN_WHISK_API_HOST --auth $OPEN_WHISK_AUTH
if [[ $op -ne "update" ]];
then
    op="create"
fi

for i in ${!functions[@]}; do
  ./build.sh $functionBaseFolder/${functions[$i]} $op
done