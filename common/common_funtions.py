
def generate_201_base_response():
    return {
        201: "Created",
        400: "Bad Request",
        500: "Internal Server Error"
    }


def generate_200_base_response():
    return {
        200: "OK",
        204: "No Data",
        400: "Bad Request",
        500: "Internal Server Error"
    }


def generate_200_model_response(response_model):
    return {
        200: response_model,
        204: "No Data",
        400: "Bad Request",
        500: "Internal Server Error"
    }
