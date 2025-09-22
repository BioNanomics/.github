#!/usr/bin/env python3
"""
Test script to validate the fetch_bionanomics_info.py script structure.
"""

import sys
import os

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(__file__))

def test_script_structure():
    """Test that the main script has the expected structure."""
    try:
        import fetch_bionanomics_info
        
        # Check that main functions exist
        assert hasattr(fetch_bionanomics_info, 'fetch_website_info'), "fetch_website_info function missing"
        assert hasattr(fetch_bionanomics_info, 'update_readme'), "update_readme function missing"
        assert hasattr(fetch_bionanomics_info, 'main'), "main function missing"
        
        print("✓ All required functions are present")
        
        # Test the update_readme function with mock data
        test_info = {
            'title': 'Test Title',
            'description': 'Test description for BioNanomics',
            'last_updated': '2024-01-01 12:00:00 UTC'
        }
        
        # Create a temporary profile directory for testing
        os.makedirs('/tmp/test_profile', exist_ok=True)
        original_cwd = os.getcwd()
        os.chdir('/tmp')
        
        try:
            fetch_bionanomics_info.update_readme(test_info)
            
            # Check if the file was created
            if os.path.exists('profile/README.md'):
                with open('profile/README.md', 'r') as f:
                    content = f.read()
                    assert 'Test Title' in content or 'Test description' in content, "Content not properly written"
                    print("✓ update_readme function works correctly")
            else:
                print("✗ README.md was not created")
                return False
                
        finally:
            os.chdir(original_cwd)
        
        return True
        
    except ImportError as e:
        print(f"✗ Failed to import fetch_bionanomics_info: {e}")
        return False
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_script_structure()
    sys.exit(0 if success else 1)