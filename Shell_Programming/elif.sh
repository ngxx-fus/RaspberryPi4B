#!/bin/bash


# ex1
clear

echo 'Do u luv me?'
echo 'Enter YES/NO'
read YN

if ["$YN" = 'YES' ];
then
	echo 'Oh, thanks, i luv you too!'
elif [ "$YN" = 'NO' ];    #U need to add "" around $YN to prevent "bash: [: =: unary operator expected" error when $YN return null
then
	echo 'No, why? ???'
else
	echo "WTH! Invalid ans! Can you read these things i noticed?"
fi

