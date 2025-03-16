from webargs import validate, fields

currency_and_convert = {
        "currency": fields.Str(
            missing="USD",
        ),
        "convert": fields.Int(
            missing=1,
            validate=[validate.Range(min=1, max=1000000, min_inclusive=True, max_inclusive=True)]
        ),
    }

