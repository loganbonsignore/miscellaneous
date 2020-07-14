item = [
    'Pecan',
    'Apple crisp',
    'Bean',
    'Banoffee',
    'Black bun',
    'Blueberry',
    'Buko',
    'Burek',
    'Tamale',
    'Steak',
]

order_list = []

print("""
Welcome to the House of Pies! Here are our pies:

-----------------------------------------------------------------""")
for i in range(len(item)):
    print(f"{[i+1]} {item[i]},")

user_input = int(input("Enter the number of the pie you'd like to order :"))

while user_input <= len(item) and user_input > 0:
    print(f"""
Great! We'll have a {item[user_input - 1]} pie added to your order!""")
    order_list.append(item[user_input-1])
    new_input = input("Is there anything else we can get you? Enter (n) to continue to payment :")
#     if new_input == "n":
#         print(f"""
# Thank you for your order! We will call your name soon.
# Total number of pies ordered: {len(order_list)}
# """)
#         exit()
#     else:
#         user_input = int(new_input)
    if new_input == "n":
        print(f"""
----------------------------------------------------------------
Thank you for your order! We will call your name soon.

You purchased:
{order_list.count('Pecan')} Pecan
{order_list.count('Apple crisp')} Apple crisp
{order_list.count('Bean')} Bean
{order_list.count('Banoffee')} Banoffee
{order_list.count('Black bun')} Black Bun
{order_list.count('Blueberry')} Blueberry
{order_list.count('Buko')} Buko
{order_list.count('Burek')} Burek
{order_list.count('Tamale')} Tamale
{order_list.count('Steak')} Steak
""")
        exit()
    else:
        user_input = int(new_input)