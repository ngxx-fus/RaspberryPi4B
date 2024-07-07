# !/bin/bash

echo "Enter YES/NO:"
read CH
case "$CH" in
	"Y" | "y" | "Ye" | "yE"  | "YES"  | "yes"  | "yES"  | "YeS"  | "YEs"  | "yeS"  | "Yes"  | "yEs" ) echo "YES is entered";;
	"N" | "n" | "No" | "no" | "NO" | "nO" ) echo "NO is entered";;
	 * ) echo "Invalid entered content!";;
esac

