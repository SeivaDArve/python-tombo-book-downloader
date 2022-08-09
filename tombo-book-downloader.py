from selenium import webdriver
import os

# Define path where the Browser (Opera) is located
#PATH = "C:\Program Files (x86)\operadriver_win64\operadriver.exe"
#driver = webdriver.Opera(PATH)

# Define path where the Browser (Chrome) is located
PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.chrome(PATH)


# Clear screen from the windows terminal
os.system('cls')

# Descriptions
print('# Title: Python Downloader for Tombo files')
print("# Path to Chrome webdriver=", PATH,"\n")

# Open the browser in a specific webpage
driver.get("https://tombo.pt/f/gva13")

# Input the link the the next book you want to download
#print("Enter the book link you want to download:")
#vbook = input()
#print('Your input:', "vbook", vbook)
#print("opening", vbook)
#driver.get(vbook)
# print("downloading")

print('done')

# Close only the tab
# driver.close()

# Close the entire browser
# driver.quit()
