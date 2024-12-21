import websocket
import json
import hmac
import hashlib
import base64
from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time
from urllib.parse import urlencode


def generate_auth_url(api_key, api_secret, host, path):
    """Generate the authenticated WebSocket URL."""
    # Generate the date in RFC1123 format
    cur_time = datetime.now()
    date = format_date_time(mktime(cur_time.timetuple()))

    # Construct the string to sign
    tmp = f"host: {host}\n"
    tmp += f"date: {date}\n"
    tmp += f"GET {path} HTTP/1.1"

    # Generate the HMAC-SHA256 signature
    tmp_sha = hmac.new(api_secret.encode('utf-8'), tmp.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(tmp_sha).decode('utf-8')

    # Construct the authorization header
    authorization_origin = (
        f"api_key=\"{api_key}\", algorithm=\"hmac-sha256\", headers=\"host date request-line\", "
        f"signature=\"{signature}\""
    )

    # Base64 encode the authorization header
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode('utf-8')

    # Construct the final URL
    params = {
        "authorization": authorization,
        "date": date,
        "host": host,
    }
    url = f"wss://{host}{path}?" + urlencode(params)
    return url


def on_message(ws, message):
    """Callback when a message is received."""
    print("Response received:", message)


def on_error(ws, error):
    """Callback when an error occurs."""
    print("Error occurred:", error)


def on_close(ws, close_status_code, close_msg):
    """Callback when the connection is closed."""
    print("Connection closed")


def on_open(ws, app_id, uid,patch_id,domain, temperature, message_content):
    """Callback when the connection is opened."""
    request_payload = {
        "header": {
            "app_id": app_id,
            "uid": uid,
            "patch_id": [patch_id]
        },
        "parameter": {
            "chat": {
                "domain": domain,
                "temperature": temperature
            }
        },
        "payload": {
            "message": {
                "text": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant."
                    },
                    {"role": "user", "content": message_content}
                ]
            }
        }
    }

    ws.send(json.dumps(request_payload))
    print("Request sent")


if __name__ == "__main__":
    # Define parameters in main function
    # app_id = "1b9e6510"  # 填写APPId
    # uid = "12345"  # 用于区分用户，可以不填
    # domain = "xqwen257bchat"  # 填写serviceId
    # patch_id = "1865753247489093632" # 填写sourceId，填写sourceId是为了匹配你训练的模型
    # temperature = 0.5
    # message_content = "你是谁"
    #
    # # Replace with your actual credentials and endpoint details
    # api_key = "c955f9684aa57d5883b70eb978b0a906" #填写APIKey
    # api_secret = "ZWE1ZTdiNTliZWQzN2Q0NDAyM2QxOTk3" #填写APISecret
    # host = "maas-api.cn-huabei-1.xf-yun.com"
    # path = "/v1.1/chat"

    app_id = "d9fbaa54"  # 填写APPId
    uid = "12345"  # 用于区分用户，可以不填
    domain = "xqwen257bchat"  # 填写serviceId
    patch_id = "1868476612280877056"  # 填写sourceId，填写sourceId是为了匹配你训练的模型
    temperature = 0.3
    # message_content = "DataWhaleLearner大模型是什么？"
    message_content = "如何确定轻量化模型的优化方向"
    # message_content = "你是谁？"
    # message_content = "采用多个不同anchor是否能够优化小尺寸和不规则尺寸目标的检测性能？"
    # message_content = "我是一个在学习开源项目过程中遇到了问题的学习者，我该做什么"

    # Replace with your actual credentials and endpoint details
    api_key = "ae5f517b2b4e37b51235d3edc7fe657f"  # 填写APIKey
    api_secret = "YWI1ODdjZWM5NTVmMTM3ODFkMDQxNTM2"  # 填写APISecret
    host = "maas-api.cn-huabei-1.xf-yun.com"
    path = "/v1.1/chat"

    # Generate the WebSocket URL
    ws_url = generate_auth_url(api_key, api_secret, host, path)

    # Disable verbose WebSocket trace logs
    websocket.enableTrace(False)

    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    # Pass parameters to the on_open function
    ws.on_open = lambda ws: on_open(ws, app_id, uid, patch_id,domain, temperature, message_content)

    ws.run_forever()
