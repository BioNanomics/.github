#!/usr/bin/env python3
"""
Manual script to test the BioNanomics website information fetching.
This can be run locally to test the functionality.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

def main():
    """Run the fetch script manually."""
    print("=" * 50)
    print("Manual BioNanomics Information Fetch Test")
    print("=" * 50)
    
    try:
        from fetch_bionanomics_info import main as fetch_main
        fetch_main()
    except Exception as e:
        print(f"Error running fetch script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()