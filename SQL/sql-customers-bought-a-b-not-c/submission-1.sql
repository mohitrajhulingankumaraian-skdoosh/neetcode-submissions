-- Write your query below
select customer_id, customer_name
from customers
where customer_id in (
    select distinct customer_id from orders
    where product_name = 'A'
    intersect
    select distinct customer_id from orders
    where product_name = 'B'
    except
    select distinct customer_id from orders
    where product_name = 'C'    
)
order by customer_name;