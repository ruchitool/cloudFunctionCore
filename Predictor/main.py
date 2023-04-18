from service import predict_req
def Predictor(request):
    try:
        inputData = request.get_json(force=True)
        print(inputData)
        if "data" in inputData:
            print(inputData["data"])
            headers = {'Access-Control-Allow-Origin': '*','Content-type':'application/json'}
            return ( {"data":predict_req(inputData["data"])},200,headers)
        else:
            headers = {'Access-Control-Allow-Origin': '*'}
            return ("No Data Found",200,headers)
    except Exception as e:
        headers = {'Access-Control-Allow-Origin': '*'}
        print("Some Error Occurred")
        return ("Some Error Occurred " + str(e),200,headers)