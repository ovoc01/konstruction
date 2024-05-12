package eval.mirindra.etu2074.konstruction.service;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import java.time.Duration;
import java.util.Map;

@Service
public class DatabaseService {
    private static final Duration REQUEST_TIMEOUT = Duration.ofSeconds(3);
    private final WebClient localApiClient;


    @Autowired
    public DatabaseService(WebClient localApiClient) {
        this.localApiClient = localApiClient;
    }

    public Map<String, Object> resetDb(){
        return localApiClient
                .post()
                .uri("/reset_database")
                .retrieve()
                .bodyToMono(Map.class)
                .block(REQUEST_TIMEOUT);
    }
}
