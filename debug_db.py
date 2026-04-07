from app import app
from models import Analysis, User, db

with app.app_context():
    print('=== Database Check ===')
    print(f"DB URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print(f'Total Users: {User.query.count()}')
    print(f'Total Analyses: {Analysis.query.count()}')
    
    print('\n=== All Analyses ===')
    analyses = Analysis.query.all()
    for a in analyses:
        user = User.query.get(a.user_id)
        print(f'ID: {a.id}, User ID: {a.user_id}, User: {user.email if user else "NOT FOUND"}, Status: {a.ai_status}, Timestamp: {a.timestamp}')
    
    print('\n=== All Users ===')
    users = User.query.all()
    for u in users:
        user_analyses = Analysis.query.filter_by(user_id=u.id).count()
        print(f'User ID: {u.id}, Email: {u.email}, Name: {u.full_name}, Analyses: {user_analyses}')
