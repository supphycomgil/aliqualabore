from bs4 import BeautifulSoup

html_content = "<html><body><h1>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')
