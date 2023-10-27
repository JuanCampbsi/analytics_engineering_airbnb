with source_airbnb as (
    select * from {{ source('Fonte_AIRBNB_Gold', 'Calendar_Silver') }}
),

final as (
    select * from source_airbnb
)

select * from final