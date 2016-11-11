from app import app
# from app import db

'''Sample Flask app in: https://github.com/miguelgrinberg/flasky/tree/master/app'''
if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
