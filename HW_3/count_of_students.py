from webargs import validate, fields

count_of_students = {
        "count_of_students": fields.Int(
            missing=10,
            validate=[validate.Range(min=1, max=1000, min_inclusive=True, max_inclusive=True)]
        ),
    }