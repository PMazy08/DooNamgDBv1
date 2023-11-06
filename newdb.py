from flask import Flask, jsonify,request
import mysql.connector

app = Flask(__name__)

# ข้อมูลการเชื่อมต่อ
host = "localhost"
user = "root"
password = "root"
database = "movie_db"

# สร้างการเชื่อมต่อ MySQL
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
###################   movies
@app.route("/movie")
def get_dog_data():
    cursor = connection.cursor()

    # ตัวอย่าง query
    query = "SELECT movies.movieId, movies.name_movie, movies.videoLink, genre.name_genre, rate.name_rate, movies.pic_movie FROM movies,rate,genre WHERE movies.rate = rate.rateId and movies.genre = genre.genreId "


    # สั่ง execute query
    cursor.execute(query)

    # ดึงข้อมูล
    result = cursor.fetchall()

    print("Number=",cursor.rowcount)
    # ปิด cursor
    cursor.close()  

    # แปลงข้อมูลให้เป็น JSON
    data = [{"movieId": row[0], "name_movie": row[1], "videoLink": row[2], "genre": row[3], "rate": row[4],"pic_movie": row[5]} for row in result]
    return jsonify(data)

# @app.route("/movie/<name>")
# def get_movie_by_name(name):
#     cursor = connection.cursor()

#     # Use a parameterized query with LIKE for partial matching
#     query = "SELECT * FROM movies WHERE name_movie LIKE %s"
#     cursor.execute(query, ('%' + name + '%',))

#     # Get the data
#     result = cursor.fetchall()

#     print("Number=", cursor.rowcount)
#     cursor.close()

#     # Convert the data to JSON
#     data = [{"movieId": row[0], "name_movie": row[1], "videoLink": row[2], "genre": row[3], "rate": row[4], "pic_movie": row[5]} for row in result]
#     return jsonify({"data": data})


@app.route("/update/movie/<movieid>", methods=["PUT"])
def update_movie(movieid):
    cursor = connection.cursor()

    # Extract updated data from request (assuming it's sent in JSON format)
    updated_data = request.get_json()

    # Use a parameterized query to update the movie information
    query = "UPDATE movies SET name_movie=%s, videoLink=%s, genre=%s, rate=%s, pic_movie=%s WHERE movieId =%s"

    cursor.execute(query, (updated_data["name_movie"], updated_data["videoLink"], updated_data["genre"], updated_data["rate"], updated_data["pic_movie"], movieid))

    # Commit the changes to the database
    connection.commit()

    cursor.close()

    return jsonify({"message": "Movie updated successfully"})


@app.route("/insert", methods=["POST"])
def insert_movie():
    if request.method == "POST":
        cursor = connection.cursor()

        # Get data from the request
        name = request.json.get("name_movie")
        link = request.json.get("videoLink")
        genre = request.json.get("genre")
        rate = request.json.get("rate")
        pic = request.json.get("pic_movie")

        # Execute the insert query
        query = "INSERT INTO movies (name_movie, videoLink, genre,rate,pic_movie) VALUES (%s, %s, %s,%s,%s)"
        values = (name, link, genre,rate,pic)
        cursor.execute(query, values)
        connection.commit()

        # Close cursor
        cursor.close()

        return jsonify({"message": "Data inserted successfully."})
    


# @app.route("/movieid/<movieid>")
# def get_movies_by_id(movieid):
#     cursor = connection.cursor()

#     # Use a parameterized query to select by genre
#     query = "SELECT * FROM movies WHERE movieId = %s"
#     cursor.execute(query, (movieid,))

#     # Get the data
#     result = cursor.fetchall()

#     print("Number=", cursor.rowcount)
#     cursor.close()

#     # Convert the data to JSON
#     data = [{"movieId": row[0], "name_movie": row[1], "videoLink": row[2], "genre": row[3], "rate": row[4], "pic_movie": row[5]} for row in result]
#     return jsonify({"data": data})



@app.route("/delete_movie/<movieid>", methods=["DELETE"])
def delete_movie(movieid):
    cursor = connection.cursor()

    # Use a parameterized query to delete the movie
    query = "DELETE FROM movies WHERE movieId = %s"
    cursor.execute(query, (movieid,))

    # Commit the changes to the database
    connection.commit()

    cursor.close()

    return jsonify({"message": "Movie deleted successfully"})


#######################  user
#######################  user
#######################  user
#######################  user
#######################  user
#######################  user
#######################  user

# @app.route("/user")
# def get_user():
#     cursor = connection.cursor()

#     # ตัวอย่าง query
#     query = "SELECT * FROM user"

#     # สั่ง execute query
#     cursor.execute(query)

#     # ดึงข้อมูล
#     result = cursor.fetchall()

#     print("Number=",cursor.rowcount)
#     # ปิด cursor
#     cursor.close()  

#     # แปลงข้อมูลให้เป็น JSON
#     data = [{"userId": row[0], "username": row[1], "pass": row[2], "role": row[3]} for row in result]
#     return jsonify(data)


@app.route("/user/<username>")
def get_username(username):
    cursor = connection.cursor()

    # ตัวอย่าง query
    query = "SELECT * FROM user WHERE username = %s"
    cursor.execute(query, (username,))
    # สั่ง execute query
    cursor.execute(query)

    # ดึงข้อมูล
    result = cursor.fetchall()

    print("Number=",cursor.rowcount)
    # ปิด cursor
    cursor.close()  

    # แปลงข้อมูลให้เป็น JSON
    data = [{"userId": row[0], "username": row[1], "pass": row[2], "role": row[3]} for row in result]
    return jsonify(data)


@app.route("/insert/user", methods=["POST"])
def insert_user():
    if request.method == "POST":
        cursor = connection.cursor()

        # Get data from the request
        user = request.json.get("username")
        password = request.json.get("pass")
    
     

        # Execute the insert query
        query = "INSERT INTO user (username, pass, role) VALUES (%s, %s,'user')"
        values = (user, password)
        cursor.execute(query, values)
        connection.commit()

        # Close cursor
        cursor.close()

        return jsonify({"message": "Data inserted successfully."}), 201
    
# @app.route("/search_user/<username>")
# def search_user(username):
#     cursor = connection.cursor()

#     # Construct a query to search for users by username
#     query = "SELECT * FROM user WHERE username = %s"
#     cursor.execute(query, (username,))

#     # Get the data
#     result = cursor.fetchall()

#     cursor.close()

#     # Convert the data to JSON
#     data = [{"userId": row[0], "username": row[1], "pass": row[2], "role": row[3]} for row in result]
#     return jsonify(data)   


#######################  Review
#######################  Review
#######################  Review
#######################  Review
#######################  Review

@app.route("/reviews")
def get_reviews():
    cursor = connection.cursor()

    # ตัวอย่าง query
    query = "SELECT * FROM reviews"

    # สั่ง execute query
    cursor.execute(query)

    # ดึงข้อมูล
    result = cursor.fetchall()

    print("Number=",cursor.rowcount)
    # ปิด cursor
    cursor.close()  

    # แปลงข้อมูลให้เป็น JSON
    data = [{"reviewsId": row[0], "movieId": row[1], "userId": row[2], "comment": row[3]} for row in result]
    return jsonify(data)

# @app.route("/reviews/user/<userId>")
# def get_reviews_userid(userId):
#     cursor = connection.cursor()

#     # ตัวอย่าง query
#     query = "SELECT * FROM reviews where userId = %s"
#     # สั่ง execute query
#     cursor.execute(query,(userId,))

#     # ดึงข้อมูล
#     result = cursor.fetchall()

#     print("Number=",cursor.rowcount)
#     # ปิด cursor
#     cursor.close()  

#     # แปลงข้อมูลให้เป็น JSON
#     data = [{"reviewsId": row[0], "movieId": row[1], "userId": row[2], "comment": row[3]} for row in result]
#     return jsonify({"data": data})

@app.route("/reviews/movie/<movieid>")
def get_reviews_movieid(movieid):
    cursor = connection.cursor()

    # ตัวอย่าง query
    query = "SELECT * FROM reviews where movieId = %s"
    # สั่ง execute query
    cursor.execute(query,(movieid,))

    # ดึงข้อมูล
    result = cursor.fetchall()

    print("Number=",cursor.rowcount)
    # ปิด cursor
    cursor.close()  

    # แปลงข้อมูลให้เป็น JSON
    data = [{"reviewsId": row[0], "movieId": row[1], "userId": row[2], "comment": row[3]} for row in result]
    return jsonify(data)


@app.route("/insert/review", methods=["POST"])
def insert_review():
    if request.method == "POST":
        cursor = connection.cursor()

        # Get data from the request
        comment = request.json.get("comment")
        movieId = request.json.get("movieId")
        userId = request.json.get("userId")
    
     

        # Execute the insert query
        query = "INSERT INTO reviews (movieId, userId,comment) VALUES (%s, %s,%s)"
        values = (movieId,userId,comment)
        cursor.execute(query, values)
        connection.commit()

        # Close cursor
        cursor.close()

        return jsonify({"message": "Data inserted successfully."}), 201




# +++================================================

@app.route("/select/genre")
def get_gen():
    cursor = connection.cursor()

    # ตัวอย่าง query
    query = "SELECT * FROM genre"

    # สั่ง execute query
    cursor.execute(query)

    # ดึงข้อมูล
    result = cursor.fetchall()

    print("Number=",cursor.rowcount)
    # ปิด cursor
    cursor.close()  

    # แปลงข้อมูลให้เป็น JSON
    data = [{"genreId": row[0], "name_genre": row[1]} for row in result]
    return jsonify(data)



# +++================================================

@app.route("/select/rate")
def get_rate():
    cursor = connection.cursor()

    # ตัวอย่าง query
    query = "SELECT * FROM rate"

    # สั่ง execute query
    cursor.execute(query)

    # ดึงข้อมูล
    result = cursor.fetchall()

    print("Number=",cursor.rowcount)
    # ปิด cursor
    cursor.close()  

    # แปลงข้อมูลให้เป็น JSON
    data = [{"rateId": row[0], "name_rate": row[1]} for row in result]
    return jsonify(data)


# @app.route("/genre/<genre>")
# def get_movies_by_genre(genre):
#     cursor = connection.cursor()

#     # Use a parameterized query to select by genre
#     query = "SELECT * FROM movies,genre WHERE genre = genreId and name_genre LIKE %s"
#     cursor.execute(query, ('%' + genre + '%',))

#     # Get the data
#     result = cursor.fetchall()

#     print("Number=", cursor.rowcount)
#     cursor.close()

#     # Convert the data to JSON
#     data = [{"movieId": row[0], "name_movie": row[1], "videoLink": row[2], "genre": row[3], "rate": row[4], "pic_movie": row[5]} for row in result]
#     return jsonify({"data": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)