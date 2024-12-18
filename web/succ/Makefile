dist:
	rm -rf dist
	mkdir dist

	# Copy all project files with redacted flag
	cp -r docker-compose.yml triage-server web-server ./dist
	sed -i 's/h0h0h0{ftp_is_f4nt4st1c_0f827e4c}/h0h0h0{redacted_flag}/g' dist/triage-server/flag

	# Simulate git history
	cd dist && \
	git init && \
	git add . && git commit -m "Initial commit" && \
	echo "secret.key" > .gitignore && \
	git rm -r --cached . && git add . && git commit -m "Updated .gitignore" && \
	rm web-server/secret.key

	# Tar it and ship it	
	cd dist && tar -czf ../succ.tar.gz .git .gitignore *
	rm -rf dist