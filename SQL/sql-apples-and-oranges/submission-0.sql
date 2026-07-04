-- Write your query below
select sale_date,
sum(
    case 
    when fruit = 'apples' then sold_num
    else -1*sold_num
    end
) as diff
from sales
group by sale_date;