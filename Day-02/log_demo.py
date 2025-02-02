import logging

logging.basicConfig(level=logging.INFO,filename='mylog.log',filemode='a',
                    format="Python-app: %(process)d - %(name)s - %(levelname)s - %(message)s -%(asctime)s"
                    )

logging.debug("Debug Error occured in code")
logging.info("info logss")
logging.warning("Wanings")
logging.error("errors are there")
logging.critical("Something wrost, critical")

username='Pramod'
logging.info(f"{username} has logged-in")

try:
    a=10
    b=0     
    c=a/b
except Exception as ex:
    logging.error("exception occured", exc_info=True)