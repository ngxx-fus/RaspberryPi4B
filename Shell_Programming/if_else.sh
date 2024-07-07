#!/bin/bash


# ex1
clear

echo 'Do u luv me?'
echo 'Enter YES/NO'
read YN

if [ $YN = 'YES' ];
then
	echo 'Oh, thanks, i luv you too!'
else
	if [ $YN = 'NO' ];
	then
		echo 'No, why? ???'
	else
		echo "WTH! Invalid ans! Can you read these things i noticed?"
	fi
	fi

