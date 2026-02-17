{% snapshot users_snapshot %}

{{
    config(
      target_schema='main',
      unique_key='user_id',
      strategy='check',
      check_cols=['address'],
    )
}}

/* Capturing historical changes for user addresses using SCD Type 2 logic.
   The 'check' strategy monitors updates to the address column.
*/
select * from {{ source('raw', 'raw_users') }}

{% endsnapshot %}