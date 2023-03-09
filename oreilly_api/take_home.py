from flask import Flask
import psycopg2
app = Flask(__name__)
#this needs to be stored as a k8s secret and passed as an env var in production:
conn_string = "host='172.17.0.2' dbname='oreilly' user='oreilly' password='hunter2'"
conn = psycopg2.connect(conn_string)
conn.autocommit = True

def fetch_data(query, call_type, value):
    cursor = conn.cursor()
    sql = query
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.commit()
    if results:
        return results
    else:
        return f"The following search '{call_type}': {value} returned no data"
    conn.close()

@app.route("/", methods=['GET'])
def main_page():
    return """Welcome to our web catalog API! Here's a list of api calls you can make: <br><br>
    /orapi/_all - fetch all of the books in our catalog <br>
    /orapi/search/_isbn/<isbn> - search by isbn <br>
    /orapi/search/_authors/<author> - search by author <br>
    /orapi/search/_books/<title_search> - search by a keyword in a books's title
    """

#get all
@app.route("/orapi/_all", methods=['GET'])
def get_all():
    psql_q = "SELECT * FROM works;"
    return fetch_data(psql_q, "all", "all")

#search by ISBN
@app.route("/orapi/search/_isbn/<isbn>", methods=['GET'])
def isbn_search(isbn):
    psql_q = f"SELECT * FROM works where isbn = '{isbn}';"
    return fetch_data(psql_q, "isbn", isbn)

#search by author, ILIKE to ignore case
@app.route("/orapi/search/_authors/<author>", methods=['GET'])
def author_search(author):
    psql_q = f"SELECT * FROM works where authors ILIKE '%{author}%';"
    return fetch_data(psql_q, "author", author)

#search by a keyword in the title, ILIKE to ignore case
@app.route("/orapi/search/_books/<title_search>", methods=['GET'])
def title_search(title_search):
    psql_q = f"SELECT * FROM works where title ILIKE '%{title_search}%';"
    return fetch_data(psql_q, "title_search", title_search)

app.run(host="0.0.0.0", port=5051)
