from django.test import TestCase
import requests

# Create your tests here.


URL ="http://localhost:8000/stu/2"

r = requests.get(url=URL)
print(r.json())
