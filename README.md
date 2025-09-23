# .github

This repository contains GitHub organization-level configurations and automation for BioNanomics.

## Features

- **Manual Website Information Fetching**: A GitHub Action workflow that fetches information from https://bionanomics.com/ and updates the organization profile README when manually triggered.
- **On-Demand Updates**: The workflow runs only when manually triggered to update the organization profile with the latest website information.

## Files

- `.github/workflows/fetch-website-info.yml` - GitHub Action workflow for fetching website information
- `scripts/fetch_bionanomics_info.py` - Python script that fetches and processes website information
- `profile/README.md` - Organization profile README that displays on the GitHub organization page