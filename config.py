import os 

project_dir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY') or "You Are the Best"
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(project_dir, 'app.db')
    