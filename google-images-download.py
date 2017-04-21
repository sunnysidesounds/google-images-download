#Searching and Downloading Google Images/Image Links

#Import Libraries

import time       #Importing the time library to check the time of code execution
import sys    #Importing the System Library
import os

import urllib2


########### Edit From Here ###########

#This list is used to search keywords. You can edit this list to search for google images of your choice. You can simply add and remove elements of the list.
search_keyword = ['Scallions',
                  'Yeast',
                  'Pistachios',
                  'Prawns',
                  #'Splenda',
                  #'Sambaar Powder',
                  #'Water',
                  #'Jalapeno',
                  #'Jalapenos',
                  #'Zucchini',
                  #'Eggplant',
                  #'Chilies',
                  #'Chili Pods',
                  #'Ziti',
                  #'Heirloom Tomatoes',
                  #'Squashbell Peppers',
                  #'Maraschino Cherries',
                  #'Cobbler Crust',
                  #'Asian Spice',
                  #'Sweet Potatoes',
                  #'Yogurt',
                  #'Graham Cracker',
                  #'Cilantro',
                  #'Hot Sauce',
                  #'Jalapeno Chilies',
                  #'Yam',
                  #'Pine Nuts',
                  #'Streusel',
                  #'Cocoa',
                  #'Vinaigrette',
                  #'Shitake Mushrooms',
                  #'Poblano Peppers',
                  #'Bell Peppers',
                  #'Scallion',
                  #'Flax Seed',
                  #'Lemonmustard Sauce',
                  #'Chili Powder',
                  #'Falafel',
                  #'Cardamoms',
                  #'Graham Wafer',
                  #'Nutella',
                  #'Cornstarch',
                  #'Food Coloring',
                  #'Licor',
                  #'Chilled Prosecco',
                  #'Bottle Rose',
                  #'Whiskey',
                  #'Ice',
                  #'Crushed Ice',
                  #'Vadouvan',
                  #'Cornmeal',
                  #'Agave Nectar',
                  #'Sriracha',
                  #'Peppermint Extract',
                  #'Parsnips',
                  #'Pitted Prunes',
                  #'Arugula',
                  #'Other',
                  #'Hot Chiles',
                  #'Matcha Powder',
                  #'Bourbon',
                  #'Seltzer',
                  #'Vegetable Bouillon',
                  #'Cereal',
                  #'Chile Peppers',
                  #'Eggplants',
                  #'Green Chartreuse',
                  #'Aperol',
                  #'Edamame',
                  #'Baharat',
                  #'Fresno Chile',
                  #'Limeade',
                  #'Parmigianoreggiano',
                  #'Applesauce',
                  #'Aperol',
                  #'Curacao',
                  #'Cornflake',
                  #'Angostura',
                  #'Benedictine',
                  #'Scotch',
                  #'Grand Marnier',
                  #'Creme Fraiche',
                  #'Rutabagas',
                  #'Persimmon',
                  #'Phyllo Sheets',
                  #'Triple Sec',
                  #'Limonada',
                  #'Oaxacan Mezcal',
                  #'Marinara',
                  #'Bison',
                  #'Chopmeat',
                  #'Peppers',
                  #'Liquid Smoke',
                  #'Espresso Powder',
                  #'Candy Canes',
                  #'Pilsners',
                  #'Edible Flowers',
                  #'Chartreuse',
                  #'Dubonnet Rouge',
                  #'Sake',
                  #'Porter',
                  #'Fillet',
                  #'Rockfish',
                  #'Echinacea',
                  #'Ginseng',
                  #'Elderberry Extract',
                  #'Cocacola',
                  #'Cookies',
                  #'Cookie',
                  #'Bulgur',
                  #'Aloe Vera',
                  #'Green Sprinkles',
                  #'Pisco',
                  #'Lillet Blanc',
                  #'Saba',
                  #'Prosecco',
                  #'Campari',
                  #'Matzohs',
                  #'Rye',
                  #'Chevre',
                  #'Zuchinnis',
                  #'Soy Sauce',
                  #'Tuna',
                  #'Kiwifruit',
                  #'Candy',
                  #'Pecans',
                  #'Yellow Tomato',
                  #'Garnish',
                  #'Dressing',
                  #'Kaiser Rolls',
                  #'Wheat Germ',
                  #'Worchestershire',
                  #'Marinade',
                  #'Sausages',
                  #'Chile Powder',
                  #'Chili',
                  #'Bulghur',
                  #'Caramels',
                  #'Escarole',
                  #'Serrano Chile',
                  #'Fettucine',
                  #'Jalapeno',
                  #'Panko',
                  #'Figs',
                  #'Paparika',
                  #'Cabernet Sauvignon',
                  #'Worcester Sauce',
                  #'Old Bay',
                  #'Evoo',
                  #'Nuts',
                  #'Orecchiette',
                  #'Cornstartch',
                  #'Cornichons',
                  #'Picante',
                  #'Crisco',
                  #'Parmigiano Reggiano',
                  #'Maltagliati',
                  #'Aquavit',
                  #'Half and Half',
                  #'Mamey',
                  #'Flowers',
                  #'Gelatin',
                  #'Filet Mignon',
                  #'Creme De Cassis',
                  #'Decorative Sugars',
                  #'White Pudding',
                  #'Pudding',
                  #'Limoncello',
                  #'Passion Fruit Juice',
                  #'Flower',
                  #'Roll',
                  #'Rolls',
                  #'Spirulina Powder',
                  #'Psyllium Husk Powder',
                  #'Dried Chile',
                  #'Chile',
                  #'Jello',
                  #'Cachaca',
                  #'Nibs',
                  #'Coolwhip',
                  #'Arugular',
                  #'Leafy Greens',
                  #'Rib Eyes',
                  #'Rib Eye',
                  #'Whole Nutmegs',
                  #'Merlot',
                  #'Belgian Endive',
                  #'Yuzu Juice',
                  #'Ground Flaxseeds',
                  #'Skillet Drippings',
                  #'Pita',
                  #'Persimmons',
                  #'Cakes',
                  #'Baby Greens',
                  #'Matzoh',
                  #'Gruyere',
                  #'Pecorinoromano',
                  #'Agar Powder',
                  #'Panna Cotta',
                  #'Tart Shell',
                  #'Crust',
                  #'Zeera Powder',
                  #'Truffles',
                  #'Tagliolini',
                  #'Gremolata',
                  #'Poppyseed',
                  #'Worstershire',
                  #'Tomato Paste',
                  #'Pico',
                  #'Tater Tots',
                  #'Rainforest Rub',
                  #'Gruyere',
                  #'Tarte',
                  #'Amandes Effilees',
                  #'Orzo',
                  #'Red Plums',
                  #'Dough',
                  #'Chuck Roast',
                  #'Roast',
                  #'Breadcumbs',
                  #'Rub',
                  #'Rose Extract',
                  #'Grits',
                  #'Xylitol',
                  #'Swerve Sweetener',
                  #'Asiago',
                  #'Plums',
                  #'Topping',
                  #'Toppings',
                  #'Pinenuts',
                  #'Linguini',
                  #'Brussel Sprouts',
                  #'Sprouts',
                  #'Five-Spice Powder',
                  #'Onion Powder',
                  #'Ancho Powder',
                  #'Shortening',
                  #'Croutons',
                  #'Marsala',
                  #'Xanthan',
                  #'Cantaloupe',
                  #'Salt Pepper Mix',
                  #'Soy Milk',
                  #'Grenadine',
                  #'Hamburger',
                  #'Zxcvbnm',
                  'Bisquick']

#This list is used to further add suffix to your search term. Each element of the list will help you download 100 images. First element is blank which denotes that no suffix is added to the search keyword of the above list. You can edit the list by adding/deleting elements from it.So if the first element of the search_keyword is 'Australia' and the second element of keywords is 'high resolution', then it will search for 'Australia High Resolution'
keywords = [' thumbnail']

########### End of Editing ###########

#Downloading entire Web Document (Raw Page Content)
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


# Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def create_directory(directory):
    if not os.path.exists(directory):
        print "Creating : " + directory
        os.makedirs(directory)


# Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    count = 0
    while True:
        if count == 10:
            break

        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            print "  link : " + item
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
        count = count + 1
    items.append("end")
    return items


############## Main Program ############
t0 = time.time()   #start the timer

# Download Image Links
i= 0
keyword_list = []
full_item_list = []
while i<len(search_keyword):
    items = []
    iteration = "Item no.: " + str(i+1) + " -->" + " Item name = " + str(search_keyword[i])
    print (iteration)
    print ("Evaluating...")
    search_keywords = search_keyword[i]

    print "KEYWORD : " + search_keywords
    search = search_keywords.replace(' ','%20')
    j = 0
    keyword_list.append(search_keywords.lower())
    while j<len(keywords):
        pure_keyword = keywords[j].replace(' ','%20')
        url = 'https://www.google.com/search?q=' + search + pure_keyword + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
        raw_html =  (download_page(url))
        time.sleep(0.1)
        items = items + (_images_get_all_items(raw_html))


        j = j + 1
    #print ("Image Links = "+str(items))
    full_item_list.extend(items)
    print ("Total Image Links = "+str(len(items)))
    print ("\n")
    i = i+1


    #This allows you to write all the links into a test file. This text file will be created in the same directory as your code. You can comment out the below 3 lines to stop writing the output to the text file.
    info = open('output.txt', 'a')        #Open the text file called database.txt
    info.write(str(i) + ': ' + str(search_keyword[i-1]) + ": " + str(items) + "\n\n\n")         #Write the title of the page
    info.close()                            #Close the file


t1 = time.time()    #stop the timer
total_time = t1-t0   #Calculating the total time required to crawl, find and download all the links of 60,000 images
print("Total time taken: "+str(total_time)+" Seconds")
print ("Starting Download...")

## To save imges to the same directory
# IN this saving process we are just skipping the URL if there is any error

k=0
kl=0
errorCount=0

print keyword_list

while(k<len(full_item_list)):
    from urllib2 import Request,urlopen
    from urllib2 import URLError, HTTPError

    try:
        print "Downloading link : " + full_item_list[k]
        if full_item_list[k] == 'end':
            kl = kl + 1

        else:

            req = Request(full_item_list[k], headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
            response = urlopen(req)

            print "  folder : " + keyword_list[kl]
            create_directory("images/" + keyword_list[kl])
            output_file = open("images/" + keyword_list[kl] + "/" + keyword_list[kl]+"_"+str(k+1)+".jpg",'wb')
            data = response.read()
            output_file.write(data)
            response.close();

            print("  completed ====> "+str(k+1))

        k=k+1;

    except IOError as e:   #If there is any IOError

        errorCount+=1
        print("IOError on image "+str(k+1))
        print e
        k=k+1;

    except HTTPError as e:  #If there is any HTTPError

        errorCount+=1
        print("HTTPError"+str(k))
        k=k+1;
    except URLError as e:

        errorCount+=1
        print("URLError "+str(k))
        print e
        k=k+1;

print("\n")
print("All are downloaded")
print("\n"+str(errorCount)+" ----> total Errors")

#----End of the main program ----#
