from rest_framework.response import Response

def success_Message(message="",data=None,status=200):
    return Response(
        {
            "success": True,
            "message": message,
            "data": data
        },
        status=status
    )

def error_response(message="",data=None,status=400):
    return Response(
        {
            "success":"False",
            "message":message,
            "errors":data
        },
        status=status
    )
