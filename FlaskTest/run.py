from app import app
'''The following 2 imports are for create tables in DB.'''
# from app import db
# from app.models import User

'''Sample Flask app in: https://github.com/miguelgrinberg/flasky/tree/master/app'''
if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
