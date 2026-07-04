select 
case
when from_id < to_id  then from_id
else to_id
end as person1,
case
when from_id < to_id then to_id
else from_id
end  as person2,
count(1) as call_count,
sum(duration) as total_duration
from calls
where duration is not null
group by person1, person2;