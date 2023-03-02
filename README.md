# Title: python-tombo-book-downloader
# Description: There is a public Portuguese library called Tower of Tombo. In This library there are books I need to have acess. Lucky me most of them are available online. My goal is to download them before they go offline and disapear
# Goal: Python (the programming language) is helping me downloading each one automatically instead of manually
# Use: Python scrapes the webpage and automates the process of downloading each page into a specific directory. 

# Installation of resources:
	# Following this tutorial: https://www.youtube.com/watch?v=s4jtkzHhLzY
 - $ sudo apt update && sudo apt upgrade
 - $ sudo apt install python3
 - $ sudo apt install python3-pip
 - $ sudo apt install python3.10-venv
 - Create a directory for our project and navigate there
   - mkdir python-tombo-book-downloader
   - cd !$
 - $ python3 -m venv tombo-venv
 - $ source tombo-venv/bin/activate
 - $ pip3 install scrapy
 - $ scrapy startproject tomboScraper
 - $ cd tomboScraper
 - Time to look at the webpage and decide what to download (copy URL)
 - Open the scrapy shell:
   # This is going to let us download the page and then interrogate it so that we know what commands we want to do for our scrapy script
   - $ scrapy shell:
      - $ fetch('https://digitarq.arquivos.pt/viewer?id=4807142')
      # The output must say "Crawled (200)" where 200 is the response that means that it works
      # Ctrl-l to clear the screen
      # When you use the scrapy shell everything is stored in the response variable. Test that by typing:
      - $ response
      # Now we can use xpath or css selector to get the information of this page
      # With the mouse, hover the element you want and click "inspect" from the right click menu
         # I decided to go to <a class="TreeNode" </a>
         - $ response.css('a.TreeNode')  ## The information that comes to the screen is all the information that matches that
         - $ response.css('div.TreeNode').get()  ## Gives us the html of the first item in that list
      # We can creat a list of all the element by:
	- $ products = response.css('a.TreeNode') 
      # Now we can see how many element did we grab by:
        - $ len(products) 
      # Get the name of things: In the webpagen find in which tag the name is inside of... in the case is in an <a> </a> tag
        - products.css('a.TreeNode').get()  ##This gets the first element
        - products.css('a.TreeNode::text').get()  ##This gets the text (name) of the element
        - products.css('a.TreeNode::text').getall()  ##This gets the text (name) of all the elements


      Tutotrial stopped at minute: 7:02
