from flask import Flask, request, jsonify
from database_handler import execute_query
from webargs.flaskparser import use_kwargs
from webargs import validate, fields

app = Flask(__name__)


@app.route("/stats_by_city")
@use_kwargs(
    {
        "genre": fields.Str(
            load_default=None,
        ),
        "limit": fields.Str(
            load_default='5',
        )
    },
    location="query"
)
def stats_by_city(genre, limit):
    query = """
            SELECT BillingCity AS City, 
                   genres.Name AS Genre, 
                   COUNT(*) AS GenreCount
            FROM invoices
            JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
            JOIN tracks ON invoice_items.TrackId = tracks.TrackId
            JOIN genres ON tracks.GenreId = genres.GenreId
            WHERE genres.Name = ?
            GROUP BY BillingCity, genres.Name
            ORDER BY GenreCount DESC
            LIMIT ?;
    """

    if not genre:
        return jsonify({
            "ERROR": "Input genre, like: '/stats_by_city?genre=Rock' and, you can set the limit: 'Rock&limit=10', limit by default = 5",
            "Genres": [
                "Rock", "Jazz", "Metal", "Alternative & Punk", "Rock And Roll", "Blues", "Latin",
                "Reggae", "Pop", "Soundtrack", "Bossa Nova", "Easy Listening", "Heavy Metal",
                "R&B/Soul", "Electronica/Dance", "World", "Hip Hop/Rap", "Science Fiction",
                "TV Shows", "Sci Fi & Fantasy", "Drama", "Comedy", "Alternative", "Classical", "Opera"
            ]
        }), 404

    records = execute_query(query=query, args=(genre, limit))

    if not records:
        return jsonify({"ERROR": "Genre not found",
                        "Genres": [
                            "Rock", "Jazz", "Metal", "Alternative & Punk", "Rock And Roll", "Blues", "Latin",
                            "Reggae", "Pop", "Soundtrack", "Bossa Nova", "Easy Listening", "Heavy Metal",
                            "R&B/Soul", "Electronica/Dance", "World", "Hip Hop/Rap", "Science Fiction",
                            "TV Shows", "Sci Fi & Fantasy", "Drama", "Comedy", "Alternative", "Classical", "Opera"
                        ]
                        }), 404

    return records


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )
