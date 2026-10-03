temp_in_cels=float(input("Enter temperature in Celsius: "));
temp_in_fahr=(temp_in_cels * 9/5) + 32;
print(f"Celsius :{temp_in_cels}  °C");
print(f"Fahrenheit: {temp_in_fahr} °F");
fahr=float(input("Enter temperature in Fahrenheit: "));
cels=(fahr - 32) * 5/9;
print(f"Fahrenheit:{fahr} °F");
print(f"Celsius: {cels} °C");