package com.montrehack.WinterBoot.gift;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;
import java.util.UUID;


@Service
public class GiftService {

    @Autowired
    private GiftRepository giftRepository;

    public Gift createGift(Gift gift) {
        return giftRepository.save(gift);
    }

    public Gift updateGift(Gift newGift, UUID id) {
        Optional<Gift> optional = giftRepository.findById(id);
        if (optional.isEmpty()) {
            return null;
        }

        Gift gift = optional.get();
        gift.setMessage(newGift.getMessage());
        return giftRepository.save(gift);
    }

    public Gift getGift(UUID id) {
        Optional<Gift> optional = giftRepository.findById(id);
        if (optional.isEmpty()) {
            return null;
        }

        return optional.get();
    }


}
