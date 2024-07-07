# !/bin/bash
# count 1 to 100


#echo "Count 1 to 100:"
#for i in {1..100}
#do
#	echo $i
#done

start=1
end=1000000

for i in $(seq $start $end)
do
	echo "	$i"
	clear
done
