snip.py
=======

snip.py was created out of the need to quickly prototype exploits during so called CTF contests.
You can store your code snippets in a directory somewhere on your machine, point SNIP\_PATH to
it and you are done. Now you can use snip.py's selector syntax to retrieve the snippets quick
and easy.

snip.py runs with Python 2.7 or 3 on UNIX systems. It is released under a MIT license.

Installation
------------

You may want to symlink snip.py into your /usr/bin/ after cloning it:

	# ln -s /path/to/snip.py /usr/bin/snip.py

Usage
-----

snip.py understands a selector syntax which looks like UNIX directories. It will first build a
list of all snippets SNIP\_PATH is pointing to and search for the snippet there. Your SNIP\_PATH
may look like this:

	SNIP_PATH = ('/home/user/snippets', '/home/user/github/snip.py/')

This example contains two paths in SNIP\_PATH. All snippets of /home/user/snippets will be
priorized. Please use absolute paths for your SNIP\_PATH. (Oh and by the way: The SNIP\_PATH is
stored in ~/.config/snip.py/settings.py.)

Now let's check which snippets are avialable to us:

	$ snip.py /
	DIR more_snippets
	snippet_1.py

If we want to copy the file snippet\_1.py into another file called quickstart.py we would execute
this command:

	$ snip.py /snippet_1.py quickstart.py

quickstart.py will be written into your current directory. It is possible to print out the content
of the file on the terminal, too:

	$ snip.py /snippet_1.py
	...

Maybe we don't want to copy snippet\_1.py but look inside the folder more\_snippets:

	$ snip.py /more_snippets
	a.py
	b.py
	c.py

We could copy files from there with following command:

	$ snip.py /more_snippets/a.py /home/user/newfile.py

There are many possibilities and tricks (you don't have to put the first / if you don't want to).

Have fun with it =)
