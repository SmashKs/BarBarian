#!/usr/bin/env bash
ps auxww | grep 'BarBarian worker' | awk '{print $2}' | xargs kill -9
