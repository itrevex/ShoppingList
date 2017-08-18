#!flask/bin/python
from app import APP

if __name__=="__main__":
    """
    start app only through main
    """
    APP.run(debug=True)