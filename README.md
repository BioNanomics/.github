# .github

This repository contains GitHub organization-level configurations and automation for BioNanomics.

## Features

- **Automated Website Information Fetching**: A GitHub Action workflow that automatically fetches information from https://bionanomics.com/ and updates the organization profile README.
- **Daily Updates**: The workflow runs daily to keep the organization profile current with the latest website information.

## Files

- `.github/workflows/fetch-website-info.yml` - GitHub Action workflow for fetching website information
- `scripts/fetch_bionanomics_info.py` - Python script that fetches and processes website information
- `profile/README.md` - Organization profile README that displays on the GitHub organization page