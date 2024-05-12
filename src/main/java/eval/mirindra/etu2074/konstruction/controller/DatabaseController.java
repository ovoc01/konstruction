package eval.mirindra.etu2074.konstruction.controller;


import eval.mirindra.etu2074.konstruction.service.DatabaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.Map;

@Controller
@RequestMapping("/extra")
public class DatabaseController {

    private DatabaseService databaseService;

    @Autowired
    public DatabaseController(DatabaseService databaseService){
        this.databaseService = databaseService;
    }


    @GetMapping
    public String index(Model model){
        return "extra/index";
    }


    @GetMapping("/resetdb")
    public String resetDb(Model model){
        Map<String, Object> response = databaseService.resetDb();
        if(Integer.valueOf(response.get("status").toString())==200){
            return "redirect:/extra?message="+response.get("message");
        }else{
            return "redirect:/extra?error="+response.get("error");
        }
    }
}
