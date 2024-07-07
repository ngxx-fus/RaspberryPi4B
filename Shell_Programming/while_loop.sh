# !/bin/bash


echo "Enter start value:" 
read start
echo "Enter end value:" 
read end
sum=0
foo=$start
echo "Computing sum from $start to $end..."

while [ "$foo" -le $end ];
do
	sum=$(($sum+$foo)) # equivalent: sum = expr $sum+$foo, but is recommended to use!
	foo=$(($foo+1))
done

echo "Ans: $sum"
