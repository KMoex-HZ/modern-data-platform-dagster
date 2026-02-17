with users as (
    select * from {{ ref('stg_users') }}
)

select
    user_id,
    user_name,
    address,
    created_at,
    effective_date,
    -- Labeling the data to distinguish between current and historical records
    case 
        when expiry_date is null then 'Active'
        else 'Historical'
    end as record_status
from users