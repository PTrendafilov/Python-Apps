print('Welcome to the email slicer')
print()
email = input('Please enter the email: ')
username, domain = email.split('@')
domain, extension = domain.split('.')
print('Username: ' + username)
print('Domain: ' + domain)
print('Extension: ' + extension)