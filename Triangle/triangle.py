
def main():
 triangle(10)

def triangle(length):
	length = int(length)
	for row in range(1, length+1):
		for col in range(1, row):
			print(end='*')
		print()

main()
