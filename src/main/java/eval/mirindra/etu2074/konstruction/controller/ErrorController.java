package eval.mirindra.etu2074.konstruction.controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/error")
public class ErrorController {

    @GetMapping("/404")
    public String error404(){
        return "error/404";
    }

    @GetMapping("/403")
    public String error403(){
        return "error/403";
    }
}
