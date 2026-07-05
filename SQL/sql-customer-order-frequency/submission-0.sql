with expenditure as (
    select o.customer_id, c.name, to_char(o.order_date, 'YYYY-MM') as month,
    sum(p.price*o.quantity) as monthly_expense
    from orders o
    left join product p
    on o.product_id = p.product_id
    left join customers c
    on c.customer_id = o.customer_id
    group by o.customer_id, c.name, to_char(o.order_date, 'YYYY-MM')
)
select customer_id, name
from expenditure
where month = '2020-06'
and monthly_expense >= 100
intersect
select customer_id, name
from expenditure
where month = '2020-07'
and monthly_expense >= 100;

