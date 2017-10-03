from flask import Flask, render_template, request

form = Flask(__name__)

@form.route('/')
def root():
    return render_template("root.html")

@form.route('/result', methods = ['POST', 'GET'])
def requests():
    return render_template("result.html", user = request.form["data"],
                           method = request.method)


if __name__ == "__main__":
    form.debug = True
    form.run()


"""
print "\n\n\n"
print "app:"
print app
print "request.headers:"
print request.headers
print "request.method:"
print request.method
print "request.args:"
print request.args
print "request.args['username']:"
print request.args['username']
print "request.args['password']:"
print request.args['password']"""
