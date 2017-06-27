# utils

## setup-pip.sh

_First of all this is targeted at Ubuntu and specifically the `apt` package manager. If you're using something else, like a Mac, you should look at [the code](setup-pip.sh) and adjust your steps accordingly. If you want to submit a patch to make the tool magically work on multiple operating systems (or at least be documented for multiple operating systems) that would also be cool._

This is a simple shell script to automate _most_ of the tasks involved in making sure that everything you need to use the py-mapzen-whosonfirst libraries with `pip` rather than `easy_install` is set up.

The first step is _not_ automated however. That involves purging any existing `py-mapzen-whosonfirst-* libraries from your system. Because this involves deleting things you need to take responsibility for doing it yourself. This is what I do:

```
python
>>> import sys
>>> print "\n".join(sys.path)
 
/usr/local/lib/python2.7/dist-packages/mapzen.whosonfirst-0.37-py2.7.egg
/usr/local/lib/python2.7/dist-packages/mapzen.whosonfirst.search-0.13_-py2.7.egg
and so on...
```

Which means everything is stored in `/usr/local/lib/python2.7/dist-packages` on my machine. So then I do this to remove all the old code:

```
sudo rm -rf /usr/local/lib/python2.7/dist-packages/mapzen.*
```

Please don't just blindly copy and paste what's happening above. Think about it in the context of _your machine_. If you're not sure, _ask someone to help you_ before proceeding.

Once that is done you should be able to execute the following commands (from inside the root of the `py-mapzen-whosonfirst` repo) to finish getting set up:

```
./utils/setup-pip.sh
make upgrade
```