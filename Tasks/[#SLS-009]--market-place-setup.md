### Market Place Setup


- Create a new django app called `marketplace` (remember to add it to the `INSTALLED_APPS` extented in the `settings.py` file)

- Create the following model classes in the `marketplace/models.py` file:

  - Product
    - image: ImageField
    - name: CharField with a maximum length of 100 characters
    - description: TextField
    - price: DecimalField with a maximum of 10 digits and 2 decimal places
    - discount_price: DecimalField with a maximum of 10 digits and 2 decimal places
    - quantity: IntegerField
    - category: ForeignKey to a Category model
    - tags: ManyToManyField to a Tag model
    - published: BooleanField
    - created_at: DateTimeField
    - updated_at: DateTimeField
  

  - Category
    - name: CharField with a maximum length of 100 characters
    - created_at: DateTimeField (use auto_now_add=True)
    - updated_at: DateTimeField (use auto_now=True)


  - Tag
    - name: CharField with a maximum length of 50 characters
    - created_at: DateTimeField (use auto_now_add=True)
    - updated_at: DateTimeField (use auto_now=True)


  - Cart
      - user: foreign key to the user model
      - items: ManyToManyField to the CartItem model
      - total_price: DecimalField with a maximum of 10 digits and 2 decimal places
      - created_at: DateTimeField
      - updated_at: DateTimeField

  
  - CartItem
    - cart: foreign key to the cart model
    - product: foreign key to the product model
    - quantity: IntegerField
    - total_price: DecimalField with a maximum of 10 digits and 2 decimal places
    - created_at: DateTimeField
    - updated_at: DateTimeField
  

  - shippingAddress
    - user: foreign key to the user model
    - address: CharField with a maximum length of 100 characters
    - city: CharField with a maximum length of 100 characters
    - state: CharField with a maximum length of 100 characters
    - phone_number: CharField with a maximum length of 15 characters
    - zip_code: CharField with a maximum length of 10 characters
    - is_default: BooleanField
    - created_at: DateTimeField
    - updated_at: DateTimeField


  - Bankcard
    - user: foreign key to the user model
    - card_number: CharField with a maximum length of 16 characters [to be discussed]
    - card_holder: CharField with a maximum length of 100 characters
    - expiry_date: CharField with a maximum length of 5 characters
    - cvv: CharField with a maximum length of 3 characters
    - is_default: BooleanField
    - created_at: DateTimeField
    - updated_at: DateTimeField
      

  - Order
    - order_id: CharField with a maximum length of 20 characters, unique
    - user: foreign key to the user model
    - products: foreign key to the Cart model
    - shipping_address: foreign key to the shippingAddress model
    - bankcard: foreign key to the Bankcard model
    - shipping_fee: DecimalField with a maximum of 10 digits and 2 decimal places
    - total_products_price: DecimalField with a maximum of 10 digits and 2 decimal places
    - total_price: DecimalField with a maximum of 10 digits and 2 decimal places
    - status: CharField with a maximum length of 20 characters (choices: 'paid' 'shipped', 'delivered', 'cancelled')
    - tracking_number: CharField with a maximum length of 20 characters
    - created_at: DateTimeField
    - updated_at: DateTimeField
