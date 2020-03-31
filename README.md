# Meausre Power using Thorlabs PM100A

## Description
This is a simple script for controlling and collecting measured data from 
[Thorlabs power meter PM100A](https://www.thorlabs.com/drawings/d308bb7cd698aa40-F97FC694-081C-CBA5-A0B1CDA28F4DB4BB/PM100A-Manual.pdf).
Measured power data will be stored into the database file of `pd.db`.

## Usage
In a virtual environment, install all packages.
```shell
$ pip3 install -r requirements.txt
```
Follow the instructions below to measure the power of a light source,
```shell
$ python3 power_measure.py
Enter the desired running time in second:
>> 
Enter the step size in second:
>> 

```