
class EndPoints:

    CREATE_ITEM = "/api/1/item"
    GET_ITEM = lambda listing_id: f"/api/1/item/{listing_id}"
    GET_STATISTIC = lambda listing_id: f"/api/1/statistic/{listing_id}"
    GET_SELLER_ITEM = lambda seller_id: f"/api/1/{seller_id}/item"