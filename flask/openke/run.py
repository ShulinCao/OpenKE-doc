import ctypes
import json

import pymongo
import time
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import send_from_directory

client = pymongo.MongoClient("localhost", 27017)
db = client.openke
download_collection = db.download_collection
paperList = []

def PaperListInit():
	print "Loading the papers list..."
	global paperList
	f = open("/data/disk2/private/csl/docs/openke/static/paper/list.txt")
	while (True):
		content = f.readline()
		if (content == ""):
			break
		nid = content.replace("\n", "").replace("\r", "")
		label = f.readline().replace("\n", "").replace("\r", "")
		year = f.readline().replace("\n", "").replace("\r", "")
		writer = f.readline().replace("\n", "").replace("\r", "")
		model = f.readline().replace("\n", "").replace("\r", "")
		title = f.readline().replace("\n", "").replace("\r", "")
		abstract = f.readline().replace("\n", "").replace("\r", "")
		abstract = abstract[0:400]+"..."
		filesrc = f.readline().replace("\n", "").replace("\r", "")
		img = f.readline().replace("\n", "").replace("\r", "")
		img = img.encode("utf-8")
		filesrc = filesrc.encode("utf-8")
		paperList.append({"year":year, "writer":writer, "model":model, "id":nid, "label":label, "title":title, "abstract":abstract, "filesrc":filesrc, "img":img})
	f.close()

app = Flask(__name__)
app.jinja_env.variable_start_string = '{{{{'
app.jinja_env.variable_end_string = '}}}}'
PaperListInit()
@app.route('/')
def root_home():
	global paperList
	info = {"paper":paperList}
	return render_template('home.html', info = info)

@app.route('/home')
def home_home():
	global paperList
	info = {"paper":paperList}
	return render_template('home.html', info = info)


@app.route('/index')
def index_home():
	global paperList
	info = {"paper":paperList}
	return render_template('home.html', info = info)

@app.route('/index/explore')
def index_explore():
	return render_template('explore.html')

@app.route('/index/researchers')
def index_researchers():
	return render_template('researchers.html')

@app.route('/index/students')
def index_students():
	return render_template('students.html')

@app.route('/index/embeddings')
def index_embeddings():
	return render_template('embeddings.html')

@app.route('/index/toolkits')
def index_toolkits():
	return render_template('toolkits.html')


@app.route('/index/documentation')
def index_documentation():
	return render_template('documentation.html')

@app.route('/index/contact')
def index_contact():
	return render_template('contact.html')

@app.route('/index/about')
def index_about():
	return render_template('about.html')

@app.route('/index/api')
def index_api():
	return render_template('api.html')

@app.route('/index/new')
def index_new():
	return render_template('new.html')

@app.route('/index/publications')
def index_publications():
	global paperList
	info = {"paper":paperList}
	return render_template('publications.html', info = info)

@app.route('/download/<username>')
def show_user_profile(username):
    return render_template('message.html')


@app.route('/sendMessage', methods=['POST'])
def sendMessage():
	s = request.form
	ip = request.remote_addr
	print ip
	if(s["name"] == "" or s["orgname"] == "" or s['email'] == "" or s['optionsRadios'] != u"agree"):
		return render_template("message.html")
	else:
		try:
			info = {}
			info["name"] = s["name"]
			info["orgname"] = s["orgname"]
			info["email"] = s["email"]
			info["telephone"] = s["telephone"]
			info["address"] = s["address"]
			info["time"] = time.strftime("%Y-%m-%d %H:%I:%S", time.localtime(time.time())) 
			#print info
			download_collection.insert(info)
		except Exception, err:
			print "DB Error!"
		return render_template("download.html")
    	
    	
        # try:
        #     conn = MySQLdb.connect(
        #         host=conf.get("db","db_host"),
        #         user=conf.get("db","db_name"),
        #         passwd=conf.get("db","db_password"),
        #         db=conf.get("db","db_database"),
        #         charset="utf8")
        #     cursor = conn.cursor()

        #     # insert into tasks
        #     insertSql = 'insert into message values(null,\'' \
        #                 + s["name"] + '\',\''\
        #                 + s["orgname"] + '\',\''\
        #                 + s["email"] + '\',\'' \
        #                 + s['address'] + '\',\'' \
        #                 + s['telephone'] + '\',\'' \
        #                 + str(request.remote_addr) + '\',\'' \
        #                 + str(datetime.datetime.now()) + '\')'
        #     cursor.execute(insertSql)
        #     conn.commit()

        # except MySQLdb.Error, e:
        #     print"Mysql Error %d: %s" % (e.args[0], e.args[1])
        #     return redirect("message")
        # finally:
        #     cursor.close()
        #     conn.close()
        # return send_page("download.html")

if __name__ == '__main__':
	# app.debug = True
	app.jinja_env.variable_start_string = '{{{{'
	app.jinja_env.variable_end_string = '}}}}'
	PaperListInit()
	app.run(host='0.0.0.0', port=8080)
