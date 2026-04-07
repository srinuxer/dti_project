from app import app
from models import Analysis, User, db

with app.app_context():
    print('DB URI:', app.config['SQLALCHEMY_DATABASE_URI'])
    print('Users:', User.query.count())
    print('Analyses:', Analysis.query.count())
    analyses = Analysis.query.all()
    for a in analyses:
        print(f'Analysis ID: {a.id}, User ID: {a.user_id}, Status: {a.ai_status}')
