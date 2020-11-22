"""
Server DB
"serverid": ctx.guild.id, 
"ownerid": ctx.guild.owner_id,
"settings" : {
    "prefix" : "",
    "prefixhistory" : [],
    "modules" : [],
    "botroles" : {
        "admin" : {
            "role" : None,
            "users" : [ctx.guild.owner_id]
        },
        "officer": {
            "role" : None,
            "users" : []
        },
        "mod": {
            "role" : None,
            "users" : []
        },
        "authuser": {
            "role" : None,
            "users" : []
        }
    }
}
})

User DB
user id
join date
leave date
leaves/joins
common servers
"""