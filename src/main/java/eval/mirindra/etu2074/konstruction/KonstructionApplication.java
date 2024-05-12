package eval.mirindra.etu2074.konstruction;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.reactive.function.client.WebClient;


@SpringBootApplication
public class KonstructionApplication {

	public static void main(String[] args) {
		SpringApplication.run(KonstructionApplication.class, args);
	}

	@Bean
	public WebClient webClient(){
		return WebClient.create("http://127.0.0.1:5000");
	}
}
