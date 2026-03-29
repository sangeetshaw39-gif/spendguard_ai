#!/bin/bash
echo "========================================="
echo "      Starting SpendGuard AI"
echo "========================================="
echo ""

echo "Checking and installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "Starting the application server..."
python3 main.py
