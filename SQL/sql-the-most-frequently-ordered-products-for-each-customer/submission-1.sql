with prod_purchase_count as (
select customer_id, product_id, count(1) as pur_freq
from orders
group by customer_id, product_id
),
pur_rank as (
    select customer_id, product_id,
    rank() over (partition by customer_id order by pur_freq desc) as pur_rnk
    from prod_purchase_count
)
select a.customer_id, a.product_id, p.product_name
from (select customer_id, product_id
from pur_rank where pur_rnk = 1)a
inner join products p
on a.product_id = p.product_id
inner join customers c 
on a.customer_id = c.customer_id
;