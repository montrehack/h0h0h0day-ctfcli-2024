package com.montrehack.WinterBoot.gift;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;

import java.io.Serializable;
import java.util.UUID;

@Entity
public class Gift {

    @Id
    @GeneratedValue
    private UUID id;

    @NotBlank(message = "Message cannot be empty.")
    private String message;

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
