import requests

# URL address where the image is located
url = "https://search1.kakaocdn.net/argon/600x0_65_wr/ImZk3b2X1w8"

# Request the server with that URL
img_response = requests.get(url)


# If the request was successful,
if img_response.status_code == 200:
    #print(img_response.content)

    print("=========[Save Image]=======")
    with open("test.jpg", "wb") as fp:
        fp.write(img_response.content)