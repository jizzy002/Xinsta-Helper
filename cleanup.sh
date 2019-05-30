#!/bin/bash
#Xinsta-Helper cleanup script

echo Xinsta Helper cleanup tool
echo 
read -p "Do you want to remove the .APK file? (y/n)" remove

case $remove in
     [Yy] )
rm input/*.apk rm *.txt rm -rf output ;;
     [Ny] )
rm -rf output rm *.txt ;;

esac

clear
echo Directory cleaned up!
