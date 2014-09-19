TELL ME THE TIME BOT
____________________________________________________________________________________

TABLE OF CONTENTS 
___________________________________________________________________________________
0. PREFACE (WHY I CREATED THIS)
1. HOW IT WORKS 
2. REQUIREMENTS
3. DEPLOYING THIS SPECIFIC TWITTER BOT FOR YOURSELF
4. EXPLAINING THE SOURCE CODE


0.PREFACE (WHY I CREATED THIS)
___________________________________________________________________________________

This is one of my first Python projects ever, and you guessed it!....it's useless!

I just wanted to program something that uses 
1.BeautifulSoup4
2.Requests
3.Social Media API (Twython, a twitter API that was compatible with python3)

So I came up with the Tell_me_the_time_bot.
This bot is a twitter bot that ,when asked for the time of a certain location on twitter, replies to your 
tweet with the exact time of the location.
The name tell_me_the_time_bot was too long for twitter so I condensed it down to
@whatsthetimebot.



1.HOW IT WORKS / FINDING OUT THE TIME OF ANY LOCATION BY TWEETING 
_____________________________________________________________________________________

To find out the time of any location on earth ,make a tweet mentioning @whatsthetimebot with any location on earth.
An example of a few tweets that will work are:

1. "@whatsthetimebot what time is it in Australia?"
2. "@whatsthetimebot Australia"
3. "@whatsthetimebot time in Australia"
4. "@whatsthetimebot Australia time"

Many common typos are also accepted, for example tweeting "@whatsthetimebot Time ni australa" is also accepted.



2.REQUIREMENTS
_____________________________________________________________________________________

To use the source code you must have:
 1.Python3.x 
 2.Latest version of Twython (The twitter API for python) that supports Python3
 3.BeautifulSoup4
 4.Requests 2.4.1 and above.
 5. Not a real requirement but Pycharm community edition is a great IDE!


3.DEPLOYING THIS SPECIFIC TWITTER BOT FOR YOURSELF
_______________________________________________________________________________________
Make sure you meet all requirements in 2. before starting this.
0. Register for a twitter app on dev.twitter.com
   remember to go into your app settings and change your read and write settings.

1.First of all make sure your TWITTER APP is authorized.
In this case we are using Twython.
Make sure you are verified to use OAUTH1 for Writing and OAUTH2 for reading.
The twythondocs can be found here 

2.Make a separate file called keys.py in the same foler and store your 
 APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET variables. 
 
 keys.py should look something like this:
 
 keys.py
 ----------
 APP_KEY = 'rwYJa5yvkPvLcfEwerwer76v'
APP_SECRET = 'tDmmgdbWhZHtzBKbwerewrwerwfKN'
OAUTH_TOKEN = '2718807werwerwerQLmVF3Gzs'
OAUTH_TOKEN_SECRET = '1HiTaubCcn36SlaSwerewerwerewqBCaPm95'
#end of keys.py
-------------

Those jumbled letters are your tokens and keys provided 

3. Make sure you replace @whatsthetimebot to your own username.
I'm sorry I didn't program it so that it would take your username automatically depending
on your twitter app. It would've honestly taken 3 minutes, but I'm done with this crappy
twitterbot and I'm ready to sleep!

4.That is all, after you replaced it, run the code! And there ya have it.
Also run the code in Pycharm. I use that for an IDE and it's amazing.

--------          -----------   -----     -----     ---   -- -  ------  --

4.EXPLAINING THE SOURCE CODE
_________________________________________________________________________________

1.A stream object is a created from the MyStreamer class.
This class inherits Twython's TwythonStreamer ( I don't know what goes on behind Twython Streamer 
you can check out the source code on Twython's github)

2.After a stream object is created you can now start listening to streaming tweets as they come in

stream.statuses.filter(track = '@whatsthetimebot')

again, read the twython API docs if you don't know where .statuses.filter came from.

This basically tracks all the mentions of @whatsthetimebot as it comes in.

3.If there is a tweet mentioning @whatsthetimebot it takes the text from that tweet and stores it
in a variable called tweet. 

4.Using this tweet, the script searches bing for this tweet with "what time is it in" attached before the tweet.

5.We generate the URL from the text stored in tweet and requests will now request that URL

6. After requesting that URL beautifulsoup spits out the beautiful html of that page, and parses out where
the time is displayed
If there isn't anything in the html div or the div isn't there, this means the user has inputted something wrong
and isn't using the program right.

7.The text inside the div is stored in the variable tweet (obviously replacing what was previously stored in
this variable)
so now this div stores the time.

8. The last step is to tweet that time to the user.
We now concatenated the @(user we would like to reply to) + tweet(the variable containing the time)

9.Finally, we use the twython api to reply to the user with our tweet variable. Remember to reply with the parameter of the tweet id!

10. That is all, thanks for taking some time to look at this! 

                        loveyouIl                                         
                                  oveyouIloveyouIlo                                     
                              veyouIloveyouIloveyouIlo                                  
                      veyouIloveyouIl           oveyouIl                                
                   oveyouIloveyo                  uIlovey                               
                 ouIloveyouIlove                   youIlo                               
                 veyouIloveyouIlo                   veyou                               
                 IloveyouIlo veyouI    loveyouIlov  eyouI                               
                 loveyouIloveyouIlov eyouIloveyouIlo veyo                               
                 uIloveyouIloveyou  IloveyouIloveyouIlove                               
                youIl  oveyouIlove  youIloveyouIloveyouIl                               
               oveyouIloveyouIlovey ouIloveyouI loveyouIl                               
              oveyouIloveyouIlove   youIloveyouIloveyouIl                               
             oveyouIloveyouIloveyouIloveyouIlovey  ouIlo                                
            veyou          IloveyouIloveyouIl     oveyou                                
           Ilove                      youIlov     eyouIl                                
          oveyou                                 Ilovey                                 
         ouIlov                                 eyouIl                                  
        oveyou                                  Ilovey                                  
        ouIlo                      veyo        uIlove                                   
        youI                      lovey ouI   loveyo                                    
        uIlo                      veyouIlove  youIl                         oveyouIlo   
       veyou                      IloveyouI  lovey                        ouIloveyouIl  
       oveyo                     uIloveyouI lovey                       ouIlov    eyou  
       Ilove                     youIlovey  ouIlo                     veyouIl    oveyo  
       uIlov                    eyouIlove  youIlo                   veyouIl     oveyo   
       uIlov                    eyouIlov   eyouIloveyouIloveyou   Iloveyo     uIlov     
        eyou                   Iloveyou    IloveyouIloveyouIloveyouIlov      eyouI      
        love                   youIlov     eyouI   lovey   ouIloveyou      Ilovey       
        ouIl                  oveyouIl      ove   youIloveyouIlovey      ouIlov         
        eyouI               lovey ouIlo         veyouIloveyouIlove     youIlov          
         eyou             Ilove  youIlov         eyouIloveyouIloveyo   uIloveyo         
         uIlov            eyouIloveyouIl                     oveyouIl    oveyouIlo      
          veyou            IloveyouIlov              eyou       Ilovey  ouIl oveyo      
          uIlove              youI                   love        youIlo  veyouIlo       
           veyouI                                lov              eyouI    love         
            youIlove                            youI              lovey     ouIl        
               oveyouI                          love              youIloveyouIlo        
     vey        ouIloveyou                       Ilov           eyouIloveyouIlo         
    veyouIl    oveyouIloveyouIlo                  vey         ouIlove    y              
    ouIloveyouIlov eyouIloveyouIloveyouI           love    youIlov                      
    eyou IloveyouIlovey    ouIloveyouIlove youIloveyouIloveyouIl                        
     ovey  ouIloveyou         IloveyouIlo veyouIloveyouIlovey                           
      ouIl   oveyou         IloveyouIlov eyouI loveyouIlov                              
       eyouIlovey           ouIloveyouI  love                                           
        youIlov              eyouIlov   eyou                                            
          Ilo                veyouI    love                                             
                              youIlo  veyo                                              
                               uIloveyouI                                               
                                 loveyou                                                
                                   Ilo                                                  
                                         
 
 




