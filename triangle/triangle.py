
def main():
 triangle(10)

def triangle(length):
	length = int(length)
	for row in range(0, length+1):
		for col in range(0, row):
			print(end='*')
		print()

main()
