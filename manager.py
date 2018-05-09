import logging
from tornado.options import define, options

def start():
    from app import start_server
    # print(INFO + '%s : Starting application ...' % current_time()
    start_server()

define("debug",
       default=True,
       group="application",
       help="start the application in debugging mode",
       type=bool)

define("runserver",
       default=True,
       help="run the server",
       type=bool)

def main():
    options.parse_command_line()
    if options.runserver:
        start()

if __name__ == "__main__":
    main()