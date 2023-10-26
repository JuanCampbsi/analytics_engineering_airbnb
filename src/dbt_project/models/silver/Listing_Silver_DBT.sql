with source_airbnb as (
    select * from {{ source('Fonte_AIRBNB', 'Listing_Silver') }}
),

final as (
    select * from source_airbnb
)

select * from final