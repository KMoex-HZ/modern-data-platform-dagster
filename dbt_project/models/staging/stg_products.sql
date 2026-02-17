with source as (
    select * from {{ source('raw', 'raw_products') }}
),

renamed as (
    select
        product_id,
        -- Normalizing column names for downstream consistency
        name as product_name,
        category,
        price
    from source
)

select * from renamed