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
            WITH CityGenreCounts AS (
                SELECT
                    i.BillingCity,
                    g.Name AS GenreName,
                    COUNT(*) AS GenreCount
                FROM invoices i
                JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
                JOIN tracks t ON ii.TrackId = t.TrackId
                JOIN genres g ON t.GenreId = g.GenreId
                WHERE g.Name = ?
                GROUP BY i.BillingCity, g.Name
            ),
            RankedCities AS (
                SELECT
                    BillingCity,
                    GenreName,
                    GenreCount,
                    RANK() OVER (ORDER BY GenreCount DESC) as rnk
                FROM CityGenreCounts
            )
            SELECT
                BillingCity AS City,
                GenreName AS Genre,
                GenreCount,
                rnk AS Rank
            FROM RankedCities
            ORDER BY rnk ASC, BillingCity ASC
            LIMIT ?;
    """

    genres_list = [item[0] for item in execute_query("SELECT Name FROM genres")]

    if not genre:
        return jsonify({
            "ERROR": "Input genre, like: '/stats_by_city?genre=Rock' and, you can set the limit: 'Rock&limit=10', limit by default = 5",
            "Genres": genres_list
        }), 404

    records = execute_query(query=query, args=(genre, limit))

    if not records:
        return jsonify({"ERROR": "Genre not found",
                        "Genres": genres_list
                        }), 404

    return records


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )
