# Hacker News Story Fetcher

Script fetches information about Hacker News stories using the Hacker News Algolia API (https://hn.algolia.com/api) and saves the data to a JSON file.

## Overview

The script reads story IDs from a text file, fetches story metadata and comments from the Hacker News API, adds comment count information, and outputs the results to a JSON file.

## Files

- `getStoriesJsonByFile.py` - Main Python script
- `story_ids.txt` - Input file containing Hacker News story IDs (one per line)
- `stories_with_comments.json` - Output file containing the fetched story data (generated when script runs)

### Running the Script

- Python 3.x
- libraries: `requests` (`py -m pip install requests`)

1. Create\edit `story_ids.txt` with the story IDs to fetch, one id per line
2. Run the script: python getStoriesJsonByFile.py
3. The results will be saved to `stories_with_comments.json`
