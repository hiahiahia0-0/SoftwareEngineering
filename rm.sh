#!/bin/bash

find . -type d -name "migrations" -exec rm -rf {} +

find . -type d -name "__pycache__" -exec rm -rf {} +