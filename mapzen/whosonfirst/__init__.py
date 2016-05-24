# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import logging
import pkg_resources
import requests

def installed_version():
   pymz = pkg_resources.get_distribution("mapzen.whosonfirst").version
   pymz = pymz.rstrip("-")
   return float(pymz)

def is_current(**kwargs):

   liberal = kwargs.get('liberal', False)
   
   pymz = installed_version()
   current = 0.0
   
   try:
      logging.debug("I am going to try and see whether you are using the most recent version of py-mapzen-whosonfirst...")
      
      rsp = requests.get("https://raw.githubusercontent.com/whosonfirst/py-mapzen-whosonfirst/master/VERSION")
      current = rsp.content
      current = float(current.strip())

   except Exception, e:
      logging.warning("Failed to determine ACTUAL current version of py-mapzen-whosonfirst, because %s" % e)

      if not strict:
         logging.info("strict mode is disabled so setting current to %s for now but don't be surprised if HILARITY ensues...")
         current = pymz
         
   if pymz < current:
      logging.warning("You are running version %s of py-mapzen-whosonfirst but the current version is %s - you should update because HILARITY may ensue if you don't" % (pymz, current))
      return False
      
   if pymz > current:
      logging.warning("You are running a newer version (%s) of py-mapzen-whosonfirst - the current version is %s" % (pymz, current))

      if liberal:
         return True

      logging.warning("You are not being liberal about things so version mismatch triggers are being invoked")
      return False

   logging.debug("py-mapzen-whosonfirst are current")
   return True

def ensure_current(**kwargs):
    
    if not is_current(**kwargs):
       logging.error("mapzen.whosonfirst Python libraries are not up to date!")
       raise Exception, "mapzen.whosonfirst Python libraries are not up to date!"
