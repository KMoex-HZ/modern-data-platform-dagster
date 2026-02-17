/* This test will FAIL if any order has a total_amount <= 0.
   Serving as a built-in Data Quality (DQ) check within dbt to ensure 
   monetary integrity without external tools like Soda.
*/
select
    order_id,
    total_amount
from {{ ref('fact_orders') }}
where total_amount <= 0