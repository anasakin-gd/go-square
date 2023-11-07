# Builder image
FROM golang:1.21 AS build-stage

WORKDIR /app

COPY . .

RUN go mod download

RUN CGO_ENABLED=0 GOOS=linux go build -o /square

# Runtime image
FROM alpine:latest

WORKDIR /app

COPY --from=build-stage ./square .

EXPOSE 8000

# Run the Go application
ENTRYPOINT ["./square"]