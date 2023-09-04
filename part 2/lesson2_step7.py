from selenium import webdriver
from selenium.webdriver.common.by import By
import os

#browser = webdriver.Chrome()

current_dir = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(current_dir, 'file.txt')

print('THIS IS', current_dir)
print(os.path.abspath(__file__))
print(file_path)

