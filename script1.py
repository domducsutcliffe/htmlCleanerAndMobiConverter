from bs4 import BeautifulSoup
import subprocess
import html

# Parse the HTML file with Beautiful Soup.
with open('aiFDB.html', 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

# Extract the title, heading, and body text.
title = soup.title.string
heading = soup.find('h1').get_text()
body_paragraphs = soup.find_all('p')
body_text = ' '.join(para.get_text() for para in body_paragraphs)

# Write the extracted text to a new HTML file.
with open('output.html', 'w') as f:
    f.write(f'<html><head><title>{html.escape(title)}</title></head><body><h1>{html.escape(heading)}</h1>{html.escape(body_text)}</body></html>')

# Convert the new HTML file to MOBI.
subprocess.run(['ebook-convert', 'output.html', 'output.mobi'])

# Convert the new HTML file to MOBI.
subprocess.run(['/Applications/calibre.app/Contents/MacOS/ebook-convert', 'output.html', 'output.mobi'])

# Add the MOBI file to the Calibre library
subprocess.run(['/Applications/calibre.app/Contents/MacOS/calibredb', 'add', 'output.mobi'])

