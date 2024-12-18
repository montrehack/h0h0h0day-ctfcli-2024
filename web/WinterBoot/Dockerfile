FROM gradle:8.4.0-jdk17-alpine AS build
COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle build --no-daemon

FROM openjdk:17
RUN mkdir /app
COPY --from=build /home/gradle/src/build/libs/*.jar /app/WinterBoot.jar

#EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/WinterBoot.jar"]