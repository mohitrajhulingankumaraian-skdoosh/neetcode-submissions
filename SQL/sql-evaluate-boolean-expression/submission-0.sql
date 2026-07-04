-- Write your query below

select e.*,
case 
when e.operator = '<' then vl.value < vr.value
when e.operator = '>' then vl.value > vr.value
when e.operator = '=' then vl.value = vr.value
else false 
end as value
from expressions e
join variables vl
on e.left_operand = vl.name
join variables vr
on e.right_operand = vr.name
