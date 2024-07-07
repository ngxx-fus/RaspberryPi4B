# !/bin/bash

echo "Enter a character (Valid: 'A', 'B', 'C', 'D'):"
read CH
case "$CH" in
	"A") echo "'A' is entered";;
	"B") echo "'B' is entered";;
	"C") echo "'C' is entered";;
	"D") echo "'D' is entered";;
	 * ) echo "Invalid character!";;
esac

