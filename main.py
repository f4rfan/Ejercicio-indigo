import largest_product_in_a_series
import largest_palindrome_product

resp = ''

while resp != '3' and resp != '3':
    resp  = input("1)Largest product in a series \n2)Largest palindrome product \n3)Salir \n")

    if resp == '1':
        largest_product_in_a_series.main()

    elif resp == '2':
        largest_palindrome_product.main()



