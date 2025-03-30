#!/bin/bash


echo "Введите IP или домен"
read target

echo "Введите порт"
read port

echo "Введите название файла результатов сканирования"
read filename
# Начало сканирования.
nmap -sT "$target" -p "$port" -oG "$filename.txt"
# Вывод результата сканирования, фильтруя вывод по открытым портам.
cat $filename | grep open