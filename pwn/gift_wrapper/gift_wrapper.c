#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <openssl/evp.h>

void gift() {
    system("/bin/sh");
}

int main() {
    // Disable buffering
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    // Get the input
    char buffer[32];
    unsigned int md5_len;
    printf("What do you want for Christmas? ");
    fgets(buffer, sizeof(buffer), stdin);

    // Compute the MD5 sum
    unsigned char sum[EVP_MAX_MD_SIZE];
    EVP_MD_CTX *ctx = EVP_MD_CTX_new();
    if (ctx == NULL) {
        fprintf(stderr, "Failed to create EVP_MD_CTX\n");
        return -1;
    }
    if (EVP_DigestInit_ex(ctx, EVP_md5(), NULL) != 1) {
        fprintf(stderr, "EVP_DigestInit_ex failed\n");
        EVP_MD_CTX_free(ctx);
        return -1;
    }
    if (EVP_DigestUpdate(ctx, buffer, strlen(buffer)) != 1) {
        fprintf(stderr, "EVP_DigestUpdate failed\n");
        EVP_MD_CTX_free(ctx);
        return -1;
    }
    if (EVP_DigestFinal_ex(ctx, sum, &md5_len) != 1) {
        fprintf(stderr, "EVP_DigestFinal_ex failed\n");
        EVP_MD_CTX_free(ctx);
        return -1;
    }
    EVP_MD_CTX_free(ctx);

    // Copy the first 4 bytes of the sum
    void* code = mmap(NULL, 4096, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_SHARED | MAP_ANONYMOUS, 0, 0);
    if (code == (void*)-1) {
        fprintf(stderr, "mmap failed\n");
        return -1;
    }
    memcpy(code, sum, 4);

    // Modify the code
    printf("The gift is wrapped, now you can add a bow.\nChoose a side on the gift (0-3): ");
    fgets(buffer, sizeof(buffer), stdin);
    unsigned long index = strtoul(buffer, NULL, 10);
    if (index >= 4) {
        printf("Index invalide");
        exit(-1);
    }
    printf("Enter the size of the bow (0-255): ");
    fgets(buffer, sizeof(buffer), stdin);
    unsigned char value = strtoul(buffer, NULL, 10) % 256;
    ((unsigned char*)code)[index] = value;

    // Jump to the code
    void (*func_ptr)() = (void (*)())code;
    func_ptr();

    return 0;
}