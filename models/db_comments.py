db.define_table('comment',
   Field('body','text',label='Your comment'),
   Field('posted_on','datetime',default=request.now),
   Field('posted_by',db.auth_user,default=auth.user_id))
db.comment.posted_on.writable=db.comment.posted_on.readable=False 
db.comment.posted_by.writable=db.comment.posted_by.readable=False
