#!/usr/bin/env bash
lsof -n -i:55667 | grep LISTEN | awk '{ print $2 }' | uniq | xargs kill -9
