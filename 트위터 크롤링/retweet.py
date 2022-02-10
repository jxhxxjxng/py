import pymysql
from selenium import webdriver
import time

# MYSQL CONNECTION
conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, db=db_name, charset='utf8')

# DICTIONARY CURSOR
curs = conn.cursor(pymysql.cursors.DictCursor)

# GET: msg_id, user_id
sql = 'SELECT user_id, msg_id FROM msgs'
curs.execute(sql)
rows = curs.fetchall()
print('rows',len(rows))

# INITIALIZE WEB DRIVER
driver_path = 'D:/Users/1/python/Scripts/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.implicitly_wait(3) # or bigger seconds

# CONSTANT: TWITTER LOGIN
url_login = 'https://twitter.com/i/flow/login'
xpath_user_account = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
xpath_user_passwd = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input'
btn_login = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/span'



# TWITTER LOGIN
driver.get(url_login)
time.sleep(2)
driver.find_element_by_xpath(xpath_user_account).send_keys(user_account)
driver.find_element_by_xpath(xpath_user_passwd).send_keys(user_password)
driver.find_element_by_xpath(btn_login).click()

for row in rows:
    user_id = str(row['user_id'])
    msg_id = str(row['msg_id'])
    rt_users = set()
    
    url_retweet = 'https://mobile.twitter.com/'+user_id+'/status/'+msg_id+'/retweets'
    
    print(url_retweet)
    
    driver.get(url_retweet)
    time.sleep(2)
    
    # GET SCROLL HEIGHT
    last_height = driver.execute_script('return document.body.scrollHeight')
    
    while True:    
        elem = driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div[2]/div/section/div')
        arr = elem.text.split('\n')
        for i in range(1, len(arr), 3):
            rt_users.add(arr[i][1:])
            
        # SCROLL THE WEB PAGE        
        # IF It doesn't crawl all rt users, change second number smaller.
        #    EX: 1080 -> 720
        driver.execute_script('window.scrollBy(0, 1080);')

        # Wait to load page
        time.sleep(0.5)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script('return document.body.scrollHeight')
        
#         print(last_height, new_height, len(rt_users))
        
        if new_height == last_height:
            break
        last_height = new_height
    
    for user in rt_users:
        sql = "INSERT IGNORE INTO users (user_id) VALUES (%s)"
        curs.execute(sql, (user))
    
conn.commit()

# CLOSE WEB DRIVER
driver.close()

# MYSQL CLOSE
conn.close()
