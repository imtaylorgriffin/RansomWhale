#!/bin/sh
btc_price=23797 #price of btc on 7/28/2022
wallet=`echo $RANDOM | md5sum | head -c 20`
transactionID=`$RANDOM | md5sum | head -c 8&&date +"%M_%S_%b"`
echo vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
echo BTC Send To Address\: $wallet
#random thing that looks like a btc address
echo vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
echo Enter Amount to Send\: 
read btc_amount
echo vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
echo Sent $btc_amount BTC \(\$$((btc_price * btc_amount))\) to $wallet
echo Transaction ID: $transactionID
echo vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv