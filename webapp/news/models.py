from webapp.db import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    pub = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<News {self.title} {self.url}>'