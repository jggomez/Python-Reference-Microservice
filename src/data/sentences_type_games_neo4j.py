GET_ALL_TYPE_GAMES =\
    """
    MATCH (user:USER{id:{userId}}) - [rel:PLAYED] -> (typeGame:TYPEGAME)
    RETURN
        id(typeGame) as id,
        typeGame.name as name, 
        typeGame.urlbackground as urlBackground,  
        typeGame.code as code, 
        typeGame.type as type, 
        max(rel.points) as level,
        typeGame.nameLevel as nameLevel
    UNION ALL
    MATCH (user:USER{id:{userId}})
    MATCH (typeGame:TYPEGAME)
    WHERE not (user) - [:PLAYED] -> (typeGame)
    RETURN 
        id(typeGame) as id,
        typeGame.name as name, 
        typeGame.urlbackground as urlBackground,  
        typeGame.code as code, 
        typeGame.type as type,
        0 as level,
        typeGame.nameLevel as nameLevel
"""

GET_ALL_TYPE_GAMES_BY_USER =\
    """
    MATCH (user:USER{{id:'{}'}}) - [rel:IS_PLAYING] -> (typeGame:TYPEGAME)
    RETURN
        id(typeGame) as id,
        typeGame.name as name, 
        typeGame.urlbackground as urlBackground,  
        typeGame.code as code, 
        typeGame.type as type,
        rel.points as level,
		typeGame.nameLevel as nameLevel, 
        round((rel.difficulty * 100)) as progression
"""
