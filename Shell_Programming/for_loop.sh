# !/bin/bash

#ex1
echo "Ex1:"
for foo in var hehe haha nani ?;
do
	echo $foo
done

#ex2 
echo  "

Ex2:"

for filename in $(ls *.cpp);
do
	echo $filename
done

echo "


Ex3:"

sum=0

for num in $(seq 1 100);
do
	let sum=$sum+$num
done
echo "Sum 1 to 100 is: $sum"
