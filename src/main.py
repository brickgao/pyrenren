from sgmllib import SGMLParser
import sys,urllib2,urllib,cookielib
import getpass

class loginrenren(SGMLParser):
    
    def __init__(self, mail, password):
        SGMLParser.__init__(self)
        self.h3=False
        self.h3_is_ready=False
        self.div=False
        self.h3_and_div=False
        self.a=False
        self.depth=0
        self.names=""
        self.dic={} 
        
        try:
            print('Try to login renren.com')
            
            cookie = cookielib.CookieJar()
            cookies = urllib2.HTTPCookieProcessor(cookie)
            opener = urllib2.build_opener(cookies)
            urllib2.install_opener(opener)
    
            parms = {
                'email': mail,
                'password': password,
                'domain': 'renren.com',
            }
            
            loginURL = 'http://renren.com/PLogin.do'
            login = urllib2.urlopen(loginURL, urllib.urlencode(parms))

            self.file = urllib2.urlopen('http://renren.com/home').read()
            idPos = self.file.index("'id':'")
            self.id = self.file[idPos+6:idPos+15]
            tokPos = self.file.index("get_check:'")
            self.tok = self.file[tokPos+11:tokPos+21]
            rtkPos = self.file.index("get_check_x:'")
            self.rtk = self.file[rtkPos+13:rtkPos+21]
            
            print('login success')

        except Exception, e:
            print(e)
    
    def post(self, content):
        url1 = 'http://shell.renren.com/' + self.id + '/status'
        postdata = {
                  'content': content,  
                  'hostid': self.id,  
                  'requestToken': self.tok,  
                  '_rtk': self.rtk,  
                  'channel': 'renren',
        }
        req = urllib2.Request(url1, urllib.urlencode(postdata))
        self.file1 = urllib2.urlopen(req).read()
        print('Push Content Success')
    
    
if __name__ == '__main__':
    Email = raw_input('Input your Email:')
    Password = getpass.getpass('Input your password:')
    newlogin = loginrenren(Email, Password)
    Content = raw_input('Input Content:')
    newlogin.post(Content)
