package com.montrehack.WinterBoot.gift;

import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

@Controller
public class GiftController {

    @Autowired
    private GiftService giftService;

    @GetMapping("/")
    @ResponseStatus(HttpStatus.OK)
    public String getIndex(Model model) {
        model.addAttribute("gift", new Gift());
        return "index";
    }

    @PostMapping("/gift")
    @ResponseStatus(HttpStatus.CREATED)
    public String createGift(Model model, @Valid @ModelAttribute Gift gift, BindingResult result) {
        if (result.hasErrors()) {
            return "index";
        }

        Gift response = giftService.createGift(gift);
        model.addAttribute("giftId", gift.getId());
        model.addAttribute("gift", new Gift());
        return "index";
    }

    @GetMapping("/gift")
    @ResponseStatus(HttpStatus.OK)
    public String getGift(Model model, @RequestParam UUID giftId) {
        Gift gift = giftService.getGift(giftId);
        model.addAttribute("gift", gift);

        return "index";
    }

    @PutMapping("/gift/{giftId}")
    @ResponseStatus(HttpStatus.OK)
    public String updateGift(Model model, @Valid @RequestBody Gift gift, @PathVariable UUID giftId) {
        Gift g = giftService.updateGift(gift, giftId);
        model.addAttribute("gift", g);

        return "index";
    }
}
