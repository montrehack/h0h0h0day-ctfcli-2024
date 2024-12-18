package com.montrehack.WinterBoot.gift;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class FlagService {

    private final static String FLAG = "FLAG{0H_0H_0H_1T5_CHR15TM4S_THYM3}";

    @Value("${winterboot.superSecretPassword}")
    private String secret;

    public String getFlag(String param) {
        if (secret.equals(param)) {
            return FLAG;
        } else {
            return "Incorrect password";
        }
    }
}
