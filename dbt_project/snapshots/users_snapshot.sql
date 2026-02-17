{% snapshot users_snapshot %}

{{
    config(
      target_schema='main',
      unique_key='user_id',
      strategy='check',
      check_cols=['address'],
    )
}}

select * from {{ source('raw', 'raw_users') }}

{% endsnapshot %}