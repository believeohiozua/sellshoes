#### Cart Items APIs

The Cart Items APIs should provide users with the following functionalities:

1. **View Cart**  
   - Retrieve a list of items currently in the user's cart.
   - Display the total price of all items.

2. **Add to Cart**  
   - Add a new item to the user's cart.  
   - If the same item is added again from the product list, the quantity should be updated instead of creating a duplicate entry.  
   - Adjust the total price to reflect the change.

3. **Update Item Quantity**  
   - **Increase Quantity**: Increase the quantity of an item in the cart by 1 or a specified amount.  
   - **Decrease Quantity**: Decrease the quantity of an item in the cart.  
     - If the quantity is reduced to 0, the item should be removed from the cart.  
   - Ensure the total price is recalculated after each update.

4. **Remove Item from Cart**  
   - Completely remove an item from the cart.  
   - Update the total price accordingly.

APIs 
1. Add to cart API NOTE: (if user add the same item again, from the product list, the quantity should be updated)
2. View Cart API
3. Increate item quantity API 
4. Decrease item quantity API  NOTE: If the quantity is set to 0, the item should be removed from the cart

### Notes
- The total price of the items in the cart must be recalculated and updated in **all API interactions**.  
- Coupon and discount logic will not be implemented at this stage.

--- 
