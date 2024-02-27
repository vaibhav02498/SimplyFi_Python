def indian_currency(number):
    number_str = str(number)
    length = len(number_str)
   
    result = ""
    flag = 0
    # Iterate through the string from the end
    for i in range(length - 1, -1, -1):
        # Add comma after three digits for the first group
        if (length - i - 1) % 3 == 0 and i != length - 1 and flag==0:
            result = "," + result
            flag=1
        # Add comma after every two digits except for the first group
        elif (length - i - 2) % 2 == 0 and i != length - 1 and flag==1:
            result = "," + result
        result = number_str[i] + result
   
    return result

input_number = input()
output_currency = indian_currency(input_number)
print("Output:", output_currency)
