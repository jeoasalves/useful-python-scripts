query_pipeline = [{
    "$group": {
        "_id": "$situacao",
        "total": {
            "$sum": 1
        }
    }
},
    {
    "$sort": {
        "total": -1
    }
},
    {
    "$project": {
        "situacao": "$situacao",
        "total": "$total"
    }
}]
