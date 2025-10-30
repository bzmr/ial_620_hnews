import requests
import json

# get ids from file that has one story_id per line (# commented lines ignored)
with open("story_ids.txt", "r", encoding="utf-8") as f:
  story_ids = []
  for line in f:
    stripped = line.strip()
    if not stripped or stripped.startswith('#'):
      continue
    if stripped.isdigit():
      story_ids.append(stripped)

# fetch json for each story id
stories = []
for story_id in story_ids:
  url = f"http://hn.algolia.com/api/v1/items/{story_id}"
  payload = {}
  headers = {}
  response = requests.request("GET", url, headers=headers, data=payload)

  try:
    data = response.json()
  except ValueError:
    print("Response is not valid JSON:")
    print(response.text)

  # get additional metrics for the story (specifically for comment counts)
  url = f"http://hn.algolia.com/api/v1/search?tags=comment,story_{story_id}"
  response = requests.request("GET", url, headers=headers, data=payload)
  try:
    extra_data = response.json()
  except ValueError:
    print("Response is not valid JSON:")
    print(response.text)

  # add num_comments from extra_data to main data
  num_comments = extra_data.get("nbHits")
  if num_comments is not None:
    data["num_comments"] = num_comments

  # add to stories list
  stories.append(data)

if stories:
  #print(json.dumps({"hits": stories}, indent=2, ensure_ascii=False))
  # write to file, stories_with_comments.json
  with open("stories_with_comments.json", "w", encoding="utf-8") as out_file:
    json.dump({"hits": stories}, out_file, indent=2, ensure_ascii=False)
