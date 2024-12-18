package com.montrehack.WinterBoot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.data.rest.RepositoryRestMvcAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
public class WinterBootApplication {

	public static void main(String[] args) {
		SpringApplication.run(WinterBootApplication.class, args);
	}

}
