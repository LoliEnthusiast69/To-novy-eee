import flask

app = flask.Flask(__name__)
app.secret_key = b'eerhioh ioriosdgiofhhi ioheriohgiohhio erghiog'
app.secret_key = b'dfjfjdjfjfjffffffffdfgdggdguiui somebodyoncetoldmethatworldisgonnarollme'

from . import routes