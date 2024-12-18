#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	if (argc == 1) {
		execl("/usr/bin/strace", "/usr/bin/strace", realpath(argv[0], NULL), "x", NULL);
	}

	char filename[64];
	fgets(filename, 64, stdin);
	filename[strlen(filename) - 1] = '\x00';

	FILE *f;
	f = fopen(filename, "r+");
	if (!f) {
		perror("open");
		exit(1);
	}

	char buf[64];
	long offset = 0;
	fgets(buf, 64, stdin);
	offset = strtol(buf, NULL, 10);

	if (fseek(f, offset, 0) == -1) {
		perror("seek");
		exit(1);
	}

	long length = 0;
	fgets(buf, 64, stdin);
	length = strtol(buf, NULL, 10);

	if (length > 1024 || length < 1) {
		fprintf(stderr, "0 < length < 1024\n");
		exit(1);
	}

	char input_buf[1024];
	fread(input_buf, length, 1, stdin);
	fwrite(input_buf, length, 1, f);
}
