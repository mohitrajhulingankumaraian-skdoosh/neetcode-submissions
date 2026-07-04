-- Write your query below
select user_id, max(time_stamp) as last_stamp
from logins
where date_part('year',cast(time_stamp as timestamp)) = '2020'
group by user_id;