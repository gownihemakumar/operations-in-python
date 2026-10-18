#COMPANY and TAX_RATE ARE CONSTANTS
COMPANY="Nimbus Software"
TAX_RATE=0.18
#variables
invoice_id=5001
customer_name="Hema kumar"
items=3
subtotal=1200
#calculate tax and total
tax=subtotal*TAX_RATE
total=subtotal+tax
print("==================")#creates top border using repeated =characters
print("COMPANY:",COMPANY)
print("TAX_RATE:",TAX_RATE)
print("INVOICE_ID:",invoice_id)
print("CUSTOMER_NAME:",customer_name)
print("ITEMS:",items)
print("SUBTOTAL:",subtotal)
print("TAX:",tax)
print("TOTAL:",total)
print("==================")
#customer adding one more item
print("=======UPDATED========")
items+=1
subtotal+=250
tax=subtotal*TAX_RATE
total=subtotal+tax
print("COMPANY:",COMPANY)
print("TAX_RATE:",TAX_RATE)
print("INVOICE_ID:",invoice_id)
print("CUSTOMER_NAME:",customer_name)
print("ITEMS:",items)
print("SUBTOTAL:",subtotal)
print("TAX:",tax)
print("TOTAL:",total)
print("==================")#creates lower border using repeated =characters

