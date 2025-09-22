#!/usr/bin/env python3
"""
Script to fetch information from https://bionanomics.com/ and update the organization profile README.
"""

import requests
from bs4 import BeautifulSoup
import os
import sys
from datetime import datetime

def fetch_website_info():
    """Fetch information from BioNanomics website."""
    try:
        url = "https://bionanomics.com/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print(f"Fetching information from {url}...")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract key information
        info = {
            'title': '',
            'description': '',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        
        # Try to get the page title
        title_tag = soup.find('title')
        if title_tag:
            info['title'] = title_tag.get_text().strip()
        
        # Try to get meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            info['description'] = meta_desc.get('content', '').strip()
        
        # If no meta description, try to get the first paragraph
        if not info['description']:
            first_p = soup.find('p')
            if first_p:
                info['description'] = first_p.get_text().strip()[:200] + "..."
        
        print(f"Successfully fetched information:")
        print(f"Title: {info['title']}")
        print(f"Description: {info['description'][:100]}...")
        
        return info
        
    except requests.RequestException as e:
        print(f"Error fetching website: {e}")
        return None
    except Exception as e:
        print(f"Error parsing website content: {e}")
        return None

def update_readme(info):
    """Update the profile README with fetched information."""
    if not info:
        print("No information to update")
        return
    
    readme_path = "profile/README.md"
    
    # Create the README content
    readme_content = f"""# BioNanomics

{info['description']}

---

*Information automatically fetched from [bionanomics.com](https://bionanomics.com/)*  
*Last updated: {info['last_updated']}*
"""
    
    # Write to README file
    os.makedirs(os.path.dirname(readme_path), exist_ok=True)
    
    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"Successfully updated {readme_path}")
    except Exception as e:
        print(f"Error writing to {readme_path}: {e}")
        sys.exit(1)

def main():
    """Main function."""
    print("Starting BioNanomics website information fetch...")
    
    info = fetch_website_info()
    update_readme(info)
    
    print("Completed successfully!")

if __name__ == "__main__":
    main()