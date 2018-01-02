#!/bin/bash
awk '{print $3}' $1 | grep -vE "(^password|^$)" | tr '\r\n' ' '
