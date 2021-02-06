import os, platform, time, sys

# | Check Dependencies |

def errorinstall():
	print('Type: \n')
	print('pip3 install -r requirements.txt')
	print('or')
	print('pip install -r requirements.txt')
	input()
	sys.exit()

# pillow

try:
	from PIL import Image
except:
	print('Error importing pillow.')
	errorinstall()

# colorama
try:
	from colorama import init, Fore, Back, Style
	init(convert=True)

except:
	print('Error importing colorama.')
	errorinstall()

# | Terminal Settings |

# Detect platform (Windows)
if(platform.system() == 'Windows'):
	os.system('cls')
	os.system('title IMG to PDF')

# Detect platform (Linux)
else:
	os.system('clear')
	os.system('echo "\033]0;IMG to PDF\a"')


# | Welcome Banner |

b = open('banner.txt', 'r')
banner = b.read()
print(Fore.YELLOW + banner + Fore.WHITE)


# | Start | 

def main():

	# GET Image File
	print('(Example: image.jpg)')
	path = input('Image Route: ')

	print() 

	# GET Name & Route of PDF
	print('(Example: image.pdf)')
	name = input('Save PDF as: ')

	try:
		pdf = Image.open(path)
		pdf.save(name)
		print(Fore.GREEN + 'PDF saved successfully')
	except:
		print()
		print(Fore.RED + 'An error occurred while saving the PDF\nPlease enter the path where you want to save the PDF and use the extension ' + Fore.YELLOW + '.pdf')


if __name__ == "__main__":
    main()
    
# Credits <3: github.com/esiquiel