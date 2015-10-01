from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import os.path

def clickOnAd(driver):
    try:
        res = driver.find_element_by_xpath("//*[contains(text(),'Skip Ad')]").click()        
    except:
        print("didn't find ad video ad insertion")
#The function receive a string indicate the requested video quality
def downloadVideo(video_quality,video_name, url, duration_of_the_video):
    """
        The function receives:
        - video _quality: which indicates what quality the robot will download: 360P,480P,720P or AUTO mode.
        - video_name: we used it to create a new folder for this video. if the folder exists we only save the PCAP in to this specific folder.
        - url: video url
        - duration_of_the_video: when to stop recording the video. In my testing the duration of the video was enough (even with ads). If it is change increase it.
        
    """
    t_time = time.strftime("%H_%M_%S")
    funcInFile = "Test"
    #create pcap folder
    root_path = "C:\\Users\\user\\Desktop\\ranTests\\pcap\\"
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    #create video folder    
    video_path = root_path + video_name +"\\"
    if not os.path.exists(video_path):
        os.makedirs(video_path)
    
    #create quality folder
    quality_path =  video_path +  funcInFile + "\\"
    if not os.path.exists(quality_path):
        os.makedirs(quality_path)
    #folder = "C:\\Users\\user\\Desktop\\ranTests\\pcap\\" + video_name + "\\"+ video_quality
    filename = quality_path + video_name + "_"  + funcInFile + t_time + ".pcap"
    tsharkOut  = open(filename, "wb")
    tsharkCall = ["C:\\Program Files\\Wireshark\\tshark.exe","-F", "pcap", "-f", "tcp port 443", "-i", "3", "-w", filename]#8-fixed line 3 wifi in my pc
    tsharkProc = subprocess.Popen(tsharkCall, stdout=tsharkOut, executable="C:\\Program Files\\Wireshark\\tshark.exe")
    chrome_options = webdriver.ChromeOptions()


    #this one worked
    chrome_options.binary_location ="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    #chrome_options.add_extension('adblockpluschrome-1.8.10.1352.crx') #note I used this one in the past. I had problems that the browser didn't close itself when I used adblock.
    driver = webdriver.Chrome(executable_path='C:\Python27\Scripts\chromedriver.exe',chrome_options=chrome_options)
    
    #driver = webdriver.Chrome(chrome_options=chrome_options)//ran
    #driver = webdriver.Chrome(executable_path = 'C:\Python27\Scripts\chromedriver.exe', chrome_options = 'C:\Users\user\Desktop\ranTests\adblockpluschrome-1.8.10.1352.crx')
    wait = WebDriverWait(driver, 100)
    driver.get(url)
    #Note: this option is disables since I am working with the auto mode. for fixed quality you will need to use this.!
    print('Note: for fixed qualities please enable this feature in the code')
    #time.sleep(1)
    #wait.until(EC.element_to_be_clickable((By.ID,'settings_button')))//worked
    #click = driver.find_element_by_id('settings_button').click()
    #driver.find_element_by_xpath("//*[@aria-label='Quality']").click()
    if video_quality == "360P":
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'360p')]")))
        time.sleep(0.3)
        driver.find_element_by_xpath("//*[contains(text(),'360p')]").click()
        time.sleep(15)
        clickOnAd(driver)
                  
    if video_quality == "480P":
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'480p')]")))
        time.sleep(0.3)
        driver.find_element_by_xpath("//*[contains(text(),'480p')]").click()
        time.sleep(15)
        clickOnAd(driver)
    if video_quality == "720P":
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'720p')]")))
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[contains(text(),'720p')]").click()
        time.sleep(15)
        clickOnAd(driver)
    if video_quality == "1080P":
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'1080p HD')]")))
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[contains(text(),'1080p')]").click()
        time.sleep(15)
        clickOnAd(driver)
    if video_quality == "Auto":
        time.sleep(10)
        clickOnAd(driver)
    
    time.sleep(duration_of_the_video)
    driver.close()
    tsharkProc.kill()


####################################################
#Start multiple downloads
####################################################
def harvest_video(amount,name,url,duration):
    for x in range(0, amount):
        print('Automatic quality')
        print('run number:', x)
        downloadVideo("Auto",name,url,duration)
        print('Note: for fixed quality please enable this lines in the code')
        #print('Capturing  360P')
        #downloadVideo("360P",name,url,duration)
        #print('Capturing  480P')
        #downloadVideo("480P",name,url,duration)
        #print('Capturing  720P')
        #downloadVideo("720P",name,url,duration)
        #print('Capturing  1080P')
        #downloadVideo("1080P",name,url,duration)

#List of URL's that I used.        
BBB_URL = "https://www.youtube.com/watch?v=Z5KLxerq05Y"
BBB_duration = 740
world_largest_zip_line_url = "https://www.youtube.com/watch?v=YcwrRA2BIlw"
world_largest_zip_line_duration = 200
sky_dive_dubay_url = "https://www.youtube.com/watch?v=zFg_mlBFV2c"
sky_dive_dubay_duration = 630
incredible_4K_url = "https://www.youtube.com/watch?v=6pxRHBw-k8M"
incredible_4K_duration = 220
the_advanture_of_life_url = "https://www.youtube.com/watch?v=wTcNtgA6gHs&list=PLSSPBo7OVSZvJtRrcF5CVSjRkmH9eNWA3"
the_advanture_of_life_duration = 260
honey_bees_url = "https://www.youtube.com/watch?v=Cx6eaVeYXOs"
honey_bees_duration = 240
Dreamlapse_UHD_url = "https://www.youtube.com/watch?v=qiBm4AfRcr0"
Dreamlapse_UHD_duration = 240
Homefront_TRAILER_url = "https://www.youtube.com/watch?v=JCPew975Qfc"
Homefront_TRAILER_duration = 170
WILDLIFE_IN_4K_url = "https://www.youtube.com/watch?v=xDMP3i36naA"
WILDLIFE_IN_4K_duration = 210
the_prodigy_nasty_url = "https://www.youtube.com/watch?v=xB_nKpEkILs&index=43&list=PL9tY0BWXOZFvWi6WNdcokF_YvXUxyESRW"
the_prodigy_nasty_duration = 230
diving_with_manta_ray_url = "https://www.youtube.com/watch?v=Mc3NTnoGzwE&index=15&list=PLSSPBo7OVSZvJtRrcF5CVSjRkmH9eNWA3"
diving_with_manta_ray_duration = 110
NIGHT_AT_THE_MUSEUM_3_url = "https://www.youtube.com/watch?v=Hr1fFMp0MqU"
NIGHT_AT_THE_MUSEUM_3_duration = 150
iron_man_3_url = "https://www.youtube.com/watch?v=uBI4nPnQ8jI"
iron_man_3_duration = 130
Oblivion_Trailer_url = "https://www.youtube.com/watch?v=ZokHZXb8QDs"
Oblivion_Trailer_duration= 160
x_men_days_of_future_past_url = "https://www.youtube.com/watch?v=IbiX07HHW3I"
x_men_days_of_future_past_duration = 145
Drone_Footage_Of_Frozen_Niagara_Falls_url = "https://www.youtube.com/watch?v=7PNTuIECZCE"
Drone_Footage_Of_Frozen_Niagara_Falls_duration = 120

the_movie_url = "https://www.youtube.com/watch?v=V5hOm8_3mJA"
the_movie_duration =  152
Hitman_url = "https://www.youtube.com/watch?v=alQlJDRnQkE"
Hitman_duration =   150
mr_Holmes_url = "https://www.youtube.com/watch?v=FJwgItmobFE"
mr_holmes_duration =  80
San_andreass_url = "https://www.youtube.com/watch?v=UN1G4BSyIos"
San_andreass_duration = 142
mad_max_url = "https://www.youtube.com/watch?v=b_4nzm9ICuo"
mad_max_duration =  142
FiveFlights_url =  "https://www.youtube.com/watch?v=PreX3h3QYHY"
FiveFlights_duration =  140
Aloha_url = "https://www.youtube.com/watch?v=O3mf_ewjc7s"
Aloha_duration =  150
Pitch_perfect2_url = "https://www.youtube.com/watch?v=TY-u5P9pRwA"
Pitch_perfect2_duration = 150
Fifty_shades_ofGrey_url = "https://www.youtube.com/watch?v=CQERFnGvi_A"
Fifty_shades_ofGrey_duration = 146
Friends_url = "https://www.youtube.com/watch?v=V5hOm8_3mJA"
Friends_duration = 152
Furious_7_url = "https://www.youtube.com/watch?v=k94wBXeauao"
Furious_7_duration = 180 
Terrence_Howard_url = "https://www.youtube.com/watch?v=NGheJlDfb08"
Terrence_Howard_duration =  182
THE_LOFT_url = "https://www.youtube.com/watch?v=08JRDC4-kug"
THE_LOFT_duration = 140
Last_Knights_url = "https://www.youtube.com/watch?v=e44QilQbvB0"
Last_Knights_duration  =150
The_Interview_url = "https://www.youtube.com/watch?v=KpyVENBPj5c"
The_Interview_duration = 160
Sex_Tape_url = "https://www.youtube.com/watch?v=JF6IXw86iSQ"
Sex_Tape_duration = 180
Ten_Rules_url = "https://www.youtube.com/watch?v=7McSiK7IrDw"
Ten_Rules_duration =142
Dom_Hemingway_url= "https://www.youtube.com/watch?v=u1izaIH269E"
Dom_Hemingway_url = 135
Exodus_url = "https://www.youtube.com/watch?v=t-8YsulfxVI"
Exodus_duration = 185
Filth_url = "https://www.youtube.com/watch?v=QH0F0GKkUFE"
Filth_duration = 134
cliff_jumps_url = "https://www.youtube.com/watch?v=Bn09g1bwgDc"
cliff_jumps_duration = 334
Fantastic_Four_url = "https://www.youtube.com/watch?v=cxIldZcUuCk"
Fantastic_Four_duration = 105 
Home_Sweet_Hell_url = "https://www.youtube.com/watch?v=UbuvFMvytu4"
Home_Sweet_Hell_duration = 134
Cinderella_url  = "https://www.youtube.com/watch?v=Pqk436s9cg4"
Cinderella_duration =  130
TenYears_url = "https://www.youtube.com/watch?v=X9Ku-HJc6yE"
TenYears_duration = 151
Albatross_url =  "https://www.youtube.com/watch?v=KQnXnbQCJDo"
Albatross_duration = 111
American_Hustle_url = "https://www.youtube.com/watch?v=BeyUrnU_lZ4"
American_Hustle_duration = 111
Avengers_url = "https://www.youtube.com/watch?v=JAUoeqvedMo"
Avengers_duration = 138
Chinese_url = "https://www.youtube.com/watch?v=LbiIu_EzuWk"
Chinese_duration = 240
CURSE_OF_THE_DRAGON_url = "https://www.youtube.com/watch?v=bMW-ja_Rkdw"
CURSE_OF_THE_DRAGON_duration = 150
Dark_Tide_url = "https://www.youtube.com/watch?v=0ipC-bjnH4A"
Dark_Tide_duration = 110
Das_Keyboard_url = "https://www.youtube.com/watch?v=CjIk1JMjMqU"
Das_Keyboard_duration =  492
Disconnect_url = "https://www.youtube.com/watch?v=gkoM0IbbLiY"
Disconnect_duration =152
Diversity_and_Inclusion_url =  "https://www.youtube.com/watch?v=PnDgZuGIhHs"
Diversity_and_Inclusion_duration =  200
Divorce_url =  "https://www.youtube.com/watch?v=vN--jzplDPE"
Divorce_duration = 131
Fast_and_Furious_six_url =  "https://www.youtube.com/watch?v=dKi5XoeTN0k"
Fast_and_Furious_six_duration = 202
First_human_url = "https://www.youtube.com/watch?v=0E77j1imdhQ"
First_human_duration = 143
Flyboard_url = "https://www.youtube.com/watch?v=m4Bm3cs9TFo"
Flyboard_duration = 200
Game_of_Thrones_url  = "https://www.youtube.com/watch?v=xZY43QSx3Fk"
Game_of_Thrones_duration =  110
Maleficent_url = "https://www.youtube.com/watch?v=w-XO4XiRop0"
Maleficent_duration = 130
Omer_adam_url = "https://www.youtube.com/watch?v=TmG_OVVYNug"
Omer_adam_duration = 290
Pacific_Rim_url = "https://www.youtube.com/watch?v=5guMumPFBag"
Pacific_Rim_duration = 152
Passion_url = "https://www.youtube.com/watch?v=-YhHeO1BuAI"
Passion_duration =  110
Red_Dawn_url = "https://www.youtube.com/watch?v=nGoe7BdGdlg"
Red_Dawn_duration = 155
Soldiers_of_Fortune_url = "https://www.youtube.com/watch?v=6sVP0axlhc4"
Soldiers_of_Fortune_duration = 135
Tamer_Hosny_url = "https://www.youtube.com/watch?v=U_dGwmcwHxU"
Tamer_Hosny_duration = 600
Taylor_Swift_url = "https://www.youtube.com/watch?v=QcIy9NiNbmo"
Taylor_Swift_duration = 245
The_English_Teacher_url = "https://www.youtube.com/watch?v=7LLWTXoHHAY" 
The_English_Teacher_duration = 140
The_Man_With_The_Iron_Fists_url= "https://www.youtube.com/watch?v=6FyGHAUpSIQ"
The_Man_With_The_Iron_Fists_duration = 140
Welcome_to_Yesterday_url = "https://www.youtube.com/watch?v=KnGcWVoxftI"
Welcome_to_Yesterday_duration = 160
goproSyberTiger_url ="https://www.youtube.com/watch?v=AZ1jTsQS4EY"
goproSyberTiger = 136


#Youtube traffic title classifier video dataset list.
#harvest_video(100,"Friends",Friends_url,Friends_duration)
#harvest_video(100,"Furious_7",Furious_7_url,Furious_7_duration)
#harvest_video(100,"Terrence_Howard",Terrence_Howard_url,Terrence_Howard_duration)
#harvest_video(100,"THE_LOFT",THE_LOFT_url,THE_LOFT_duration)
#harvest_video(100,"Last_Knights",Last_Knights_url,Last_Knights_duration)
#harvest_video(100,"The_Interview",The_Interview_url,The_Interview_duration)
#harvest_video(100,"world_largest_zip_line",world_largest_zip_line_url,world_largest_zip_line_duration)
#harvest_video(100,"Sex_Tape",Sex_Tape_url,Sex_Tape_duration)
#harvest_video(100,"Ten_Rules",Ten_Rules_url,Ten_Rules_duration)
#harvest_video(100,"Exodus",Exodus_url,Exodus_duration)
#harvest_video(100)
#harvest_video(100,"Home_Sweet_Hell",Home_Sweet_Hell_url,Home_Sweet_Hell_duration)
#harvest_video(100,"Cinderella",Cinderella_url,Cinderella_duration)
#harvest_video(100,"TenYears",TenYears_url,TenYears_duration)
#harvest_video(100,"Albatross",Albatross_url,Albatross_duration)
#harvest_video(100,"American_Hustle",American_Hustle_url,American_Hustle_duration)
#harvest_video(100,"Avengers",Avengers_url,Avengers_duration)
#harvest_video(100,"Chinese",Chinese_url,Chinese_duration)
#harvest_video(100,"CURSE_OF_THE_DRAGON",CURSE_OF_THE_DRAGON_url,CURSE_OF_THE_DRAGON_duration)
#harvest_video(100,"Dark_Tide",Dark_Tide_url,Dark_Tide_duration)
#harvest_video(100,"Flyboard",Flyboard_url,Flyboard_duration)
#harvest_video(100,"cliff_jumps",cliff_jumps_url,cliff_jumps_duration)
#harvest_video(100,"Taylor_Swift",Taylor_Swift_url,Taylor_Swift_duration)
#harvest_video(100,"diving_with_manta_ray",diving_with_manta_ray_url,diving_with_manta_ray_duration)
#harvest_video(100,"Das_Keyboard",Das_Keyboard_url,Das_Keyboard_duration)
#harvest_video(100,"Disconnect",Disconnect_url,Disconnect_duration)
#harvest_video(100,"Diversity_and_Inclusion",Diversity_and_Inclusion_url,Diversity_and_Inclusion_duration)
#harvest_video(100,"Divorce",Divorce_url,Divorce_duration)
#harvest_video(100,"Fast_and_Furious_six",Fast_and_Furious_six_url,Fast_and_Furious_six_duration)
#harvest_video(100,"First_human",First_human_url,First_human_duration)
###################################################################################33
#test data single download of titles which are not found  in DB
#harvest_video(1,"SyberTiger",goproSyberTiger_url,goproSyberTiger)
#harvest_video(1,"Game_of_Thrones",Game_of_Thrones_url,Game_of_Thrones_duration)
#harvest_video(1,"Maleficent",Maleficent_url,Maleficent_duration)
#harvest_video(1,"Omer_adam",Omer_adam_url,Omer_adam_duration)
#harvest_video(1,"Pacific_Rim",Pacific_Rim_url,Pacific_Rim_duration)
#harvest_video(1,"Passion",Passion_url,Passion_duration)
#harvest_video(1,"Red_Dawn",Red_Dawn_url,Red_Dawn_duration)
#harvest_video(1,"Tamer_Hosny",Tamer_Hosny_url,Tamer_Hosny_duration)
#harvest_video(1,"The_English_Teacher",The_English_Teacher_url,The_English_Teacher_duration)
#harvest_video(1,"The_Man_With_The_Iron_Fists",The_Man_With_The_Iron_Fists_url,The_Man_With_The_Iron_Fists_duration)
#harvest_video(1,"Welcome_to_Yesterday",Welcome_to_Yesterday_url,Welcome_to_Yesterday_duration)
#harvest_video(1,"The_movie",the_movie_url,the_movie_duration)
#harvest_video(1,"Hitman",Hitman_url,Hitman_duration)
#harvest_video(1,"San_andreass",San_andreass_url,San_andreass_duration)
#harvest_video(1,"Mr_Holmes",mr_Holmes_url,mr_holmes_duration)
#harvest_video(1,"Mad_max",mad_max_url,mad_max_duration)
#harvest_video(1,"FiveFlights",FiveFlights_url,FiveFlights_duration)
#harvest_video(1,"Pitch_perfect2",Pitch_perfect2_url,Pitch_perfect2_duration)
#harvest_video(1,"Fifty_shades_ofGrey",Fifty_shades_ofGrey_url,Fifty_shades_ofGrey_duration)

#harvest_video(1,"Drone_Footage_Of_Frozen_Niagara_Falls",Drone_Footage_Of_Frozen_Niagara_Falls_url,Drone_Footage_Of_Frozen_Niagara_Falls_duration)
#harvest_video(1,"x_men_days_of_future_past",x_men_days_of_future_past_url,x_men_days_of_future_past_duration)
#harvest_video(1,"Oblivion_Trailer",Oblivion_Trailer_url,Oblivion_Trailer_duration)
#harvest_video(1,"iron_man_3",iron_man_3_url,iron_man_3_duration)
#harvest_video(1,"NIGHT_AT_THE_MUSEUM_3",NIGHT_AT_THE_MUSEUM_3_url,NIGHT_AT_THE_MUSEUM_3_duration)
#harvest_video(1,"the_prodigy_nasty",the_prodigy_nasty_url,the_prodigy_nasty_duration)
#harvest_video(1,"WILDLIFE_IN_4K",WILDLIFE_IN_4K_url,WILDLIFE_IN_4K_duration)
#harvest_video(1,"Homefront_TRAILER",Homefront_TRAILER_url,Homefront_TRAILER_duration)
#harvest_video(1,"Dreamlapse_UHD",Dreamlapse_UHD_url,Dreamlapse_UHD_duration)
#harvest_video(1,"honey_bees",honey_bees_url,honey_bees_duration)
#harvest_video(1,"the_advanture_of_life",the_advanture_of_life_url,the_advanture_of_life_duration)
#harvest_video(1,"incredible_4K",incredible_4K_url,incredible_4K_duration)

#sample usage of downloading a fixed YouTube Quality
#for x in range(0, 40):
    #print('run number:', x)
    #print('Capturing  360P')
    #downloadVideo("360P","sky_dive_dubay",sky_dive_dubay_url,sky_dive_dubay_duration)
    #print('Capturing  480P')
    #downloadVideo("480P","sky_dive_dubay",sky_dive_dubay_url,sky_dive_dubay_duration)
    #print('Capturing  720P')
    #downloadVideo("720P","sky_dive_dubay",sky_dive_dubay_url,sky_dive_dubay_duration)
