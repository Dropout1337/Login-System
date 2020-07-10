import requests, time

username = input(' > Username: ')
password = input(' > Password: ')

r = requests.get('https://pastebin.com/raw/jB285Hxc').text
if username and password in r:
  time.sleep(0.1)
else:
  print('Invalid Username Or Password.')
  input()
  exit()

# Your Code Below

print('Whats Your Name?')
name = input()
print(f'Hi {name}')
input()
