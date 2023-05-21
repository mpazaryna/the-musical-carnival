import requests
import html2text

# Define a function to retrieve website
def get_website(url):
  try:
    response = requests.get(url)
    if response.status_code != 200:
      print(f"Error retrieving website. Status code: {response.status_code}.")
      return None
    return response.text
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving website: {e}")
    return None

# Define a function to save content to file
def save_to_file(file_name, content):
  with open(file_name, 'w') as f:
    f.write(content)

# Define a function to print the contents of a file
def print_file_contents(file_name):
  with open(file_name, 'r') as f:
    print(f.read())

# Define a function to convert HTML to Markdown
def html_to_markdown(html_content):
  converter = html2text.HTML2Text()
  converter.ignore_links = True
  return converter.handle(html_content)

# URL to web page
url = 'https://every.to/chain-of-thought/ai-and-the-future-of-programming'

# Get website content
website_content = get_website(url)
if website_content is None:
  exit()

# Save HTML content to file
preview_file_name = 'preview.html'
save_to_file(preview_file_name, website_content)

# Convert HTML to Markdown
markdown_text = html_to_markdown(website_content)

# Save Markdown content to file
markdown_file_name = 'article.md'
save_to_file(markdown_file_name, markdown_text)

# Print contents of preview.html and article.md
print(f"\nContents of {preview_file_name}")
print_file_contents(preview_file_name)
print(f"\nContents of {markdown_file_name}")
print_file_contents(markdown_file_name)