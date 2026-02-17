with source as (
    select * from {{ ref('users_snapshot') }}
),

renamed as (
    select
        user_id,
        -- Standardizing field names for the user dimension
        name as user_name,
        address,
        created_at,
        -- Mapping dbt snapshot metadata to business-friendly temporal columns
        dbt_valid_from as effective_date,
        dbt_valid_to as expiry_date
    from source
)

select * from renamed