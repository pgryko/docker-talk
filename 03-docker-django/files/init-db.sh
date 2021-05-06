#!/bin/bash
set -e

createuser djangodb -s
createdb djangodb -O djangodb