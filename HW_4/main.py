from flask import Flask, request, jsonify
from database_handler import execute_query
from webargs.flaskparser import use_kwargs
from webargs import validate, fields

app = Flask(__name__)


@app.route("/order-price")
@use_kwargs(
    {
        "country": fields.Str(
            load_default=None,
        ),
    },
    location="query"
)
def order_price(country):
    query = "SELECT BillingCountry AS COUNTRY, SUM(Total) AS SALES FROM invoices"

    if country:
        query += f" WHERE BillingCountry = ?"

    query += ' GROUP BY BillingCountry ORDER BY SALES DESC'

    if country:
        records = execute_query(query=query, args=(country,))
    else:
        records = execute_query(query=query)

    return records


@app.route("/info-about-track")
@use_kwargs(
    {
        "track_id": fields.Str(
            load_default=None,
        ),
    },
    location="query"
)
def get_all_info_about_track(track_id):
    query = """
    SELECT * FROM (
        SELECT
            tracks.TrackId,
            tracks.Name AS 'TRACK NAME',
            albums.Title AS 'ALBUM NAME',
            genres.Name AS 'GENRE NAME',
            artists.Name AS 'ARTIST NAME',
            tracks.Composer AS 'COMPOSER',
            media_types.Name AS 'MEDIA TYPE',
            ROUND(tracks.Milliseconds / 60000.0, 2) AS 'SONG DURATION (MIN)',
            GROUP_CONCAT(DISTINCT playlists.Name) AS 'PLAYLIST NAMES',
            ROUND(
                (SELECT SUM(tr.Milliseconds)
                 FROM tracks tr
                 WHERE tr.AlbumId = albums.AlbumId
                ) / 3600000.0, 2) AS 'TOTAL ALBUM DURATION (HOURS)'
        FROM tracks
        JOIN genres ON tracks.GenreId = genres.GenreId
        JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
        JOIN albums ON tracks.AlbumId = albums.AlbumId
        JOIN artists ON albums.ArtistId = artists.ArtistId
        LEFT JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
        LEFT JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
        GROUP BY tracks.TrackId
    )
    """


    if track_id:
        query += f" WHERE TrackId = ?"
        records = execute_query(query=query, args=(track_id,))
    else:
        records = execute_query(query=query)

    if not records:
        return jsonify({"message": "Track not found"}), 404

    column_names = [
        "TrackId",
        "TRACK NAME",
        "ALBUM NAME",
        "GENRE NAME",
        "ARTIST NAME",
        "COMPOSER",
        "MEDIA TYPE",
        "SONG DURATION (MIN)",
        "PLAYLIST NAMES",
        "TOTAL ALBUM DURATION (HOURS)"
    ]


    if track_id:
        result_dict = dict(zip(column_names, records[0]))
    else:
        result_dict = [dict(zip(column_names, row)) for row in records]

    return result_dict


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )
