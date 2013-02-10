DIFF = git --no-pager diff --color-words --no-index

install:
	./setup.py install

test: install
	cat test/doc.json | json pluck '[2].id' > test/.scratch
	$(DIFF) test/.scratch test/expected_pluck
	cat test/doc.json | json render test/urls.mustache > test/.scratch
	$(DIFF) test/.scratch test/expected_urls
	json render test/env.mustache > test/.scratch
	$(DIFF) test/.scratch test/expected_env
	cat test/doc.json | json slice login id > test/.scratch
	$(DIFF) test/.scratch test/expected_slice
	cat test/doc.json | json indent > test/.scratch
	$(DIFF) test/.scratch test/expected_indent_1
	cat test/doc.json | json indent 4 > test/.scratch
	$(DIFF) test/.scratch test/expected_indent_4
	cat test/doc.json | json colorize > test/.scratch
	$(DIFF) test/.scratch test/expected_colorized_1
	cat test/doc.json | json colorize 4 > test/.scratch
	$(DIFF) test/.scratch test/expected_colorized_4
