#!/bin/bash
# Neuronix Setup Script for macOS/Linux
# This script helps you configure API keys and set up Neuronix

echo ""
echo "=============================================================================="
echo "                    NEURONIX SETUP - macOS/Linux Edition"
echo "=============================================================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.10+ from: https://www.python.org/downloads/"
    exit 1
fi

# Run the setup script
python3 setup.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Setup failed"
    exit 1
fi

echo ""
echo "Setup complete!"
