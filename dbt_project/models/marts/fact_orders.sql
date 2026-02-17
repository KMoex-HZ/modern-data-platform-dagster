with orders as (
    select * from {{ ref('stg_orders') }}
),

products as (
    select * from {{ ref('stg_products') }}
)

select
    o.order_id,
    o.user_id,
    o.product_id,
    p.product_name,
    p.category,
    o.quantity,
    p.price,
    (o.quantity * p.price) as total_amount, -- Kita hitung total belanjanya
    o.order_at
from orders o
left join products p on o.product_id = p.product_id