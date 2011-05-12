@auth.requires_login()
def post():
    return dict(form=crud.create(db.comment),
                comments=db(db.comment.id>0).select())
	
