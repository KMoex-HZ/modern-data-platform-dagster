with source as (
    select * from {{ ref('users_snapshot') }}
),

renamed as (
    select
        user_id,
        name as user_name,
        address,
        created_at,
        dbt_valid_from as effective_date,
        dbt_valid_to as expiry_date
    from source
)

select * from renamed