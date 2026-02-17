with source as (
    select * from {{ source('raw', 'raw_orders') }}
),

renamed as (
    select
        order_id,
        user_id,
        product_id,
        amount as quantity, -- Kita aliaskan biar standar DE
        cast(order_date as timestamp) as order_at
    from source
)

select * from renamed