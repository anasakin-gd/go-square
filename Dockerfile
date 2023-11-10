# Builder image
FROM golang:1.21-alpine AS build-stage

WORKDIR /app

COPY . .

RUN go mod download

RUN CGO_ENABLED=0 go build -o /square

# Runtime image
FROM alpine:latest

WORKDIR /app

COPY --from=build-stage ./square .

RUN addgroup -S nonroot && adduser -u 1200 -S nonroot -G nonroot

USER nonroot

EXPOSE 8000

# Run the Go application
ENTRYPOINT ["./square"]