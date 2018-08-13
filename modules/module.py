import json ;


#TODO CLOCK SENSITIVE

class module(object):

    bot_cmd = "" ;

    def login_check_dec(function):
        def wrapper(*args, **kargs):
            if args[2] != args[0].caller.login:
                return function(*args, **kargs) ;
            else:
                return None ;
        return wrapper ;

    def clock_dec(function):
        '''
        Deprecated
        :return:
        '''
        def wrapper(*args, **kargs):
            if args[0].clock_sensitive:
                return function(*args, **kargs)
            else:
                return None
        return wrapper ;


    def module_on_dec(function):
        def wrapper(*args, **kargs):
            if args[0].is_module_on:
                return function(*args, **kargs)
            else:
                return None
        return wrapper ;

    def check_command_dec(function):
        def wrapper(*args, **kargs):
            raw_cmd = args[1].split() ;
            s = args[0] ;
            if len(raw_cmd) >= 2 and raw_cmd[0] == module.bot_cmd and raw_cmd[1] in s.keywords:
                return function(*args, **kargs) ;
            else:
                return None ;
        return wrapper ;

    def check_command(self, cmd):
        raw_cmd = cmd.split() ;
        return len(raw_cmd) >= 2 and raw_cmd[0] == module.bot_cmd and raw_cmd[1] in self.keywords ;


    def __init__(self, keyword = None):
        self.timer = 0 ;
        self.clock_sensitive = True ;
        self.is_module_on = True ;
        self.caller = None ;
        self.help = "" ;
        self.whatis = "" ;
        if keyword:
            self.keywords = [keyword] ;
        else:
            self.keywords = ["Default_Module_Name"] ;
        self.__version__ = "0.0.0"
        if not(module.bot_cmd):
            try:
                with open("./config.json", "r") as f:
                    config = json.loads(f.read()) ;
                module.bot_cmd = config["bot_cmd"] ;
            except IOError as e:
                print("Could not load config.json "+str(e)) ;
                module.bot_cmd = "tbot";

    @module_on_dec
    def run(self, cmd, sender = None, room = None):
        pass

    @module_on_dec
    def run_on_clock(self):
        pass

    def exit(self):
        pass

    @module_on_dec
    def clock_update(self):
        self.timer += 1 ;

    def reset_clock(self):
        self.timer = 0 ;

    def set_clock_sensitivity_on(self):
        self.clock_sensitive = True ;

    def set_clock_sensitivity_off(self):
        self.clock_sensitive = False ;

    def get_timer(self):
        return self.timer ;

    def is_module_activated(self):
        return self.is_module_on ;

    def set_module_on(self):
        self.is_module_on = True ;

    def set_module_off(self):
        self.is_module_on = False ;

    def admin(self, caller):
        self.caller = caller ;

        


if __name__ == "__main__":
    mod = module() ;
    mod.clock_update() ;
    print(mod.timer)
    mod.clock_sensitive_off() ;
    print(mod.timer)