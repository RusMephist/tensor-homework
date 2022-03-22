#!/bin/bash

function get_server_code {
    server_code="`curl -o /dev/null -s -w "%{http_code}" $server`"
    if [ "$server_code" == 000 ]; then
        printf "{\"failed\": true, \"msg\": \"can't connect to server\"}"
        exit 1
    else
        msg="$server_code"
    fi
}

source $1

if [ -z $action ]; then
    printf '{"failed": true, "msg": "missing required arguments: action"}'
    exit 1
fi
if [ -z $server ]; then
    printf '{"failed": true, "msg": "missing required arguments: server"}'
    exit 1
fi

changed="false"
msg=""
contents=""

case $action in
    get_code)
        get_server_code
        ;;
    *)
        printf '{"failed": true, "msg": "invalid action: %s"}' "$action"
        exit 1
        ;;
esac

printf '{"changed": %s, "msg": "%s"}' "$changed" "$msg"

exit 0
