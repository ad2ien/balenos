#!/bin/bash
# Reset the session 
pkill firefox
rm ~/Downloads/*

firefox --private-window &
