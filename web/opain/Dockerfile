FROM golang:1.22.5-alpine@sha256:0d3653dd6f35159ec6e3d10263a42372f6f194c3dea0b35235d72aabde86486e AS deps
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

FROM deps AS build
ENV CGO_ENABLED=0
COPY opain.go .
RUN sed -i "s/FLAG-redacted/FLAG-46fa6417dd4ef07a4d066e19097c7517a0b07401/g" opain.go
RUN go build -o opain

FROM alpine/socat:latest@sha256:7d42e94ae628014cc9c0721d438ac3bfe2c88161e59269ec063c2841b73247eb
COPY --from=build /app/opain /opain
EXPOSE 36086
ENTRYPOINT ["socat"]
CMD ["tcp-l:36086,fork", "exec:timeout 60 /opain"]
