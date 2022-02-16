#!/bin/bash

echo "Run test ...."

echo "Run first test suite test_app"
python3 -m unittest tests/test_app.py

echo "Run secound test suite test_random_moves"
python3 -m unittest tests/test_app.py
