# -*- coding: utf-8 -*-

'''
SNS type: status, user, comment
'''
import utils
import errors
from snsconf import SNSConf

class StatusID(object):
    """
    All information to locate one status is here. 

    It shuold be complete so that:

       * one can invoke reply() function of plugin on this object. 
       * Or one can invoke reply() function of container on this object. 

    In order to reply one status, here's the information 
    required by each platforms:

       * Renren: the status_id and source_user_id
       * Sina:
       * QQ:

    """
    def __init__(self, platform = None, status_id = None, source_user_id = None):
        super(StatusID, self).__init__()

        self.platform = platform
        self.status_id = status_id
        self.source_user_id = source_user_id

    def __str__(self):
        """docstring for __str__"""
        return "(p:%s|sid:%s|uid:%s)" % \
                (self.platform, self.status_id, self.source_user_id)
        

class Status(object):
    def __init__(self, dct=None):
        self.created_at = ""
        self.id = 0
        self.text = ""
        self.reposts_count = 0
        self.comments_count = 0
        self.user = None
        self.username = ""
        self.usernick = ""

        self.ID = StatusID()
        
        try:
            self.parse(dct)
        except AttributeError:
            raise errors.snsTypeParseError
            
    def parse(self, dct):
        pass

    def show(self):
        utils.console_output(unicode(self))
    
    #def __str__(self):
    #    return "[%s] at %s \n  %s" % \
    #            (self.username, self.created_at, self.text)
    def __str__(self):
        #raise errors.SNSEncodingError()
        #return unicode(self).encode('utf-8')
        return unicode(self).encode(SNSConf.SNSAPI_CONSOLE_STDOUT_ENCODING)

    def __unicode__(self):
        return "[%s] at %s \n  %s" % \
                (self.username, self.created_at, self.text)

class StatusList(list):
    """
    A list of Status object 
    """
    def __init__(self):
        super(StatusList, self).__init__()

    def __str__(self):
        tmp = ""
        for s in self:
            tmp = tmp + str(s) + "\n"
        return tmp

    def __unicode__(self):
        tmp = ""
        for s in self:
            tmp = tmp + unicode(s) + "\n"
        return tmp
        
    
class User(object):
    def __init__(self, jobj=None):
        self.id = 0
        
#TODO:
#    This class is not used anywhere in the project. 
#    Retire it in the next upgrades?
class Error(dict):
    def show(self):
        #print self
        utils.console_output(self)

class AuthenticationInfo(utils.JsonObject):
    #default auth configurations
    def __init__(self, auth_info = None):
        if auth_info :
            self.callback_url = auth_info['callback_url']
            self.cmd_fetch_code = auth_info['cmd_fetch_code']
            self.cmd_request_url = auth_info['cmd_request_url'] 
            self.save_token_file = auth_info['save_token_file'] 
        else :
            self.callback_url = None
            self.cmd_fetch_code = "(built-in)"
            self.cmd_request_url = "(built-in)"
            self.save_token_file = "(built-in)"

if __name__ == "__main__":
    s = Status("fe")
    s.show()