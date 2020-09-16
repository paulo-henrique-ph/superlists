from selenium import webdriver

browser = webdriver.Chrome()

# Open the Web Browser
browser.get("http://localhost:8000")

# See if the title mentions todo list
assert 'To-Do' in browser.title

# Insert a task "Buy peacock feathers"

# When inserted show the item "1: Buy peacock feathers"

# Add another task "Use peacock feathers to make a fly"

# Show the two items in the list

# Generate a unique url for the user

# Access this unique url and see if the tasks still included

# End

browser.quit()
