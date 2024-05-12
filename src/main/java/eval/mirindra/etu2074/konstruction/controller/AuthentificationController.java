package eval.mirindra.etu2074.konstruction.controller;


import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller

public class AuthentificationController {

    @GetMapping
    public String loginPage(){
        return "auth/login";
    }

    @PostMapping("/login")
    public String login(Model model, BindingResult result){
        return "redirect:/extra";
    }

}
