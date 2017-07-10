import requests
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from details import get_user_id

APP_ACCESS_TOKEN =  '1705754005.29541b0.156ba485dedb482cbc95c8e430efa9ec'

BASE_URL = "https://api.instagram.com/v1/"

# list for the hashtags in the caption of a user
HASHTAG=[]
CAPTION=[]
IMAGE=[]
# function to find the hashtag in the caption by using split
def find_hashtag(user_id):
    url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + APP_ACCESS_TOKEN
    user_post= requests.get(url).json()
    if user_post["meta"]["code"] == 200:
        for media in user_post["data"]:
            caption=media["caption"]["text"]
            CAPTION.append(caption)

        for caption in CAPTION:
            WORD=str(caption).split(" ")
            for word in WORD:
                if str(word).find("#") != -1:
                    if find_duplicates(word):
                        HASHTAG.append(word)



    else:
        print "Error" + user_post["meta"]["code"]
        return -1

# function to find redundancy in the hashtags in the caption of a user

def find_duplicates(word):
    for hashtag in HASHTAG:
        if hashtag == word:
            return False
    return True

#function to find number of hashtags used in a users caption
def find_post():
    for hashtag in HASHTAG:
        counter=0
        for caption in CAPTION:
            if str(caption).find(hashtag)>=0:
                counter+=1
        IMAGE.append(counter)

# function to plot the graph
def plot_graph():
    objects= HASHTAG
    y_pos= np.arange(len(objects))
    performance= IMAGE

    plt.bar(y_pos, performance,align='center',alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Popularity')
    plt.title('Trending analysis')

    plt.show()




# function to get the post of a user having hashtag

def get_post_with_hashtag(username):
    user_id=get_user_id(username)
    find_hashtag(user_id)




def get_image_with_hashtag(username):
    user_id=get_user_id(username)
    find_hashtag(user_id)
    find_post()

    sno = 0
    for h in HASHTAG:
        print str(sno+1) + h +" : "+ str(IMAGE[sno])
        sno += 1
    plot_graph()

get_image_with_hashtag("vikrant7am")